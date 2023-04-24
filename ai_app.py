""" Script for AI-APP """

import streamlit as st

import modules.main as main

st.set_page_config(
    page_title="Langchain Boilerplate", page_icon=":shark:", layout="wide"
)

main.app()
