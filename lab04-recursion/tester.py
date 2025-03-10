## Lab04- TESTER ##

# Call using python -m unittest tester.py #

import unittest
from io import StringIO
import sys
from Recursion import printNoDoubleLetterWords, toWords

class TestRecursion(unittest.TestCase):

    def test_printNoDoubleLetterWords(self):
        output = StringIO()
        sys.stdout = output
        printNoDoubleLetterWords(2, ['a', 'b', 'c'])
        sys.stdout = sys.__stdout__
        expected_output = "ab\nac\nba\nbc\nca\ncb\n"
        self.assertEqual(output.getvalue(), expected_output)

        output = StringIO()
        sys.stdout = output
        printNoDoubleLetterWords(3, ['x', 'y'])
        sys.stdout = sys.__stdout__
        expected_output = "xyx\nxyy\nyxy\nyxx\n"
        self.assertEqual(output.getvalue(), expected_output)

        output = StringIO()
        sys.stdout = output
        printNoDoubleLetterWords(1, ['a', 'b'])
        sys.stdout = sys.__stdout__
        expected_output = "a\nb\n"
        self.assertEqual(output.getvalue(), expected_output)

        output = StringIO()
        sys.stdout = output
        printNoDoubleLetterWords(0, ['a', 'b'])
        sys.stdout = sys.__stdout__
        expected_output = "\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_toWords(self):
        self.assertEqual(toWords(0), "zero")
        self.assertEqual(toWords(340), "three hundred and forty")
        self.assertEqual(toWords(1000430), "one million four hundred and thirty")
        self.assertEqual(toWords(-2101000442), "negative two billion one hundred and one million four hundred and forty-two")
        self.assertEqual(toWords(15), "fifteen")
        self.assertEqual(toWords(105), "one hundred and five")
        self.assertEqual(toWords(1000), "one thousand")
        self.assertEqual(toWords(1000000), "one million")
        self.assertEqual(toWords(1234567890), "one billion two hundred and thirty-four million five hundred and sixty-seven thousand eight hundred and ninety")
        self.assertEqual(toWords(-999999999), "negative nine hundred and ninety-nine million nine hundred and ninety-nine thousand nine hundred and ninety-nine")

if __name__ == "__main__":
    unittest.main()