
FROM python:3.11-slim

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


RUN python -c "from transformers import pipeline; pipeline('text2text-generation', model='humarin/chatgpt_paraphraser_on_T5_base')"


EXPOSE 5000


CMD ["python", "app.py"]
