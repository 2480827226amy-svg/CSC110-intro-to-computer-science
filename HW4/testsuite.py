import unittest
from main import *

class MyTests(unittest.TestCase):
    def test_isUp(self):
        self.assertEqual(isUp('up'), True)
        self.assertEqual(isUp('down'), False)
        self.assertEqual(isUp('bob'), False)

    def test_isContinueGame_NoInput(self):
        self.assertEqual(isContinueGame('n'), False)
        self.assertEqual(isContinueGame('N'), False)
        self.assertEqual(isContinueGame('badinput'), False)
        
    def test_isContinueGame_YesInputWithRandom(self):
        random.seed(124)
        self.assertEqual(isContinueGame('Y'), True)
        self.assertEqual(isContinueGame('y'), False)
        self.assertEqual(isContinueGame('Y'), False)
        self.assertEqual(isContinueGame('y'), False)
        self.assertEqual(isContinueGame('Y'), True)
        self.assertEqual(isContinueGame('y'), True)

    # def sillyNumberGameWithLoops(min_num: int, max_num: int, is_Up: bool) -> str:
    def test_sillyNumberGameWithLoops_Five(self):
        self.assertEqual(sillyNumberGameWithLoops(5,5, False), "5\tFive Golden Rings!\n")
        self.assertEqual(sillyNumberGameWithLoops(5,5, True), "5\tFive Golden Rings!\n")
    
    def test_sillyNumberGameWithLoops_UpSmall(self):    
        self.assertEqual(sillyNumberGameWithLoops(1,2,True), "1\t#\n2\t2_\n")
    
    def test_sillyNumberGameWithLoops_UpLarge(self):    
        self.assertEqual(sillyNumberGameWithLoops(2,15,True), "2\t2_\n3\t0-3-\n4\t2_4_\n5\tFive Golden Rings!\n6\t0-3-6-\n7\t#\n8\t2_4_6_8_\n9\t0-3-6-9-\n10\tFive Golden Rings!\n11\t#\n12\t0-3-6-9-12-\n13\t#\n14\t2_4_6_8_10_12_14_\n15\tFive Golden Rings!\n")

    def test_sillyNumberGameWithLoops_DownSmall(self):
        self.assertEqual(sillyNumberGameWithLoops(1,2,False), "2\t2_\n1\t#\n")
    
    def test_sillyNumberGameWithLoops_DownLarge(self):
        self.assertEqual(sillyNumberGameWithLoops(9,15,False), "15\tFive Golden Rings!\n14\t10_12_14_\n13\t#\n12\t0-3-6-9-12-\n11\t#\n10\tFive Golden Rings!\n9\t0-3-6-9-\n")





if __name__ == '__main__':
    unittest.main()

