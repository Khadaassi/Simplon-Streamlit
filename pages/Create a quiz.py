import streamlit as st
from pydantic import ValidationError
from quiz_models import Question

from config.json_utils import read_json, write_json

# Define the full path to the JSON file in the config folder
json_file_path = 'config/data.json'

st.page_link(icon="🏠",page="Home page.py", label= "Home page")
# Quiz creation interface
st.html("<h1 style='text-align: center;'>Create Your QUIZ</h1>")

with st.form(key="quiz_form", clear_on_submit=True):
    question_text = st.text_input("Enter the question:")
    answer_1 = st.text_input("Enter answer 1.")
    answer_2 = st.text_input("Enter answer 2.")
    answer_3 = st.text_input("Enter answer 3.")
    answers = {
        "Answer 1": answer_1,
        "Answer 2": answer_2,
        "Answer 3": answer_3
    }
    correct_answer_key = st.radio("Choose the correct answer", list(answers.keys()))
    submitted = st.form_submit_button("Submit")

    if submitted:
        if not question_text or not answer_1 or not answer_2 or not answer_3:
            st.error("Please fill in all fields before submitting.")
        else:
            correct_answer = answers[correct_answer_key]
            
            # Validate the question using pydantic
            try:
                new_question = Question(
                    Question=question_text,
                    Answers=answers,
                    Correct_Answer=correct_answer
                )
                # If validation passes, read, append, and write to JSON
                existing_data = [Question(**entry) for entry in read_json(json_file_path)]
                existing_data.append(new_question)

                write_json(json_file_path, existing_data)
                st.success("Question successfully submitted!")

            except ValidationError as e:
                st.error(f"Validation error: {e}")


left_column, right_column = st.columns(2)

# Preview existing questions
with left_column:
    with st.expander("Show saved questions"):
        questions_data = read_json(json_file_path)
        if questions_data:
            for i, question_entry in enumerate(questions_data, start=1):
                st.write(f"**Question {i}:** {question_entry['Question']}")
                for idx, ans in enumerate(question_entry['Answers'], start=1):
                    st.write(f"- Answer {idx}: {ans}")
                st.write(f"**Correct answer:** {question_entry['Correct_Answer']}")
                st.write("---")
        else:
            st.info("No questions saved.")

# Quiz launch functionality (simple display for now)
with right_column:
    st.markdown(
        """
        <style>
        .custom-button {
            display: block;
            margin: auto;
            padding: 8px 30px;
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
        <a href="http://localhost:8501/Quiz" class="custom-button">Launch the quiz</a>
        """,
        unsafe_allow_html=True
    )
