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




def subject_summary(grades):

	num_of_students = len(grades)
	num_of_subjects = len(grades[0])

	print()
	print('\nSUBJECT SUMMARY')

	for subject in range(num_of_subjects):

		total_in_subject = 0
		highest_score = -999999
		lowest_score = 999999
		best_student = 0
		worst_student = 0
		count_pass = 0
		count_fail = 0
	
		for student in range(num_of_students):
		
			score = grades[student][subject]

			total_in_subject += score	

			if score > highest_score:
				highest_score = score
				best_student = student + 1

			if score < lowest_score:
				lowest_score = score
				worst_student = student + 1

			if score >= 50:
				count_pass += 1

			else:
				count_fail += 1

		average_in_sub = total_in_subject / num_of_students

		print(f'Subject {subject + 1}')
		print(f'Highest scoring student is: student {best_student} scoring {highest_score}')
		print(f'Lowest scoring student is: student {worst_student} scoring {lowest_score}')
		print(f'Total score is: {total_in_subject}')
		print(f'Average score is: {average_in_sub:.2f}')
		print(f'Number of passes: {count_pass}')
		print(f'Number of fails: {count_fail}\n')
		print()

	

def class_summary(grades):
	
	num_of_students = len(grades)
	num_of_subjects = len(grades[0])	

	student_total_score = []
	highest_total_score = -999999
	lowest_total_score = 999999
	best_student = 0
	worst_student = 0
	class_total = 0

	
	for student in range(num_of_students):
		total = 0

		for subject in range(num_of_subjects):

			total += grades[student][subject]

		student_total_score.append(total)
		class_total += total

		if total > highest_total_score:
			highest_total_score = total
			best_student = student + 1

		if total < lowest_total_score:
			lowest_total_score = total
			worst_student = student + 1

	class_average = class_total / num_of_students
		
	most_fail = 0
	most_pass = 0
	hardest_subject = 0
	easiest_subject = 0
	
	for subject in range(num_of_subjects):

		count_pass = 0
		count_fail = 0

		for student in range(num_of_students):
			if grades[student][subject] >= 50:
				count_pass += 1
			else:
				count_fail += 1

		if count_fail > most_fail:
			most_fail = count_fail
			hardest_subject = subject + 1

		if count_pass > most_pass:
			most_pass = count_pass
			easiest_subject = subject + 1

	
	overall_high_score = grades[0][0]
	overall_low_score = grades[0][0]
	highest_score_student = 0
	lowest_score_student = 0
	high_score_sub = 0
	low_score_sub = 0

	for student in range(num_of_students):

		for subject in range(num_of_subjects):
			score = grades[student][subject]
			if score > overall_high_score:
				overall_high_score = score
				highest_score_student = student + 1
				high_score_sub = subject + 1

			if score < overall_low_score:
				overall_low_score = score
				lowest_score_student = student + 1
				low_score_sub = subject + 1


	
	print(f'The hardest subject is {hardest_subject} with {most_fail} failures')
	print(f'The easiest subject is {easiest_subject} with {most_pass} passes')
	print(f'The overall Highest score is scored by student {highest_score_student} in subject {high_score_sub} scoring {overall_high_score}')
	print(f'The overall Lowest score is scored by student {lowest_score_student} in subject {low_score_sub} scoring {overall_low_score}')

	print('=============================================================================')
	print()
	print('\nCLASS SUMMARY')
	print('=============================================================================')
	print(f'Best Graduating Student is: student {best_student} scoring {highest_total_score}')
	print('=============================================================================')
	print()
	print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
	print(f'Worst Graduating Student is: student {worst_student} scoring {lowest_total_score}')

	print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
	print()
	print('=============================================================================')
	print(f'Class Total Score: {class_total}')
	print(f'Class Average Score: {class_average:.2f}')
	print('=============================================================================')

