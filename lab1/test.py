import unittest
from lab1.main import Add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(Add(""), 0)

    def test_single_number(self):
        self.assertEqual(Add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(Add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(Add("1,2,3,4,5"), 15)

    def test_general_invalid_values_raises_error(self):
        with self.assertRaises(ValueError):
            Add("1,,2")

    def test_newline_as_separator(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_invalid_separator_sequence_raises_error(self):
        with self.assertRaises(ValueError):
            Add("1,\n")
            
if __name__ == '__main__':
    unittest.main()