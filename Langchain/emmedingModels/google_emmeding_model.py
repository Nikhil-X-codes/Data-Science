from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", 
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


text = "The capital of India is New Delhi"
vector = embeddings.embed_query(text)
print(f"Vector length: {len(vector)}") 
print(vector[:5])  