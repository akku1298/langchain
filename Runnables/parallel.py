from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.8-flash')

prompt1 =PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)



paralle_chain = RunnableParallel({
    'joke': RunnableSequence(prompt1,model,parser),
    'explanation':RunnableSequence(prompt2, model, parser)
})

result= paralle_chain.invoke({'topic':'AI'})

print(result['joke'])