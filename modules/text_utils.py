""" Module for defining prompts and instructions"""

from langchain.prompts.prompt import PromptTemplate

_DEFAULT_TEMPLATE = """
                    You are an AI answering a variety of question the human user might have. 
                    The AI is talkative and provides lots of specific details from its context.
                    If the AI does not know the answer to a question, it truthfully says it does not know.

                    Human: {input}
                    AI:
                    """

PROMPT = PromptTemplate(input_variables=["input"], template=_DEFAULT_TEMPLATE)
