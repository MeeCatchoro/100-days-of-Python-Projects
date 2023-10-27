from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for n in range(len(question_data)):
    question_text = question_data[n]["question"]
    question_answer = question_data[n]["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)

while QuizBrain.still_has_questions(quiz):
    QuizBrain.next_question(quiz)

print("You've completed the quiz!")
print(f"Your final iscore was: {quiz.score}/{quiz.question_number}.")
