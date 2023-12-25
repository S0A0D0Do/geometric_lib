import unittest
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter

class TestSquare(unittest.TestCase):
	def test_zero_area(self):
		self.assertEqual(rectangle_area(0), 0)

	def test_small_area(self):
		self.assertEqual(rectangle_area(0.345,0.45), 0.15525)

	def test_big_area(self):
		self.assertEqual(rectangle_area(123,890), 1009470)

	def test_normal_area(self):
		self.assertEqual(srectangle_area(2,5), 10)

	" Рассмоттрим периметр при этих же условиях"

	def test_zero_perimeter(self):
		self.assertEqual(rectangle_perimeter(0), 0)

	def test_small_perimeter(self):
		self.assertEqual(rectangle_perimeter(0.345,0.45),1.59)

	def test_big_perimeter(self):
		self.assertEqual(rectangle_perimeter(123,890), 2026)

	def test_normal_area(self):
		self.assertEqual(rectangle_perimeter(3,25), 40)
