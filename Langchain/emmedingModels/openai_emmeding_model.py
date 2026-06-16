from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=32,  
    openai_api_key=api_key  
)

result = embedding.embed_query("Delhi is the capital of India")
print(f"Vector length: {len(result)}")
print(result[:5])