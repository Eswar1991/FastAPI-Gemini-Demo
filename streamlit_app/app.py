import streamlit as st
import requests

st.title("AI Text Generator with Gemini & Perplexity (via FastAPI API)")

# User inputs topic
topic = st.text_input("Enter a topic:")

# Select endpoint for generation
endpoint = st.selectbox(
    "Choose generation type",
    options=[
        ("Gemini Essay", "essay-direct"),
        ("Gemini Poem", "poem-direct")
    ],
    format_func=lambda x: x[0]  # display the name, but return endpoint value
)

if st.button("Generate") and topic.strip():
    # Build FastAPI URL (assuming running locally on port 8000)
    base_url = "http://localhost:8000"
    url = f"{base_url}/{endpoint[1]}"
    
    # Query params
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
