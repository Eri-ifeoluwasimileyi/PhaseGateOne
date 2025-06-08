import checkout

import unittest
#from unittest import TestCase


class TestCheckout(unittest.TestCase):


	def test_check_name_validity_valid(self):

		actual = checkout.check_name_validity("Eri ife")
		expected = "Eri ife"
		self.assertEqual(actual, expected)

	def test_check_name_validity_empty(self):
		actual = checkout.check_name_validity("")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)

		actual = checkout.check_name_validity("   ")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)

	def test_check_name_validity_invalid(self):
		actual = checkout.check_name_validity("Eriife1324")
		expected = "Invalid name"
		self.assertEqual(actual, expected)

		actual = checkout.check_name_validity("Eri@ife")
		expected = "Invalid name"
		self.assertEqual(actual, expected)

	def test_check_amount_valid(self):
		actual = checkout.check_amount("100")
		expected = True
		self.assertEqual(actual, expected)

		actual = checkout.check_amount("50.75")
		expected = True
		self.assertEqual(actual, expected)

	def test_check_amount_invalid(self):
		actual = checkout.check_amount("")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)

		actual = checkout.check_amount("   ")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)

	def test_check_amount_is_invalid(self):
		actual = checkout.check_amount("abc")
		expected = "Invalid input"
		self.assertEqual(actual, expected)

		actual = checkout.check_amount("123.45.67")
		expected = "Invalid input"
		self.assertEqual(actual, expected)


	def test_print_invoice_is_valid(self):
		customer_name = "ada"
		
		cart = [
			{'name': 'egg', 'quantity': 3, 'price': 100, 'total': 300}
		]
		cashier_name = "ola"
		discount = 10
		cashier = (cashier_name, discount)

		actual = checkout.print_invoice(cart, customer_name, cashier, discount)
		expected = 290.25
		self.assertEqual(actual, expected)



	def test_print_receipt(self):
		customer_name = "ada"

		cart = [
			{'name': 'egg', 'quantity': 3, 'price': 100, 'total': 300}
		]
		cashier_name = "ola"
		discount = 10
		cashier = (cashier_name, discount)
		payment = 300
		total = checkout.print_invoice(cart, customer_name, cashier, discount)
		
		actual = checkout.print_receipt(cart, customer_name, cashier, discount, payment)
		expected = 300 - 290.25
		self.assertEqual(actual, expected)
