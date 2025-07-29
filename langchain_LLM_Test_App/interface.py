import streamlit as st

st.title("Prompt Generator")
llm_name = st.sidebar.selectbox("Which LLMS do you want to consider?", ("Select", "LangChain", "LlamaIndex", "Haystack"))

if llm_name == "LangChain":
    llm_type = st.sidebar.text_area(label="Do you want to learn more about LangChain? Enter: (Y/n)", max_chars=100)

elif llm_name == "LlamaIndex":
    llm_type = st.sidebar.text_area(label="Do you want to learn more about LlamaIndex? Enter: (Y/n)", max_chars=100)
        
elif llm_name == "Haystack":
    llm_type = st.sidebar.text_area(label="Do you want to learn more about Haystack? Enter: (Y/n)", max_chars=100)