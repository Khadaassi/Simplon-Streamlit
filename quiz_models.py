from pydantic import BaseModel

class Question(BaseModel):
    Question: str
    Answers: dict
    Correct_Answer: str

# class Quizz(BaseModel):
#     questions = list[Question]
