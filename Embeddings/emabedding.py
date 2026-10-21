from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001')

result = model.embed_query("What is capital of India")

print(result)