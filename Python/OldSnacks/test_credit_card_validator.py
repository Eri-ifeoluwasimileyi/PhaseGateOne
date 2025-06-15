import credit_card_validator
import unittest


class TestCardNumber(unittest.TestCase):



	def test_card_exist(self):
		credit_card_validator.validate_card


	def test_visa_card_is_valid(self):
		card = "4132465789041896"
		actual = credit_card_validator.validate_card(card)
		expected = "VisaCard"
		self.assertEqual(actual, expected)
	
	
	def test_mastercard_is_valid(self):	
		card = "5132465789041896"
		actual = credit_card_validator.validate_card(card)
		expected = "MasterCard"
		self.assertEqual(actual, expected)


	def test_discover_is_valid(self):
		card = "6132465789041896"
		actual = credit_card_validator.validate_card(card)
		expected = "DiscoverCard"
		self.assertEqual(actual, expected)



	def test_American_express_is_valid(self):	
		card = "371246578904189"
		actual = credit_card_validator.validate_card(card)
		expected = "American Express"
		self.assertEqual(actual, expected)



	def test_length_is_invalid(self):	
		card = "4132465789"
		actual = credit_card_validator.validate_card(card)
		expected = "Invalid Card Length"
		self.assertEqual(actual, expected)


	def test_mastercard_is_valid_pass(self):	
		card = "5399831619690403"
		actual = credit_card_validator.check_validity(card)
		expected = "Valid"
		self.assertEqual(actual, expected)


	def test_mastercard_is_invalid(self):	
		card = "5399831619690404"
		actual = credit_card_validator.check_validity(card)
		expected = "Invalid"
		self.assertEqual(actual, expected)


	def test_visacard_is_valid(self):	
		card = "4388576018410707"
		actual = credit_card_validator.check_validity(card)
		expected = "Valid"
		self.assertEqual(actual, expected)


	def test_visacard_is_invalid(self):	
		card = "4388576018402626"
		actual = credit_card_validator.check_validity(card)
		expected = "Invalid"
		self.assertEqual(actual, expected)


	def test_americanexpress_is_invalid(self):	
		card = "3788576018402626"
		actual = credit_card_validator.check_validity(card)
		expected = "Invalid"
		self.assertEqual(actual, expected)


	def test_americanexpress_is_valid(self):	
		card = "3788576018402629"
		actual = credit_card_validator.check_validity(card)
		expected = "Valid"
		self.assertEqual(actual, expected)


	def test_discover_is_valid(self):
		card = "6388576018410702"
		actual = credit_card_validator.check_validity(card)
		expected = "Valid"
		self.assertEqual(actual, expected)


	def test_discover_is_invalid(self):
		card = "6388576018410703"
		actual = credit_card_validator.check_validity(card)
		expected = "Invalid"
		self.assertEqual(actual, expected)














