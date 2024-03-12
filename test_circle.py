"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
from unittest import TestCase


class TestCircle(TestCase):

    def test_add_area(self):
        circle = Circle(10)
        circle_2 = Circle(10)
        new_circle = circle.add_area(circle_2)
        self.assertAlmostEqual(new_circle.get_radius(),
                               14.142135623730951,
                               places=5)
        self.assertEqual(circle.get_radius(), 10)
        self.assertEqual(circle_2.get_radius(), 10)

    def test_add_area_edge(self):
        circle_2 = Circle(10)
        circle_3 = Circle(0)
        new_circle = circle_2.add_area(circle_3)
        self.assertEqual(new_circle.get_radius(), 10)
        new_circle = circle_3.add_area(circle_2)
        self.assertEqual(new_circle.get_radius(), 10)

    def test_circle_constructor(self):
        self.assertRaises(Exception, Circle, -1)


if __name__ == "__main__":
    unittest.main()
