from flask import Flask, request, jsonify
from seo_rewriter import rewrite_content
from seo_analyzer import analyze_seo

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to AI SEO Optimizer API!"})

@app.route("/analyze", methods=["GET"])
def seo_analyze():
    """Analyzes website content for SEO optimization."""
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL parameter missing."})

    seo_data = analyze_seo(url)
    return jsonify(seo_data)

@app.route("/rewrite", methods=["POST"])
def seo_rewrite():
    """Rewrites content for better SEO ranking."""
    data = request.json
    content = data.get("content", "")

    if not content:
        return jsonify({"error": "No content provided for rewriting."})

    optimized_text = rewrite_content(content)
    return jsonify({"optimized_content": optimized_text})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)





