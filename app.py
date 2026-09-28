import streamlit as st

from agent.agent import app


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖",
    layout="centered"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🤖 AI Research Agent")

st.write(
    "Ask a question and let the AI agent decide "
    "which tool to use."
)


# --------------------------------------------------
# User Input
# --------------------------------------------------

question = st.text_input(
    "Enter your question:"
)


# --------------------------------------------------
# Ask Button
# --------------------------------------------------

if st.button("Ask Agent"):

    if question.strip() == "":

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Researching..."
        ):

            result = app.invoke(
                {
                    "messages": [
                        (
                            "user",
                            question
                        )
                    ]
                }
            )


        # ------------------------------------------
        # Get final answer
        # ------------------------------------------

        final_answer = result[
            "messages"
        ][-1].content


        # ------------------------------------------
        # Display answer
        # ------------------------------------------

        st.subheader(
            "Answer"
        )

        st.write(
            final_answer
        )