import unittest
from circle import area as circle_area, perimeter as circle_perimeter

class TestCircle(unittest.TestCase):

    def test_area(self):
        res = circle_area(75)
        self.assertEqual(res, 17671.458676442588)

    def test_zero_area(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):

        res = circle_perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):

        res = circle_perimeter(75)
        self.assertEqual(res, 471.23889803846896)
