import unittest
from main import *

class MyTests(unittest.TestCase):

    def test_isNoVowel(self):
        self.assertEqual(isNoVowel("rhythm"), True)
        self.assertEqual(isNoVowel("welcome"), False)
    
    def test_isIndex0Vowel(self):
        self.assertEqual(isIndex0Vowel("rhythm"), False)
        self.assertEqual(isIndex0Vowel("apple"), True)
    
    def test_findIndexFirstVowel(self):
        self.assertEqual(findIndexFirstVowel("computer"), 1)
        self.assertEqual(findIndexFirstVowel("happy"), 1)
        self.assertEqual(findIndexFirstVowel("transform"), 2)
        self.assertEqual(findIndexFirstVowel("rhythm"), -1)
    
    def test_pigLatinEncrypt(self):
        self.assertEqual(pigLatinEncrypt("rhythm computer").strip(), "rhythm*~way omputer*cay")    
        self.assertEqual(pigLatinEncrypt("welcome my orange").strip(), "elcome*way my*~way orange*~way") 

    def test_findIndexAsterisk(self):
        self.assertEqual(findIndexAsterisk("hell*o"), 4)
        self.assertEqual(findIndexAsterisk("computer*"), 8)
        self.assertEqual(findIndexAsterisk("a*ppple"), 1)
        self.assertEqual(findIndexAsterisk("appple"), -1)

    def test_pigLatinDecrypt(self):
        self.assertEqual(pigLatinDecrypt("my*~way rhythm*~way").strip(), "my rhythm")
        self.assertEqual(pigLatinDecrypt("elcome*way o*tay omputer*cay ience*scay").strip(), "welcome to computer science") 


if __name__ == '__main__':  
    unittest.main()
 