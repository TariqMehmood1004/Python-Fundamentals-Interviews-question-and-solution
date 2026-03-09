from dotenv import load_dotenv
load_dotenv()  # loads OPENAI_API_KEY from .env


from openai import OpenAI


client = OpenAI()


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Explain microservices"}
    ]
)

print(response.choices[0].message.content)