from typing import Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

# output structure
class UserCommand(BaseModel):
    intent: str = Field(description="Intent of the command: add, remove, or update")
    email: str = Field(default=None, description="User's email")
    name: Optional[str] = Field(default=None, description="User's name")
    phone: Optional[str] = Field(default=None, description="User's phone number")
    city: Optional[str] = Field(default=None, description="User's city")

# Load LLaMA model using ChatGroq
llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))

parser = PydanticOutputParser(pydantic_object=UserCommand)

prompt = PromptTemplate(
    template="""
You are a chatbot system that helps admins manage user data.
Strictly return only valid JSON in the format below:

{format_instructions}

Command: {command}

JSON:
""",
    input_variables=["command"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | llm | parser

def parse_with_llm(command: str) -> dict:
    try:
        return chain.invoke({"command": command}).dict()
    except Exception as e:
        print("[LLM Parsing Error]", e)
        return {
            "intent": None,
            "email": None,
            "name": None,
            "phone": None,
            "city": None
        }