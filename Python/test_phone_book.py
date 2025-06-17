import unittest
import phone_book
from phone_book import *

class TestPhoneBook(unittest.TestCase):



	def test_check_name_validity_empty(self):
		contacts = []
		actual = check_name_validity(contacts, '')
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


		actual = check_name_validity(contacts, '   ')
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


		actual = check_name_validity(contacts, 'Eri-ife')
		expected = 'Eri-ife'
		self.assertEqual(actual, expected)

		

	def test_check_name_validity_valid(self):
		contacts = []
		actual = check_name_validity(contacts, 'Ola')
		expected = "Ola"
		self.assertEqual(actual, expected)



	def test_add_contact(self):
		contacts = []
		actual = add_contact(contacts, 'Ola', 'Eri', '0123456789')
		expected = "Contact saved"
		self.assertEqual(actual, expected)



	def test_add_contact_invalid(self):
		contacts = []
		actual = add_contact(contacts, 'Tom', 'Red', 'phone123')
		expected = "Phone number must only be digit"
		self.assertEqual(actual, expected)



	def test_remove_contact(self):
		contacts = [{'first_name': 'Ola', 'last_name': 'Eri', 'phone_number': '1234567890'}, {'first_name': 'Tom', 'last_name': 'Red', 'phone_number': '2345678901'}]
		actual = remove_contact(contacts, '2')
		expected = "removed successfully"
		self.assertEqual(actual, expected)



	def test_remove_contact_not_valid(self):
		contacts = []
		actual = remove_contact(contacts, 'abc')
		expected = "Invalid input"
		self.assertEqual(actual, expected)



	def test_remove_contact_invalid(self):
		contacts = []
		actual = remove_contact(contacts, '10')
		expected = "Contact not found"
		self.assertEqual(actual, expected)



	def test_edit_contact(self):
		contacts = [{'first_name': 'Ola', 'last_name': 'Eri', 'phone_number': '1234567890'}]
		actual = edit_contact(contacts, '1', 'Lizzy', 'Eri', '1112223333')
		expected = "Contact updated"
		self.assertEqual(actual, expected)



	def test_edit_contact_invalid(self):
		contacts = [{'first_name': 'Ola', 'last_name': 'Eri', 'phone_number': '1234567890'}]
		actual = edit_contact(contacts, '10', 'A', 'B', '123')
		expected = "Contact not found"
		self.assertEqual(actual, expected)



	def test_edit_contact_invalid_2(self):
		contacts = []
		actual = edit_contact(contacts, 'abc', 'A', 'B', '123')
		expected = "Invalid input"
		self.assertEqual(actual, expected)



	def test_edit_contact_invalid_3(self):
		contacts = []
		actual = edit_contact(contacts, '1', 'A', 'B', '12ab')
		expected = "Phone number must be only digit"
		self.assertEqual(actual, expected)



	def test_find_by_phone(self):
		contacts = [{'first_name': 'Lizzy', 'last_name': 'Eri', 'phone_number': '1112223333'}, {'first_name': 'Ola', 'last_name': 'Smoke', 'phone_number': '2345678901'}]
		actual = find_by_phone(contacts, '1112223333')
		expected = {'first_name': 'Lizzy', 'last_name': 'Eri', 'phone_number': '1112223333'}
		self.assertEqual(actual, expected)




	def test_find_by_phone_invalid(self):
		contacts = []
		actual = find_by_phone(contacts, '0000000000')
		expected = "Contact not found"
		self.assertEqual(actual, expected)



	def test_find_by_first_name(self):
		contacts = [{'first_name': 'Alia', 'last_name': 'Fat', 'phone_number': '3456789012'}, {'first_name': 'Bob', 'last_name': 'Brown', 'phone_number': '9876543210'}]
		actual = find_by_first_name(contacts, 'Alia')
		expected = {'first_name': 'Alia', 'last_name': 'Fat', 'phone_number': '3456789012'}
		self.assertEqual(actual, expected)
	
	

	def test_find_by_first_name_invalid(self):
		contacts = []
		actual = find_by_first_name(contacts, 'Alice')
		expected = "Contact not found"
		self.assertEqual(actual, expected)


		
	def test_find_by_last_name(self):
		contacts = [{'first_name': 'Alia', 'last_name': 'Fat', 'phone_number': '3456789012'}, {'first_name': 'Bob', 'last_name': 'Brown', 'phone_number': '9876543210'}]
		actual = find_by_last_name(contacts, 'Fat')
		expected = {'first_name': 'Alia', 'last_name': 'Fat', 'phone_number': '3456789012'}
		self.assertEqual(actual, expected)



	def test_find_by_last_name_invalid(self):
		contacts = []
		actual = find_by_last_name(contacts, 'Alice')
		expected = "Contact not found"
		self.assertEqual(actual, expected)
