# ------------------------------------------------------
#        Name: Amy Tang
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------

#######################################################################
## TODO: Write the code for the following functions and finish the incomplete doc strings.

def sphereVolume(radius: float) -> float:
  """ Calculates the volume of a sphere using the formula (4/3) × pi × r^3.
  :param radius: (float) The radius of the sphere
  :return : (float) The resulting volume of the sphere
  
  >>> sphereVolume(10.21)
  4456.004399386668       #Note: Don't worry if the last digit or two is off.
  """
  pi = 3.14  #Do not change this value.
  return (4/3) * pi * (radius**3)


def funnyReturn(message: str) -> str:
  """ Adds three stars '*' on each side of a users message.
  :param message: (str) The users message
  :return : (str) The users message with "***" on each side.

  >>> funnyReturn('hello')
  '*** hello ***'
  """
 
  return '*** '+message+' ***'



def funnyPrint(message: str) -> None:
  """ Prints to the console a message with three stars '*' on each side.
  :param message: (str) The message to be printed

  >>> funnyPrint('hello')
  *** hello ***
  """
  print("***",message,"***")


def workStudyCalc(num_hour: int) -> float:
  """ Calculates the total money a student will get in a week, given the Smith rate of $14.50 per hour.
  :param num_hour: (int) number of hours the student wants to work
  :return : (float) the money they receive

  >>> workStudyCalc(10)
  145.0
  """
  return (14.5 * num_hour)


def percentComplete(total: int, left: int) -> float:
  """ Calculates the percentage of sites and inspector has completed, given the total number of site she has to complete and how many she has left.
  :param total:(int) the total number of sites she has to complete
  :param left:(int) the amount of sites left
  :return:(float) the percentage amount she has done

  >>> percentComplete(87, 23)
  73.5632183908046
  """
  return ((total-left)/total)*100



def getChange(amount: float) -> int:
    """ Returns the amount of cents given an amount of money.
    :param amount: (float) the total amount of money given
    :return: (int) the amount of cents
    
    >>> getChange(14.56)
    56

    """
    return round((amount % 1) * 100)


#######################################################################
## TODO: Add doc strings to the following functions.

def add(var_a: int, var_b: int) -> int:
  """ Calculates the sum of two integer variables.
  :param var_a: (int) value of variable a
  :param var_b: (int) value of variable b
  :return : (int) the total
 
  >>> add(12,13)
  25
  """
  return var_a + var_b


def subtract(var_a: int, var_b: int) -> int:
  """" Calculates the difference between two variables
  :param var_a:(int) value of variable a
  :param var_b:(int) value of variale b
  :return:(int) the difference between two variables
  >>> subtract (13,12)
  1
  """
  return var_a - var_b


def number_of_balloons(dollars: int) -> int:
  # Note: You can buy packs of 100 for $10.99
  """" calculate how many balloons one can buy with given amount of money. 
  :param dollars:(int) the money one has
  :return:(int) the number of ballons one can buy
  >>> number_of_ballons (1099)
  10000
  """
  packs = int(dollars / 10.99)
  return packs * 100


def mystery(param_1:int, param_2:int) -> None:
  # Note: You have to figure out what the param and return types should be.
  """" Writes an equation of two numbers
  :param param_1:(int) the first number 
  :param param_2:(int) the second number
  >>> mystery (8,4)
  """
  firstNumber = param_1
  secondNumber = param_2
  print(firstNumber, "//", secondNumber, "=", firstNumber//secondNumber, "remainder", firstNumber%secondNumber)


def inchesToMeters(inches: float) -> float:
  """" Converting inches to meters
  :param inches:(float) the inches that need to be convert to meters
  :return:(float) the number of meters converted from inches
  >>> inchesToMeters(10,8)
  0.27432
  """
  return inches / 39.37


#######################################################################
## TODO: Add your new functions here.
def calculateMetricHeight(height_in_feet:int, height_in_inches: int) -> float:
  """" Converting someone's height in feet and inches to meters
  :param height_in_feet:(int) the height in feet
  :param height_in_iches:(int) the height in inches 
  :return:(float) the converted height in meters
  >>> inchesToMeters(10,8)
  3.224
  """
  inches = (height_in_feet * 12) + height_in_inches
  return inches / 39.37

def mySelfCare(major:str,house:str)-> None:
  """ Conducts a self-introduction given major and house.
  :param major:(str) the major Amy studies
  :param house:(str) the house Amy lives in
  >>> mySelfCare(math,ziskind)
  """
  print("Hi! My name is Amy (she/her). I'm a first year, planning to major in",major,"I live in", house, "I'm from Suzhou, China. This semester I'll engage in self care by sleep early and having breakfast every day.")

def myWiseChoice(dollar:float) -> float:
  """This function converts dollar to RMB
  :param dollar:(float) the number of dollars one have
  :return:(float) the number of RMB converting from dollars
  >>> myWiseChoice (20)
  146.2
  """
  RMB = dollar*7.31
  return RMB

#######################################################################
## TODO: Use the main function to run and test your functions.

def main() -> None:
  """This function is used to test the other functions,
      especially those that print to the Console.
  """    
  ## Add or change this code as you see fit.
  print("Function main test:")
  print(print.__doc__)
  ##print(sphereVolume.__doc__)

  ##Examples and test cases

  print(sphereVolume(2.5))
  print(sphereVolume(10.22))
  print(sphereVolume(8.18))

  print(funnyReturn("welcome"))
  print(funnyReturn("Amy"))
  print(funnyReturn("do_CS_homework"))

  funnyPrint("Python")
  funnyPrint("is really")
  funnyPrint("complex")

  print(workStudyCalc(20))
  print(workStudyCalc(289))
  print(workStudyCalc(102))

  print(percentComplete(25,16))
  print(percentComplete(95,87))
  print(percentComplete(287,169))

  print(getChange(10.98))
  print(getChange(8.9873))
  print(getChange(6.5552))

  print(add(1,2))
  print(add(4,9))
  print(add(1099,2877))

  print(subtract(10,8))
  print(subtract(2,19))
  print(subtract(5,199))

  print(number_of_balloons(2000))
  print(number_of_balloons(2090))
  print(number_of_balloons(1200))

  print(mystery(3,8))
  print(mystery(18,9))
  print(mystery(23,8))

  print(inchesToMeters(10.89))
  print(inchesToMeters(39.87))
  print(inchesToMeters(100.90))

  print(calculateMetricHeight(80,29))
  print(calculateMetricHeight(20,18))
  print(calculateMetricHeight(90,2))

  print(mySelfCare("Math","Ziskind"))
  print(mySelfCare("Psychology","Cutter"))
  print(mySelfCare("Computer Science","Ford"))

  print(myWiseChoice(197.86))
  print(myWiseChoice(99.20))
  print(myWiseChoice(10000.2))



#######################################################################
## DO NOT EDIT ANYTHING BELOW HERE
if __name__ == "__main__":
    main()