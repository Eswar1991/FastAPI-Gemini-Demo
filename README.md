Certainly! Here’s a fully updated, **Gemini-powered project overview and workflow** for your LLM-Chatbot-with-FastAPI-and-Streamlit, reflecting your new code and architecture. This replaces references to OpenAI, Groq, and Ollama with your direct Gemini client functions, updated endpoints, and a Streamlit interface that calls your FastAPI Gemini endpoints.

# LLM-Chatbot-with-FastAPI-and-Streamlit (Google Gemini Version)

This project enables you to generate creative text content using Google's Gemini LLM. FastAPI serves as your API backend, and Streamlit provides an interactive web UI. The architecture showcases modern Python best practices, clear modularization, and makes all text generation calls via your own FastAPI endpoints.

## 🚀 Key Technologies and Structure

- **FastAPI:** High-performance Python web API framework.
- **Google Gemini API (google-genai):** For direct LLM-powered content generation.
- **Prompt Templates:** For structured essay and poem generation.
- **Custom Python Functions:** Your own `generate_essay` and `generate_poem` logic, using your Gemini client.
- **Streamlit:** The web interface, which interacts with the FastAPI server via HTTP requests.
- **LangServe & Langchain (optional):** You may add these if you wish for further modular chains.
- **dotenv:** Securely manages your API key/environment variables.
- **Modular Folder Structure:** Keeps code for API endpoints, prompt templates, Gemini client, and Streamlit UI clearly separated.

## 1. Environment Variables (`.env`)

Create a `.env` file at the root of your project:

```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

> **Never share your API keys publicly! They are sensitive and should stay private.**

## 2. Python Requirements

Install all necessary libraries:

```bash
pip install fastapi google-genai python-dotenv uvicorn streamlit requests
```

## 3. FastAPI Backend Usage

**app/gemini_client.py:**
```python
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
```

**app/gemini_tasks.py:**
```python
from google.genai import types
from app.gemini_client import client

def generate_essay(topic: str, model="gemini-1.5-flash"):
    prompt = f"Write me an essay about {topic} with 100 words"
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            max_output_tokens=250
        ),
    )
    return response.text

def generate_poem(topic: str, model="gemini-1.5-flash"):
    prompt = f"Write me a poem about {topic} with 100 words"
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            max_output_tokens=250
        ),
    )
    return response.text
```

**app/routes.py:**
```python
from fastapi import FastAPI, Query
from app.gemini_tasks import generate_essay, generate_poem

def setup_routes(app: FastAPI):
    @app.get("/essay-direct")
    def essay_direct(topic: str = Query(..., description="Topic to generate essay about")):
        return {"result": generate_essay(topic)}

    @app.get("/poem-direct")
    def poem_direct(topic: str = Query(..., description="Topic to generate poem about")):
        return {"result": generate_poem(topic)}
```

**app/main.py:**
```python
from fastapi import FastAPI
from app.routes import setup_routes
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Gemini Text Generator API",
    version="1.0",
    description="FastAPI server with Gemini LLM"
)

setup_routes(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
```

## 4. Streamlit Web Interface

**streamlit_app/app.py:**
```python
import streamlit as st
import requests

st.title("AI Text Generator with Gemini (via FastAPI API)")

topic = st.text_input("Enter a topic:")

endpoint = st.selectbox(
    "Choose generation type",
    options=[
        ("Gemini Essay", "essay-direct"),
        ("Gemini Poem", "poem-direct"),
    ],
    format_func=lambda x: x[0]
)

if st.button("Generate") and topic.strip():
    base_url = "http://localhost:8000"
    url = f"{base_url}/{endpoint[1]}"
    params = {"topic": topic}

    with st.spinner(f"Calling endpoint `{endpoint[0]}`..."):
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            result = data.get("result", "No result found.")
            st.markdown("### Generated Text:")
            st.write(result)
        except Exception as e:
            st.error(f"API call failed: {e}")
else:
    st.info("Please enter a topic and click Generate.")
```

## 5. How to Run the Application

**a. Start the FastAPI Server:**

```bash
python -m app.main
```

**b. In a separate terminal, start Streamlit:**

```bash
python -m streamlit run streamlit_app/app.py
```

- Visit `http://localhost:8501` in your browser.
- Generate essays and poems by selecting your desired generation type.

## 🟢 Basic Workflow

1. **Run the FastAPI server** (Gemini-powered endpoints ready).
2. **Launch Streamlit UI** for user interaction.
3. **User chooses essay or poem, enters a topic, presses generate.**
4. **Streamlit calls the backend endpoint and displays the Gemini-generated text.**

## 📝 Additional Notes

- Only Gemini-powered endpoints are used for content generation.
- You can add further endpoints or models by expanding backend logic.
- Make sure you have a working, active Gemini API key.
- Ports or URLs can be adjusted as needed.

**You now have a fully integrated, Gemini-powered API and UI stack, with each component calling your robust content generation endpoints!**
