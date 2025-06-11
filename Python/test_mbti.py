import mbti

import unittest
#from unittest import TestCase


class TestMbti(unittest.TestCase):

	
	def test_function1_exist(self):
		mbti.extrovert_introvert("ola")


	def test_function2_is_valid(self):
		actual = mbti.extrovert_introvert("ola")
		expected = "I"
		self.assertEqual(actual, expected)


	def test_function3_is_valid(self):
		actual = mbti.extrovert_introvert("ola")
		expected = "E"
		self.assertEqual(actual, expected)
	
	

	def test_function4_is_valid(self):
		actual = mbti.sensing_intuitive("ola")
		expected = "S"
		self.assertEqual(actual, expected)



	def test_function5_is_valid(self):
		actual = mbti.sensing_intuitive("ola")
		expected = "N"
		self.assertEqual(actual, expected)

	

	def test_function6_is_valid(self):
		actual = mbti.thinking_feeling("ola")
		expected = "T"
		self.assertEqual(actual, expected)



	def test_function7_is_valid(self):
		actual = mbti.thinking_feeling("ola")
		expected = "F"
		self.assertEqual(actual, expected)



	def test_function8_is_valid(self):
		actual = mbti.judging_percerptive("ola")
		expected = "J"
		self.assertEqual(actual, expected)



	def test_function9_is_valid(self):
		actual = mbti.judging_percerptive("ola")
		expected = "P"
		self.assertEqual(actual, expected)




