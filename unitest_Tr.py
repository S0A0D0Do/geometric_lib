import unittest
from square import area as square_area, perimeter as square_perimeter

class TestSquare(unittest.TestCase):
	def test_zero_area(self):
		self.assertEqual(square_area(0), 0)

	def test_small_area(self):
		self.assertEqual(square_area(0.045), 0.002025)

	def test_big_area(self):
		self.assertEqual(square_area(543), 294849)

	def test_negative_area(self):
		with self.assertRaises(ValueError):
			square_area(-1)

	def test_normal_area(self):
		self.assertEqual(square__perimeter(10), 100)

	" Рассмоттрим периметр при этих же условиях"

	def test_zero_perimeter(self):
		self.assertEqual(square_perimeter(0), 0)

	def test_small_perimeter(self):
		self.assertEqual(square_perimeter(1), 4)

	def test_big_perimeter(self):
		self.assertEqual(square_perimeter(543), 2172)

	def test_negative_perimeter(self):
		with self.assertRaises(ValueError):
			square_perimeter(-1)

	def test_normal_perimeter(self):
		self.assertEqual(square_area(10), 40)
