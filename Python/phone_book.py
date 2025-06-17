def check_name_validity(contacts, name):

	if name in contacts:

		return "Name already exist"

	if name == '':

		return "this space cannot be empty"

	
	new_name = name.replace(' ', '', 1)


	if name.isspace():

		return "this space cannot be empty"

	elif new_name.isalpha():

		return name

	elif name.split('-'):

		return name
	
	else: return "Invalid name"




def add_contact(contacts, first_name, last_name, phone_number):
	

	if not phone_number.isdigit():

		return "Phone number must only be digit"
			
	contacts.append({'first_name': first_name, 'last_name': last_name, 'phone_number': phone_number})	
	return "Contact saved"



def view_contact(contacts):

	for index, contact in enumerate(contacts, 1):
	
		print(f"{index}. {contact['first_name']} {contact['last_name']} - {contact['phone_number']}")
 


def remove_contact(contacts, remove):

	if not remove.isdigit():

		return "Invalid input"

	remove = int(remove)

	for index, contact in enumerate(contacts, 1):

		if remove == index:

			contacts.pop(index - 1)

			return "removed successfully"

	return "Contact not found"



def edit_contact(contacts, edit, new_firstname, new_lastname, new_phonenumber):

	if not edit.isdigit():

		return "Invalid input"
	
	edit = int(edit)

	if not new_phonenumber.isdigit():

		return "Phone number must be only digit"


	for index, contact in enumerate(contacts, 1):

	
		if edit == index:

			contact['first_name'] = new_firstname

			contact['last_name'] = new_lastname

			contact['phone_number'] = new_phonenumber

			return "Contact updated"

	return "Contact not found"



def find_by_phone(contacts, phone_number):

	for contact in contacts:

		if contact['phone_number'] == phone_number:

			return contact

	return "Contact not found"




def find_by_first_name(contacts, first_name):
	

	for contact in contacts:

		if contact['first_name'] == first_name:

			return contact

	return "Contact not found"




def find_by_last_name(contacts, last_name):
	

	for contact in contacts:

		if contact['last_name'] == last_name:

			return contact

	return "Contact not found"

