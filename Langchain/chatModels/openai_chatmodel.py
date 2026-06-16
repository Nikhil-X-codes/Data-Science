from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    model='gpt-4o-mini',          
    temperature=0.7,               
    max_completion_tokens=150     
)

result = model.invoke("Write a 5 line poem on cricket")
print(result.content)