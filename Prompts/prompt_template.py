from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

model = ChatGoogleGenerativeAI(model='gemini-3.8-flash')

template = PromptTemplate(
    template='Tell this person about the city in 10 lines. the name of city is {name}',
    input_variables=['name']
)

prompt = template.invoke({'name':'jaipur'})

result = model.invoke(prompt)

print(result.content)