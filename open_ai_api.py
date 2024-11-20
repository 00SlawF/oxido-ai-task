import os
from openai import OpenAI
key = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key = key)

text = input("Ask ChatGPT for something:\n")

prompt = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{"role": "user", "content": text}],
)

print(prompt.choices[0].message.content)
