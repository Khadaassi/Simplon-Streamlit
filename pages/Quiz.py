import streamlit as st
from config.json_utils import read_json
from random import shuffle

questions = read_json('config/data.json')
# st.session_state["test"] = False

# Initialize session state variables if they do not exist
if 'current_question_index' not in st.session_state:
    st.session_state['current_question_index'] = 0
if 'score' not in st.session_state:
    st.session_state['score'] = 0

# Quiz page
st.markdown("<h1 style='text-align: center;'>QUIZ</h1>", unsafe_allow_html=True)
st.write("Welcome to the quiz page!")

# Display the current question
if st.session_state['current_question_index'] < len(questions):
    question = questions[st.session_state['current_question_index']]
    
    # Form to handle submission
    with st.form(key=f"form_{st.session_state['current_question_index']}"):
        st.write(f"Question {st.session_state['current_question_index'] + 1}: {question['Question']}")
        
        # Display multiple-choice answers
        user_answer = st.radio("Choose your answer:", question['Answers'].values(), key=f"question_{st.session_state['current_question_index']}")
        
        # value_button = "submit" if st.session_state["test"] else "next"
        # Submit button
        submitted = st.form_submit_button("Submit")
        
        if submitted:  # Check if the button was clicked
            if user_answer == question['Correct_Answer']:
                st.success("Correct answer!")
                st.session_state['score'] += 1
            else:
                st.error("Wrong answer.")
            # Move to the next question after submission
            st.session_state['current_question_index'] += 1
        # st.session_state["test"] = False if st.session_state["test"] else True

else:
    st.write("Quiz completed!")
    st.write(f"Your score: {st.session_state['score']}/{len(questions)}")
    if st.session_state['score'] > len(questions) / 2:
        st.balloons()

# Reset the quiz
    if st.button("Restart the quiz"):
        st.session_state['current_question_index'] = 0
        st.session_state['score'] = 0
        st.rerun()
