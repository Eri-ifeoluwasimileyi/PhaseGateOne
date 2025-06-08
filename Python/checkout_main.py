import checkout
from checkout import *

cart = []


customer_name = str(input("What is the customer name: "))

check = True

while True:

	while check:

		name = str(input("What did the user buy?: "))

		new_name = check_name_validity(name)
	
		if new_name != name:
		
			print(new_name)
			continue


		quantity = str(input("How many pieces?: "))
		
		if quantity.isdigit():
			quantity = int(quantity)
			if quantity <= 0:

				print("Invalid input")
				continue
		else:
			print("Quantity must be a whole number.")
			continue

		price = str(input("How much per unit?: "))

		new_price = check_amount(price)

		if new_price == True:

			price = float(price)
		
		else:
			print(new_price)
			continue


		cart.append({'name': name, 'price': price, 'quantity': quantity})

		while check:

			user_choice = str(input("Do you want to add another item? (yes/no): "))
		
			user_choice = user_choice.lower()
	
			if(user_choice == 'yes'):

				break
			elif(user_choice == 'no'):
				check = False
				break
	
	if len(cart) > 0:


		cashier_name = str(input("Enter cashier name?: "))

		correct_name = check_name_validity(cashier_name)
	
		if correct_name != cashier_name:
		
			print(correct_name)
			continue

		discount = input("Enter discount: ")

		if check_amount(discount) == True:

			discount = float(discount)
		else:
			print("Invalid discount")
			continue
			discount = 0.0

		print_invoice(cart, cashier_name, customer_name, discount)
	

		cash = input("How much did the customer give to you?: ")

		if check_amount(cash) == True:

			cash = float(cash)
		else:
			print("Invalid amount")
			
			cash = 0.0

		print_receipt(cart, cashier_name, customer_name, discount, cash)
		break


	else:
		print("No items in cart. Invoice cannot be raised.")


