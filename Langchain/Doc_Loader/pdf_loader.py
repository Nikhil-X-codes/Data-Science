from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Letter.pdf")

docs = loader.load()

print(f"Total Pages: {len(docs)}")

for i, doc in enumerate(docs):
    print("\n" + "="*60)
    print(f"Page: {i+1}")
    print(f"Metadata: {doc.metadata}")
    print(f"Content:\n{doc.page_content}")