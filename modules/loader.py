""" Module for defining chain or agent"""

from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI


def load_chain(api_key):
    """Logic for loading the chain/agent goes here"""
    llm = ChatOpenAI(temperature=0, openai_api_key=api_key)
    chain = ConversationChain(llm=llm)
    return chain
