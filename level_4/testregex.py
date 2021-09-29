""" Exercise 2 Create a unit testing to extensively test all 
possibilities of the function created in the regex exercise above.
"""
import unittest

from lowregex import match_regex

class TestRegex(unittest.TestCase):

    def test_match(self):

        #Testing several lowercase strings with different lenght at 
        #the start and the end of the expression

        match_list = ["a_a", "a_b", "aa_bb", "aaa_bbbb", "af_uioo", "aert_fd"]
        for el in match_list:
            result = match_regex(el)
            message = f"Test with input: {el} failed"
            self.assertEqual(result, "Match found!", message)
        
    def test_not_a_match(self):

        #Testing several Uppercase and lowercase 
        #strings combinations with different lenght at 
        #the start and the end of the expression. 
        #Also tested cases with no or more than one underscore or 
        #underscores at the start or the end

        not_a_match_list = ["A_B","AB","abcd", "a_B", "A_b", "_ab", 
        "ab_", "a_b_", "_a_b", "a_b_c", "_a_b_c", "_a_b_c_", 
        "a_b_c_", "aaBa_c", "a_bcdE", "a__b", "aa__bb","ab",
        "cbcde"
        ]
        for el in not_a_match_list:
                result = match_regex(el)
                message = f"Test with input: {el} failed"
                self.assertEqual(result, "Not a Match", message)

if __name__ == '__main__':
    unittest.main()