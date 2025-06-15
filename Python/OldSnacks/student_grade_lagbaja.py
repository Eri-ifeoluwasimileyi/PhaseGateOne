def score_and_grade(num_of_students, num_of_subjects):

	grades = []

	for student in range(num_of_students):
		
		student_scores = []
		
		for subject in range(num_of_subjects):
	
			while True:

				print(f'Entering score for student {student + 1}')

				score = int(input(f'Enter score for subject {subject + 1}: '))

				if score > 0 and score <= 100:
					print()
					print('\nSaving >>>>>>>>>>>>>>>>>>>>>>>>>>>>')
					student_scores.append(score)
					print('Saved Successfully\n')
					print()
					break
				else:
					print('Invalid input, Try Again')
		
		grades.append(student_scores)
	
	return grades



def grade_calculation(grades):

	num_of_students = len(grades)
	num_of_subjects = len(grades[0])

	total_score = []

	for student in range(num_of_students):
	
		total = 0

		for subject in range(num_of_subjects):

			total += grades[student][subject]

		total_score.append(total)

	print('=============================================================================')
	print('STUDENT\t\t', end='')
	
	for index in range(num_of_subjects):
		print(f'SUB{index + 1}\t', end='')

	print('TOT\tAVE\tPOS')
	print()

	print('=============================================================================')
	
	for student in range(num_of_students):
		print(f'Student {student + 1}', end='')

		for subject in range(num_of_subjects):
			print(f'\t{grades[student][subject]}', end='')

		total = total_score[student]
		average = total / num_of_subjects

		position = 1
		for counter in range(num_of_students):
			if total_score[counter] > total:
				position += 1

		print(f'\t{total}\t{average:.2f}\t{position}')
		print()

	print('=============================================================================')
	print('=============================================================================')
	print()
