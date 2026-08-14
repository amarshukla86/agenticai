from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="You are a helpful assistant that explains concepts in a clear and concise manner. For the user's question, 'Explain Artificial Intelligence.', you should explain what Artificial Intelligence is and how it works. You should also include examples of how Artificial Intelligence is used in the real world.",
    input="Explain Artificial Intelligence.",    
    temperature=0.5
)

print(response.output_text)
