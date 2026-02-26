import unittest
from main import *

class MyTests(unittest.TestCase):

    def test_numGradeToSU(self):
        self.assertEqual(numGradeToSU(79), 'S')
        self.assertEqual(numGradeToSU(33), 'U')
        self.assertEqual(numGradeToSU(-1), 'Error')
        self.assertEqual(numGradeToSU(101), 'Error')

    def test_numGradeToLetter(self):
        self.assertEqual(numGradeToLetter(100), 'A')
        self.assertEqual(numGradeToLetter(89), 'B')
        self.assertEqual(numGradeToLetter(77), 'C')
        self.assertEqual(numGradeToLetter(60), 'D')
        self.assertEqual(numGradeToLetter(10), 'E')
        self.assertEqual(numGradeToLetter(101), 'Error')
        self.assertEqual(numGradeToLetter(-1), 'Error')

    def test_letterGradeToNumRange(self):
        self.assertEqual(letterGradeToNumRange('A'), "90 - 100")
        self.assertEqual(letterGradeToNumRange('B'), "80 - 89")
        self.assertEqual(letterGradeToNumRange('C'), "70 - 79")
        self.assertEqual(letterGradeToNumRange('D'), "60 - 69")
        self.assertEqual(letterGradeToNumRange('E'), "0 - 59")
        self.assertEqual(letterGradeToNumRange('Z'), 'Error')

    def test_gradeConverter(self):
        self.assertEqual(gradeConverter(100), 'A')
        self.assertEqual(gradeConverter(89), 'B')
        self.assertEqual(gradeConverter(77), 'C')
        self.assertEqual(gradeConverter(60), 'D')
        self.assertEqual(gradeConverter(10), 'E')
        self.assertEqual(gradeConverter(101), 'Error')
        self.assertEqual(gradeConverter(-1), 'Error')
        self.assertEqual(gradeConverter('A'), "90 - 100")
        self.assertEqual(gradeConverter('B'), "80 - 89")
        self.assertEqual(gradeConverter('C'), "70 - 79")
        self.assertEqual(gradeConverter('D'), "60 - 69")
        self.assertEqual(gradeConverter('E'), "0 - 59")
        self.assertEqual(gradeConverter('Z'), 'Error')

    def test_basicCalculator(self):
        self.assertEqual(basicCalculator('+', 5, 100), 105)
        self.assertEqual(basicCalculator('-', 5, 100), -95)
        self.assertEqual(basicCalculator('*', 5, 100), 500)
        self.assertEqual(basicCalculator('//', 100, 5), 20)
        self.assertEqual(basicCalculator('%', 101, 5), 1)
        self.assertEqual(basicCalculator('//', 5, 0), None)
        self.assertEqual(basicCalculator('%', 5, 0), None)
        self.assertEqual(basicCalculator('/', 5, 100), None)

    def test_highwayAnalysis(self):
        self.assertEqual(highwayAnalysis(69), 'Primary-NS')
        self.assertEqual(highwayAnalysis(4), 'Primary-EW')
        self.assertEqual(highwayAnalysis(608), 'Auxiliary-08')
        self.assertEqual(highwayAnalysis(699), 'Auxiliary-99')
        self.assertEqual(highwayAnalysis(400), 'Invalid')
        self.assertEqual(highwayAnalysis(0), 'Invalid')

    def test_stonesPoundsConverter(self):
        self.assertEqual(stonesPoundsConverter(10.5), 147.0)
        self.assertEqual(stonesPoundsConverter(-53), -1)
        self.assertEqual(stonesPoundsConverter(164.5), 11.75)
        
if __name__ == '__main__':
    unittest.main()

