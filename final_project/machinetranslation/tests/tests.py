import unittest
from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
         self.assertEqual(english_to_french(''),0)
         self.assertEqual(english_to_french(' '),0)

    def test2(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(''),0)
        self.assertEqual(french_to_english(' '),0)

    def test2(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()