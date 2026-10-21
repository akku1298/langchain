from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','You are helpful {domain} expert'),
    ('human','Exaplin in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain': 'LLM', 'topic':'Embeddings'})

print(prompt)