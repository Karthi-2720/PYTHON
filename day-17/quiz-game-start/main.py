from data import question_data
from question_model import Question
from quiz_brain import Quizbrain
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()


print("you completed the quiz.")
print(f"you final score is {quiz.score}/{quiz.question_number}.")
