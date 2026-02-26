import unittest
from main import *
import io
import sys 

class MyTests(unittest.TestCase):
    def test_sphereVolume(self) -> None:
        self.assertEqual(round(sphereVolume(10.21)), round(4456.00))
        self.assertEqual(round(sphereVolume(1.5)), round(14.129999999999997))
        self.assertEqual(round(sphereVolume(5)), round(523.3333333333334))

    def test_funnyReturn(self) -> None:
        self.assertEqual(funnyReturn("Hello"), "*** Hello ***")
        self.assertEqual(funnyReturn("This is a cool phrase!"), "*** This is a cool phrase! ***")
        self.assertEqual(funnyReturn(""), "***  ***")
       
    def test_workStudyCalc(self) -> None:
        self.assertEqual(workStudyCalc(10), 145.0)
        self.assertEqual(workStudyCalc(17), 246.5)
        self.assertEqual(workStudyCalc(0), 0)

    def test_percentComplete(self) -> None:
        self.assertEqual(percentComplete(87, 23), 73.5632183908046)
        self.assertEqual(percentComplete(66, 0), 100.0)
        self.assertEqual(percentComplete(100, 5), 95.0)

    def test_getChange(self) -> None:
        self.assertEqual(getChange(14.56), 56)
        self.assertEqual(getChange(1.00), 0)
        self.assertEqual(getChange(76.05), 5)

    def test_add(self) -> None:
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 5), 6)
        self.assertEqual(add(-4, -5), -9)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(5, 4), 1)
        self.assertEqual(subtract(-4, 4), -8)
        self.assertEqual(subtract(0, 4), -4) 

    def test_number_of_balloons(self) -> None:
        self.assertEqual(number_of_balloons(10), 0)
        self.assertEqual(number_of_balloons(30), 200)
        self.assertEqual(number_of_balloons(100), 900)
    
    def test_inchesToMeters(self) -> None:
        self.assertEqual(inchesToMeters(100), 2.54000508001016)
        self.assertEqual(inchesToMeters(39.37), 1)
        self.assertEqual(inchesToMeters(1), 0.025400050800101603)

    def test_calculateMetricHeight(self) -> None:
        self.assertEqual(calculateMetricHeight(5,6), 1.6764033528067057) # type: ignore
        self.assertEqual(calculateMetricHeight(6,2), 1.8796037592075185) # type: ignore
        self.assertEqual(calculateMetricHeight(2,0), 0.6096012192024385) # type: ignore

    def test_funnyPrint(self) -> None:
        tests = [("Hello", "*** Hello ***"),
                 ("This is a cool phrase!", "*** This is a cool phrase! ***"),
                 ("", "***  ***")]

        for message, expected in tests:
            #This is what is used to get the print output to compare it to a check 
            # Capture the output from squares 
            captured_output = io.StringIO() #Apparently this is like an import thing 
            sys.stdout = captured_output  # capture output
            funnyPrint(message)  # Run now the squares function so the output will be captured HERE
            sys.stdout = sys.__stdout__  # clears it
            # obtains the  output and strip extra spaces or newlines. Important for cleaning it
            actual_output = captured_output.getvalue().strip() 
            # Compare actual output and expected 
            self.assertEqual(actual_output, expected)
        
    def test_mystery(self) -> None:
        tests = [(6,3,"6 // 3 = 2 remainder 0"),
                 (3,8,"3 // 8 = 0 remainder 3"),
                 (25,8,"25 // 8 = 3 remainder 1")]

        for param_1, param_2, expected in tests:
            #This is what is used to get the print output to compare it to a check 
            # Capture the output from squares 
            captured_output = io.StringIO() #Apparently this is like an import thing 
            sys.stdout = captured_output  # capture output
            mystery(param_1, param_2)  # Run now the squares function so the output will be captured HERE
            sys.stdout = sys.__stdout__  # clears it
            # obtains the  output and strip extra spaces or newlines. Important for cleaning it
            actual_output = captured_output.getvalue().strip() 
            # Compare actual output and expected 
            self.assertEqual(actual_output, expected)
                
if __name__ == '__main__':
    unittest.main()

