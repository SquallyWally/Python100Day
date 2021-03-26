# new_dict = {new_key:new_value for (key,value) in dict.items() if condition}
import random

names = ["Lex", "Io", "Beth", "Caroline", "Eleanor", "Batista"]

students_score = {student: random.randint(1, 100) for student in names}

passed_student = {student: score for (student, score) in students_score.items() if score >= 55}
