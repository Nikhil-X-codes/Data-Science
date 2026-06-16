from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}",
    input_variables=["topic"]
)

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": prompt1 | model | parser,
    "linkedin": prompt2 | model | parser
})

result = parallel_chain.invoke({"topic": "AI"})

print("Tweet:")
print(result["tweet"])

print("\nLinkedIn Post:")
print(result["linkedin"])

# parallel_chain.get_graph().print_ascii()