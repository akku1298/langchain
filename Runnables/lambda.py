from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.8-flash')

def word_count(text):
    return len(text.split())

prompt1 =PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()




joke_gen_chain = RunnableSequence(prompt1, model, parser)
paralle_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation':RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain,paralle_chain)

result = final_chain.invoke({'topic':'AI'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)