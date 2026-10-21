🦜 LangChain Model Practice
A hands-on repository for learning and practicing the core concepts of LangChain through simple Python examples and experiments.
📚 Topics Covered
🤖 Chat Models
Learning how to work with chat-based language models, send messages, and handle model responses.
🧠 LLM
Exploring the basics of interacting with Large Language Models using LangChain.
🔤 Embeddings
Understanding how text is converted into numerical vector representations and how embedding models work.
📝 Prompts
Practicing prompt creation and reusable Prompt Templates for interacting with language models.
🔎 Output Parsers
Learning how to parse and process LLM responses into useful formats.
🔗 Runnables
Understanding Runnables and LCEL (LangChain Expression Language) for connecting different LangChain components and creating simple pipelines.
🧩 Structured Output
Learning how to generate structured responses from LLMs using different Python data structures.

Examples include:
- JSON
- Pydantic
- TypedDict
Structured_Output/
├── output_json.py
├── output_pydantic.py
├── output_typeddict.py
└── typeddict_demo.py

✂️ Text Splitters
Learning how to divide large text into smaller chunks for further processing.

Examples include:
- Length-based splitting
- Structure-based splitting
Text_Splitter/
├── length_based.py
└── text_structure_based.py

📁 Project Structure
langchain-model/
│
├── ChatModel/
├── Embeddings/
├── LLM/
├── Output_Parser/
├── Prompts/
├── Runnables/
├── Structured_Output/
├── Text_Splitter/
│
├── .env
├── .gitignore
├── requirements.txt
├── template.json
└── test.py

⚙️ Setup
Create Virtual Environment
python -m venv venv

Activate Environment
Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Environment Variables
Add the required API keys to your .env file:
OPENAI_API_KEY=your_api_key_here

Keep .env private and never commit API keys to GitHub.

🎯 Goal
The goal of this repository is to build a strong understanding of LangChain fundamentals through hands-on practice.

The concepts learned here will eventually be used to build more advanced applications such as RAG systems, AI assistants, agents, and other LLM-powered applications.