from langchain.prompts import ChatPromptTemplate

# Define your prompt templates
prompt_essay = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt_poem = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")
