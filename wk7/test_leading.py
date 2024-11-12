import unittest
from leading import leading_substrings

class TestLeadingSubstrings(unittest.TestCase):
    
    def test_basic_case(self):
        self.assertEqual(leading_substrings('bear'), ['b', 'be', 'bea', 'bear'])
    
    def test_single_character(self):
        self.assertEqual(leading_substrings('a'), ['a'])
    
    def test_empty_string(self):
        self.assertEqual(leading_substrings(''), [])
    
    def test_repeated_characters(self):
        self.assertEqual(leading_substrings('aaa'), ['a', 'aa', 'aaa'])
    
    def test_special_characters(self):
        self.assertEqual(leading_substrings('@bc1'), ['@', '@b', '@bc', '@bc1'])
    
    def test_long_string(self):
        long_string = "abcdefghij"
        expected = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']
        self.assertEqual(leading_substrings(long_string), expected)

if __name__ == "__main__":
    unittest.main()
