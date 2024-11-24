import unittest
import coverage
from ..palindrome.transform import Transform


class MyTestCase(unittest.TestCase):

    def test_reverse_number(self):
        transformer = Transform()
        self.assertEqual(transformer.reverse_number(12), 21)
        self.assertEqual(transformer.reverse_number(11), 11)
        self.assertEqual(transformer.reverse_number(51), 15)
        self.assertEqual(transformer.reverse_number(607), 706)
        self.assertEqual(transformer.reverse_number(196), 691)

    def test_is_palindrome(self):
        transformer = Transform()
        self.assertTrue(transformer.is_palindrome(11))
        self.assertFalse(transformer.is_palindrome(28))
        self.assertFalse(transformer.is_palindrome(51))
        self.assertFalse(transformer.is_palindrome(607))
        self.assertFalse(transformer.is_palindrome(196))

    def test_palindrome(self):
        transformer = Transform()
        self.assertEqual(transformer.palindrome(28), (121, 2))
        self.assertEqual(transformer.palindrome(11), (11, 0))
        self.assertEqual(transformer.palindrome(51), (66, 1))
        self.assertEqual(transformer.palindrome(607), (4444, 2))
        self.assertEqual(transformer.palindrome(196), (-1, 17))


if __name__ == "__main__":
    unittest.main()
