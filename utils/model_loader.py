import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal, Optional, Any
# from langchain_huggingface import HuggingFaceEmbeddings
from utils.config_loader import load_config
from langchain_groq import ChatGroq



class ConfigLoader():
    def __init__(self):
        print("Loading Config...")
        self.config = self.load_config()
    
    def __getitem__(self, key):
        return self.config[key]
    

class ModelLoader(BaseModel):
    model_provider : Literal["groq"] = "groq"
    config : Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, _context: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("LLM Loading ....")
        print(f"Loading Model from provider": {self.model_provider})
        if self.model_provider == "groq":
            print("Loading LLM model from Groq...")
            GROQ_API_KEY = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model_name=model_name, api_key=GROQ_API_KEY)
        return llm
    


