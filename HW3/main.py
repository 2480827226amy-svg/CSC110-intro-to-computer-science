# ------------------------------------------------------
#        Name: Amy Tang
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------
from typing import Union  # Do not delete this.

#######################################################################
## Part 1

def numGradeToSU(num_grade: int) -> str:
  """ This function inputs the score for student and determines whether the student passed the satisfied score. 
  :param num_grade:(int) The students' grade in integer
  :return:(str) The either satisfatory or unsatifactory grade for the student

  >>> numGradeToSU(79)
  S
  >>> numGradeToSU(23)
  U
  >>> numGradeToSU(89)
  S
  """

  if num_grade >= 70 and num_grade <= 100:
    return "S"
  elif num_grade >= 0 and num_grade <= 69:
    return "U"
  else:
    return "Error"


def numGradeToLetter(num_grade: int) -> str:
  """ This function inputs grade for students and returns the grade letter they got.
  :param num_grade:(int) The students' grade in integer
  :return:(str) The students' grade in letter

  >>> numGradeToLetter(89)
  B
  >>> numGradeToLetter(99)
  A
  >>> numGradeToLetter (33)
  E
  """

  if num_grade <= 100 and num_grade >=90:
    return("A")
  elif num_grade <= 89 and num_grade >=80:
    return("B")
  elif num_grade <= 79 and num_grade >= 70:
    return("C")
  elif num_grade <= 69 and num_grade >= 60:
    return("D")
  elif num_grade <= 59 and num_grade >= 0: 
    return("E")
  else:
    return("Error")


def letterGradeToNumRange(letter_grade: str) -> str:
  """ This function converts the grade students received in letters to number ranges
  :param letter_grade:(str) The grade student received in letters
  :return:(str) The grade in number ranges equivalent to the grade in letters

  >>> letterGradeToNumRange('C')
  "70 - 79"
  >>> letterGradeToNumRange("A")
  "90 - 100"
  >>> letterGradeToNumRange('D')
  "60 - 69"

  """
  if letter_grade == "A":
    return("90 - 100")
  elif letter_grade == "B":
    return("80 - 89")
  elif letter_grade == "C":
    return("70 - 79")
  elif letter_grade == "D":
    return("60 - 69")
  elif letter_grade == "E":
    return("0 - 59")
  elif letter_grade == "S":
    return("70 - 100")
  elif letter_grade == "U":
    return("0 - 69")
  else:
    return("Error")


def gradeConverter(grade: Union[int,str]) -> str: #Union means that the input can either be an integer or a string.
  """ The function returns the grade letter when inputing grade in numbers, and it returns grade in numbers when inputting grade in letters
  :param grade:(Union[int,str]) The grade in form of letter or number that need to be converted
  :return:(str) returns the grade in the other form

  >>> gradeConverter(89)
  B
  >>> gradeConverter("A")
  90 - 100
  >>> gradeConverter(28)
  E

  """
  if type(grade) == int:
    return(numGradeToLetter(grade))
  elif type(grade) == str:
    return(letterGradeToNumRange(grade))
  else:
    return("Error")


#######################################################################
## Part 2

def basicCalculator(sign: str, num_1: int, num_2: int) -> int:
  """ This function does basic calculation. 
  :param sign:(str) The signed used in the integer calculator, i.e., '+', '-', '*', '//', '%'
  :para num_1:(int) The first value that needs to be calculated
  :param num_2:(int) The second value that needs to be calculated
  :return:(int) The final calculated value

  >>> basicCalculator("+", 8, 6)
  14
  >>> basicCalculator("*", 9, 8)
  72
  >>> basicCalculator("//", 81, 9)
  9

  """
  if sign == "+":
    return num_1 + num_2
  if sign == "-":
    return num_1 - num_2
  if sign == "*":
    return num_1 * num_2
  if sign == "//" and num_2 != 0:
    return num_1 // num_2
  if sign == "%" and num_2 != 0:
    return num_1 % num_2
  else:
    return None

  
#######################################################################
## Part 3

def highwayAnalysis(num: int) -> str:
  """ This function determines the direction of primary highway and determines the number of auxiliary highways.
  :param num:(int) The number of high way.
  :return:(str) The name of high way with direction or number. 

  >>> highwayAnalysis(8)
  Primary-EW
  >>> highwayAnalysis(298)
  Auxiliary-98
  >>> highwayAnalysis(899)
  Auxiliary-99

  """
  if num >= 1 and num <= 99:
    if num % 2 == 0:
      return "Primary-EW"
    if num % 2 == 1:
      return "Primary-NS"
  elif num > 100 and num <= 999 and num != 200 and num!=300 and num!=400 and num!=500 and num!=600 and num!=700 and num!=800 and num!= 900:
    primary_highway= num%100
    if primary_highway >= 10:
      return "Auxiliary-"+ str(primary_highway)
    if primary_highway <10:
      return "Auxiliary-0"+str(primary_highway)

  else:
    return "Invalid"

#######################################################################
## Part 4

def stonesPoundsConverter(value: float) -> float:
  """ This function detects whether the input value is in stone or pound and converts one to another.
  :param value:(float) The input weight of a person
  :return:(float) The converted weight in the other unit of a person

  >>> stonesPoundsConverter(9)
  126
  >>> stonesPoundsConverter(50)
  3.57
  >>> stonesPoundsConverter(180)
  12.86

  """
  if value >= 0 and value < 50:
    return value * 14
  elif value >= 50:
    return value / 14
  else:
    return -1.0

#######################################################################
## Use the main function to test your functions.

def main():
  """This function is used to test the other functions,
      especially those that print to the Console.
  """    
  ## Add or change this code as you see fit.
  print("Function main test:")

  print(numGradeToSU(95))
  print(numGradeToSU(59))
  print(numGradeToSU(28))

  print(numGradeToLetter(99))
  print(numGradeToLetter(28))
  print(numGradeToLetter(68))
  print(numGradeToLetter(79))
  print(numGradeToLetter(180))

  print(letterGradeToNumRange("A"))
  print(letterGradeToNumRange("D"))
  print(letterGradeToNumRange("S"))
  print(letterGradeToNumRange("U"))

  print(gradeConverter(68))
  print(gradeConverter("A"))
  print(gradeConverter(89))
  print(gradeConverter("C"))

  print(basicCalculator("+", 1,2))
  print(basicCalculator("%", 8,5))
  print(basicCalculator("//", 100,20))

  print(highwayAnalysis(908))
  print(highwayAnalysis(900))
  print(highwayAnalysis(289))

  print(stonesPoundsConverter(100))
  print(stonesPoundsConverter(48))
  print(stonesPoundsConverter(208))


#######################################################################
## DO NOT EDIT ANYTHING BELOW HERE
if __name__ == "__main__":
    main()