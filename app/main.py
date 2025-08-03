import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes import setup_routes

load_dotenv()  # load .env variables

app = FastAPI(
    title="Langchain Gemini Server",
    version="1.0",
    description="FastAPI server with Langchain and Gemini LLM",
)

# setup the API routes using our defined routes
setup_routes(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
