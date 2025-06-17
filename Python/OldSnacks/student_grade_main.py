import student_grade
from student_grade import *

while True:

	num_of_students = int(input('How many students do you have? '))
	
	if num_of_students > 0:
		break
	else:
		print('Invalid input, please enter a valid number')

while True:

	num_of_subjects = int(input('How many subjects do they offer? '))

	if num_of_subjects > 0:
		break
	else:
		print('Invalid input, please enter a valid number')

print("\nSaving >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Saved Successfully\n")


grades = score_and_grade(num_of_students, num_of_subjects)
grade_calculation(grades)
subject_summary(grades)
class_summary(grades)