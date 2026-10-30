from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI(title="LangChain Server", version="1.0", description="A simple API server")

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("Write me a poem about {topic} in about 100 words")

add_routes(app, model, path="/openai")
add_routes(app, prompt | model, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
