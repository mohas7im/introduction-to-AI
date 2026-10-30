import requests
import streamlit as st


def get_poem(topic):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={"input": {"topic": topic}},
    )
    response.raise_for_status()
    return response.json()["output"]["content"]


st.title("Poem Generator")
topic = st.text_input("Enter a topic for the poem")

if topic:
    st.write(get_poem(topic))
