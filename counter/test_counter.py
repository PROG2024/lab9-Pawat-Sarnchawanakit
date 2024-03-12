"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class CounterTest(unittest.TestCase):

    def test(self):
        self.assertEqual(Counter().count, 0, "Initial counter not set to 0.")
        self.assertEqual(Counter().increment(), 1,
                         "Increment should return new value.")
        Counter().increment()
        self.assertEqual(Counter().count, 2, "Count should now be 2.")


if __name__ == "__main__":
    unittest.main()
