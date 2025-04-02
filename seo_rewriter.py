from transformers import pipeline


try:
    rewriter = pipeline("text2text-generation", model="humarin/chatgpt_paraphraser_on_T5_base")
    print(" Model loaded successfully.")
except Exception as e:
    print(f" Error loading model: {e}")

def rewrite_content(content):
    """Rewrites content for better SEO using a paraphraser model."""
    try:
        if not content or len(content) < 10:
            return "Error: Content too short to optimize."

        prompt = f"Paraphrase: {content}"  
        response = rewriter(prompt, max_length=100, num_return_sequences=1, do_sample=True)

        print(f"🔹 Raw Response: {response}") 

        return response[0].get('generated_text', ' No text generated!') 

    except Exception as e:
        return f" Error generating text: {e}"

