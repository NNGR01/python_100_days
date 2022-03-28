from question_model import Question 
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
  x_text = x['text']
  x_aswer = x['answer']
  q_question = Question(x_text, x_aswer)
  question_bank.append(q_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question() 

print("You have finish the test") 
print(f"Youre score are : {quiz.score}/{len(question_bank)} ") 