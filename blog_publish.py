import os


from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama

#from langchain_core.globals import set_debug

#set_debug(True)

 
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o-mini",api_key=OPENAI_API_KEY)
title_prompt= PromptTemplate(
    input_variables=["topic"],
    template ="""You are an experienced speech writer.
    You need to write a blog post for
    the following topic: {topic} 
    Answer exactly with one title.
    """
    )

speech_prompt= PromptTemplate(
    input_variables=["topic"],
    template ="""You need to write a blog post with Introduction , 3 main points with subpoints and conclusion
    for the following topic: {topic} 

    """
    )
EMOTIONS = [
    "Inspiring", "Passionate", "Empathetic", "Motivational", "Heartfelt",
    "Uplifting", "Empowering", "Sincere", "Hopeful", "Enthusiastic",
]
emotion = st.selectbox("Tone", EMOTIONS)

st.title("Speech Generator")
topic = st.text_input("Enter a topic ")

if topic:
    chain = speech_prompt | llm
    response = chain.invoke({"topic": topic}, {"emotion": emotion})
    st.write(response.content)

