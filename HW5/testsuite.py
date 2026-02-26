import unittest
from main import *

class MyTests(unittest.TestCase):
    #https://wisdomquotes.com/short-quotes/

    def test_changeCase(self):
        self.assertEqual(changeCase("UP down All arOund", 'U'), "UP DOWN ALL AROUND")
        self.assertEqual(changeCase("UP down All arOund", 'L'), "up down all around")
        self.assertEqual(changeCase("UP down All arOund", 'T'), "Up Down All Around")
        self.assertEqual(changeCase("UP down All arOund", 'Z'), "UP down All arOund")

    def test_doubleVowel(self):
        self.assertEqual(doubleVowel("It's a beautiful day to save lives."), "It's aa beeaauutiifuul daay too saavee liivees.")
        self.assertEqual(doubleVowel("Don’t tell people your plans. Show them your results."), "Doon’t teell peeooplee yoouur plaans. Shoow theem yoouur reesuults.")
        self.assertEqual(doubleVowel("When nothing goes right, go left."), "Wheen noothiing gooees riight, goo leeft.")
        self.assertEqual(doubleVowel("I can & I will."), "I caan & I wiill.")
        self.assertEqual(doubleVowel("Believe"), "Beeliieevee")

    def test_abbreviate(self):
        self.assertEqual(abbreviate("It's a beautiful day to save lives."), "It's ...ives.")
        self.assertEqual(abbreviate("Don’t tell people your plans. Show them your results."), "Don’t...ults.")
        self.assertEqual(abbreviate("When nothing goes right, go left."), "When ...left.")
        self.assertEqual(abbreviate("I can & I will."), "I can...will.")
        self.assertEqual(abbreviate("Believe"), "Believe")

    def test_capEachWord(self):
        self.assertEqual(capEachWord("It's a beautiful day to save lives."), "It's A Beautiful Day To Save Lives.")
        self.assertEqual(capEachWord("Don’t tell people your plans. Show them your results."), "Don’t Tell People Your Plans. Show Them Your Results.")
        self.assertEqual(capEachWord("When nothing goes right, go left."), "When Nothing Goes Right, Go Left.")
        self.assertEqual(capEachWord("i can & i will."), "I Can & I Will.")
        self.assertEqual(capEachWord("Believe"), "Believe")

    def test_reverse(self):
        self.assertEqual(reverse("It's a beautiful day to save lives."), ".sevil evas ot yad lufituaeb a s'tI")
        self.assertEqual(reverse("Don’t tell people your plans. Show them your results."), ".stluser ruoy meht wohS .snalp ruoy elpoep llet t’noD")
        self.assertEqual(reverse("When nothing goes right, go left."), ".tfel og ,thgir seog gnihton nehW")
        self.assertEqual(reverse("I can & I will."), ".lliw I & nac I")
        self.assertEqual(reverse("Believe"), "eveileB")

    def test_moreSmith(self):
        self.assertEqual(moreSmith("It's a beautiful day to save lives."), "SmithSmithSmithSmith")
        self.assertEqual(moreSmith("Don’t tell people your plans. Show them your results."), "Smith")
        self.assertEqual(moreSmith("When nothing goes right, go left."), "College")
        self.assertEqual(moreSmith("I can & I will."), "Smith")
        self.assertEqual(moreSmith("Believe"), "College")

    def test_prettify(self):
        self.assertEqual(prettify("It's a beautiful day to save lives."), "|                 It's a beautiful day to save lives.                  |")
        self.assertEqual(prettify("Don’t tell people your plans. Show them your results."), "|                          Don’t tell people your plans. Show them your results.                           |")
        self.assertEqual(prettify("When nothing goes right, go left."), "|                When nothing goes right, go left.                 |")
        self.assertEqual(prettify("I can & I will."), "|       I can & I will.        |")
        self.assertEqual(prettify("Believe"), "|   Believe    |")
        
if __name__ == '__main__':
    unittest.main()

