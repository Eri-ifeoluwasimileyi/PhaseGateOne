for number in range(1, 11):

	if number % 4 == 0:

		multiple = 1

		for num in range(0, 5):

			multiple = multiple * number

			print(multiple)
