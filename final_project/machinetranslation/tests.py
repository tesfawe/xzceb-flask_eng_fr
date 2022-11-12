import unittest
from translator import english_to_french, french_to_english
class TestE2F(unittest.TestCase):

    """English to French tests"""

    def test_english_to_french(self):
        self.assertNotEqual(english_to_french("None"), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Thank you'), 'Je vous remercie')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')  

class TestF2E(unittest.TestCase):
    """English to French tests"""
    def test_french_to_english(self):
        self.assertNotEqual(french_to_english("None"), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
        self.assertEqual(french_to_english('Je vous remercie'), 'Thank you.')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')  
 

if __name__ == '__main__':
    unittest.main()      