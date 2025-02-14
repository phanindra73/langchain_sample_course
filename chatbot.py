from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
import gradio as gr
from dotenv import load_dotenv, find_dotenv
import os

# Find and load .env from the root directory
load_dotenv(find_dotenv())

my_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = my_key

llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=my_key)

# Define a function to generate responses

def chatbot_response(user_input):
    messages = [HumanMessage(content=user_input)]
    response = llm(messages)
    return response.content
#Create a Gradio interface
iface = gr.Interface(fn=chatbot_response, inputs=gr.Textbox(placeholder="Type your message here..."), outputs="text", title="LangChain Chatbot")
iface.launch(share=True)

