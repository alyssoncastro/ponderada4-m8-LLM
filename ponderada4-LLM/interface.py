import os
import gradio as gr
import random
from dotenv import load_dotenv
from langchain.llms import OpenAI

# API Key ChatGPT
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Configuração do modelo LLM com streaming
llm = OpenAI(api_key=api_key, model="gpt-3.5-turbo-instruct", max_tokens=512)

def preparar_prompt(pergunta):
    return f"""
    Pergunta do usuário: '{pergunta}'
    Contexto: Normas de segurança em ambientes industriais. contextualiza todas as respostas.
    """

def chatbot(pergunta):
    resposta = ""
    for chunk in llm.stream(preparar_prompt(pergunta)):
        resposta += chunk
    return resposta

def random_response(message, history):
    return random.choice(["Olá, como posso ajudar?", " "])


def is_question(message):
    if message[-1] == "?":
        return True
    return False


#Gradio interface
def interface(message, history):
    if is_question(message):
        resposta = chatbot(message)
    else:
        resposta = random_response(message, history)
    return resposta

demo = gr.ChatInterface(interface)

demo.launch()
