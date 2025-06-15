from datetime import datetime

def check_name_validity(name):
	
	new_name = name.replace(' ', '', 1)

	if name == '':

		return "this space cannot be empty"

	elif name.isspace():

		return "this space cannot be empty"


	elif new_name.isalpha():

		return name

	elif name.split('-'):

		return name

	else: return "Invalid name"



def check_amount(amount):

	if not amount:

		return "this space cannot be empty"

	if amount.isspace():

		return "this space cannot be empty"

	another_amount = amount.replace('.', '', 1)

	if all(number.isdigit() for number in another_amount):
		
		amount = float(amount) 
			
		if amount == round(amount, 2): return True

		else: return "Invalid input"

	else: return "Invalid input"




def print_invoice(cart, cashier_name, customer_name, discount_rate):

	now = datetime.now()

	date = now.strftime("%d-%b-%Y %I:%M:%S %p")


	subtotal = 0

	for item in cart:

		subtotal += item['price'] * item['quantity']


	discount = subtotal * (discount_rate / 100)

	after_discount = subtotal - discount

	VAT = after_discount * 0.075

	final_total = after_discount + VAT


	print(f'''
	MID-DAY STORE
	MAIN BRANCH
	LOCATION: 545 Groove street, Lagos
	Tel: +2349027871650
	Date: {date}
	Cashier: {cashier_name}
	Customer's name: {customer_name}
    
	=================================================
		ITEM      QTY      Price      Total
	-------------------------------------------------
					''')

	for item in cart:

		total  = item['price'] * item['quantity']

		print(f"\t\t{item['name']}\t{item['quantity']}\t{item['price']:,.2f}\t{total:,.2f}")


	print(f'''
	-------------------------------------------------
			Sub Total:   {subtotal:,.2f}
			Discount:    {discount:,.2f}
			VAT @ 7.5%:  {VAT:,.2f}
	=================================================
			Bill Total:  {final_total:,.2f}
	=================================================
	THIS IS NOT A RECEIPT KINDLY PAY {final_total:,.2f}
	=================================================
					''')

	return final_total


	  
def print_receipt(cart, cashier_name, customer_name, discount_rate, payment):


	now = datetime.now()

	date = now.strftime("%d-%b-%Y %I:%M:%S %p")


	subtotal = 0

	for item in cart:

		subtotal += item['price'] * item['quantity']


	discount = subtotal * (discount_rate / 100)

	after_discount = subtotal - discount

	VAT = after_discount * 0.075

	final_total = after_discount + VAT

	balance = payment - final_total


	print(f'''
	MID-DAY STORE
	MAIN BRANCH
	LOCATION: 545 Groove street, Lagos
	Tel: +2349027871650
	Date: {date}
	Cashier: {cashier_name}
	Customer's name: {customer_name}
    
	=================================================
		ITEM      QTY      Price      Total(NGN)
	-------------------------------------------------
					''')

	for item in cart:

		total  = item['price'] * item['quantity']

		print(f"\t\t{item['name']}\t{item['quantity']}\t{item['price']:,.2f}\t{total:,.2f}")


	print(f'''
	-------------------------------------------------
			Sub Total:   {subtotal:,.2f}
			Discount:    {discount:,.2f}
			VAT @ 7.5%:  {VAT:,.2f}
			
	=================================================
			Bill Total:   {final_total:,.2f}
			Amount paid:  {payment:,.2f}
			Balance:      {balance:,.2f}
	=================================================
		THANK YOU FOR YOUR PATRONAGE
	=================================================
					''')

	return balance


