""" Module for UI """

import streamlit as st

from modules.loader import load_chain


def app():
    """Create the interface of the app"""

    # track session states
    if "generated" not in st.session_state:
        st.session_state["generated"] = []
    if "past" not in st.session_state:
        st.session_state["past"] = []

    api_key = st.sidebar.text_input(
        "OpenAI API key",
        help="You can get your free API token from [here](https://platform.openai.com/account/api-keys).",
        type="password",
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("App created by [Franz Buchmann](https://www.linkedin.com/in/franz-buchmann/)")

    if api_key:
        chain = load_chain(api_key=api_key)
        st.title("Langchain boilerplate")
        st.write("Introduction to the app goes here.")

        s_example = "This is a question"
        inp = st.text_area(
            "Use the question below or input your own question in English",
            value=s_example,
            max_chars=150,
            height=100,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                output = chain.run(inp)
                st.markdown(output)
                st.session_state.past.append(inp)
                st.session_state.generated.append(output)

    else:
        st.error("🔑 Please enter your OpenAI API Key to load the app")
