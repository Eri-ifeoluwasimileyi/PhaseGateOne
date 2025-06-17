for number in range(1, 11):

	if number % 4 == 0:

		multiple = 1
		
		sum = 0

		for num in range(0, 5):

			multiple = multiple * number
			
			sum = sum + multiple

			print(sum)
