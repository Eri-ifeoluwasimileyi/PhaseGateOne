def validate_card(card_number):

	if len(card_number) <= 13 or len(card_number) > 16:

		return  "Invalid Card Length"


	elif card_number[0] == '4':

		return "VisaCard"

	elif card_number[0] == '5':

		return "MasterCard"

	elif card_number[0] == '6':

		return "DiscoverCard"
	
	elif card_number[0] == '3' and card_number[1] == '7':

		return "American Express"
		
	else: 
		return "Invalid Card";



def check_validity(card_number):

	sum_odd = 0

	sum_even = 0

	totol_sum = 0

	size = len(card_number)

	for index in range(size -1, -1, -1):

		digits = int(card_number[index])

		if((size - index) % 2 == 0):
		
			digits *= 2

			if digits > 9:
		
				digits = (digits // 10) + (digits % 10)

			sum_even += digits

		else:	
			sum_odd += digits


	total_sum = sum_even + sum_odd
	
	if(total_sum % 10 == 0):
		
		return "Valid"

	else:
		return "Invalid"




user_input = str(input("Hello, Kindly Enter Card details to verify: ")
print()

print("****************************************")

print("***Credit Card Type: " + validate_card(user_input))

print("***Credit Card Number: " + user_input)

print("***Credit Card Digit Length: " ,  len(user_input))

print("***Credit Card Validity Status: " + check_validity(user_input))

print("****************************************")
		
