from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

vragen_bank = []

for element in question_data:
    '''Voegt een nieuwe vraag toe'''
    element_text = element["question"]
    element_antwoord = element["correct_answer"]
    new_vraag = Question(element_text, element_antwoord)
    vragen_bank.append(new_vraag)

quiz = QuizBrain(vragen_bank)
# quiz bevat nog vragen
while quiz.still_has_questions():
    quiz.next_question()


print("AFGELOPEN")
print(f"Final Score was : {quiz.score}/{quiz.question_number}")
#TODO: Check open TriviaDB