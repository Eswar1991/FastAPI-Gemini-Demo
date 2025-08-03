from google.genai import types
from app.gemini_client import client  # or update import based on your actual folder

def generate_essay(topic: str, model="gemini-1.5-flash"):
    prompt = f"Write me an essay about {topic} with 100 words"
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            max_output_tokens=250  # Add this parameter directly if supported
        )
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
        )
    )
    return response.text
