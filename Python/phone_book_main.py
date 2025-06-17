import phone_book
from phone_book import *



contacts = []

while True:

	print('''
		
1. Add contact

2. Remove contact

3. Find contact by phone number

4. Find contact by first Name

5. Find contact by last Name

6. Edit contact

7. Exit
	''')

	user_choice = str(input('Enter your choice: '))
	print()

	if user_choice == '1':
	
		while True:
		
			first_name = str(input('Enter first name: '))
		
			new_name = check_name_validity(contacts, first_name)
			
			if new_name != first_name:
		
				print(new_name)
				continue

			last_name = str(input('Enter last name: '))	

			new_name = check_name_validity(contacts, last_name)
		
			if new_name != last_name:

				print(new_name)
				continue
				
			phone_number = str(input('Enter number: '))
			
			if not phone_number.isdigit():

				print("Phone number must be only digit")
				continue

			print(add_contact(contacts, first_name, last_name, phone_number))
			break


	elif user_choice == '2':

		while True:

			view_contact(contacts)

			print()

			remove = str(input('Enter a number to remove: '))
			
			if not remove.isdigit():

				print("Phone number must be only digit")
				continue

			print(remove_contact(contacts, remove))

			break



	elif user_choice == '3':

		while True:

			number = str(input('Enter phone number to find: '))
			
			if not number.isdigit():

				print("Phone number must be only digit")
				continue

			if find_by_phone(contacts, number):

				print("Contact found: ", find_by_phone(contacts, number))

			else:
				print("Contact not found")
				continue

			break



	elif user_choice == '4':

		while True:

			first_name = str(input('Enter first name: '))
		
			new_name = check_name_validity(contacts, first_name)
			
			if new_name != first_name:
		
				print(new_name)
				continue
	
			contact = find_by_first_name(contacts, first_name)

			if isinstance(contact, dict):

				print(f"Contact found: {contact['first_name']} {contact['last_name']} - {contact['phone_number']}")
				print()

			else:
				print("Contact not found")
				continue
			break




	elif user_choice == '5':

		while True:

			last_name = str(input('Enter last name: '))
		
			new_name = check_name_validity(contacts, last_name)
			
			if new_name != last_name:
		
				print(new_name)
				continue
	
			contact = find_by_last_name(contacts, last_name)

			if isinstance(contact, dict):

				print(f"Contact found: {contact['first_name']} {contact['last_name']} - {contact['phone_number']}")
				print()

			else:
				print("Contact not found")
				continue
			break






	elif user_choice == '6':
		
		while True:

			view_contact(contacts)

			print()		

			edit = input("Enter number to edit: ")

			if not edit.isdigit():

				print("Invalid input. Please enter a number.")
				continue


			new_firstname = str(input('Enter new first name: '))

			new_fname = check_name_validity(contacts, new_firstname)
			
			if new_fname != new_firstname:
		
				print(new_fname)
				continue

			new_lastname = str(input('Enter new last name: '))

			new_lname = check_name_validity(contacts, new_lastname)
			
			if new_lname != new_lastname:
		
				print(new_lname)
				continue

			new_phonenumber = str(input('Enter new phone number: '))

			if not new_phonenumber.isdigit():

				print("Phone number must be only digit")
				continue

			print(edit_contact(contacts, edit, new_firstname, new_lastname, new_phonenumber))
			print()
			break



	elif user_choice == '7':

		print("Exiting phonebook")
		break

	else:
		print("Invalid input, try again")

		