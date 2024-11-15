import streamlit as st

st.image("images/quiz_banner.png", use_container_width=True)

st.html("<h1 style='text-align: center;'>Home</h1>")

st.write("Welcome to the home page!")

# Button to redirect to the quiz creation page
st.markdown(
    """
    <style>
    .custom-button {
        display: block;
        margin: auto;
        padding: 15px 20px;
        font-size: 18px;
        color: black;
        text-decoration: none;
        border: 1px solid;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
        background-color: transparent;
    }

    .custom-button:hover {
        color: black;
    }

    /* Dark mode detection */
    @media (prefers-color-scheme: dark) {
        .custom-button {
            color: white; /* White text by default in dark mode */
            border-color: white; /* White border in dark mode */
        }
        .custom-button:hover {
            color: white; /* Keep white text on hover in dark mode */
        }
    }
    </style>
    <a href="http://localhost:8501/Create_a_quiz" class="custom-button">Create a quiz</a>
    """,
    unsafe_allow_html=True
)

# Button to redirect to the quiz page
st.markdown(
    """
    <style>
    .custom-button {
        display: block;
        margin: auto;
        padding: 15px 20px;
        font-size: 18px;
        color: black;
        text-decoration: none;
        border: 1px solid;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
        background-color: transparent;
    }

    .custom-button:hover {
        color: black;
    }

    /* Dark mode detection */
    @media (prefers-color-scheme: dark) {
        .custom-button {
            color: white; /* White text by default in dark mode */
            border-color: white; /* White border in dark mode */
        }
        .custom-button:hover {
            color: white; /* Keep white text on hover in dark mode */
        }
    }
    </style>
    <a href="http://localhost:8501/Start_a_quiz" class="custom-button">Start a quiz</a>
    """,
    unsafe_allow_html=True
)
