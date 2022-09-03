import unittest
from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Mer'), 'Sea')
        self.assertNotEqual(french_to_english('Mer'), 'Pea')
        self.assertEqual(french_to_english(''),'')

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Sea'), 'Mer')
        self.assertNotEqual(english_to_french('Pea'), 'Mer')
        self.assertEqual(english_to_french(''), '')

unittest.main()