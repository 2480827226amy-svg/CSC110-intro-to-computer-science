# ------------------------------------------------------
#        Name: Amy Tang
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------
import random   # Do not edit/remove this line.

def isUp(direction: str) -> bool:
  """ The function receives the request from the student of whether they want the list of number in ascending or descending order and returns the choice into true or false.
  :param direction:(str) The entered order of numbers student want to get. 
  :return:(bool) Converted true or false of the students' choices.

  >>> isUp("up")
  True
  >>> isUp("down")
  False

  """

  if direction == "up":
    return True
  elif direction == "down":
    return False


def isContinueGame(choice: str) -> bool:   
  """ The function determines whether the game should continue based on user input.
  :param choice:(str) The choices of whether to continue to play the game from the user. 
  :return:(bool) True if game continues and false if game stops. 

  >>> isContinueGame("Y")
  Sorry, I'm too tired to play again ...
  >>> isUp("Nono")
  Thanks for playing!
  >>> isUp("y")
  Ok, here we go ...
  
  """
  if choice == "Y" or choice == "y":
    x:float = random.randint(1,2)
    if x==1:
      print("Sorry, I'm too tired to play again...") 
      return False
    else: 
      print("Ok, here we go....")
      return True
  else: 
    print("Thanks for playing!")
    return False


def sillyNumberGameWithLoops(min_num: int, max_num: int, is_Up: bool) -> str:
  """ This function provides the multiple of 2, 3, 5 within the range from min number and max number given by user and arrange in either ascending or descending order based on users' selections. 
  :param min_num:(int) the minimum number user entered for generating multiple
  :param max_num:(int) the maximum number user entered for generating multiple
  :param is_Up:(bool) True if the user choose an ascending order and false if the user choose an descending order. 
  :return:(str) The multiple of each number in the given range

  >>> sillyNumberGameWithLoops(3, 5, False)
  5       Five Golden Rings!
  4       4_
  3       0-3-
  >>> sillyNumberGameWithLoops(2,6,True)
  2       2_
  3       0-3-
  4       2_4_
  5       Five Golden Rings!
  6       2_4_6_
  >>> sillyNumberGameWithLoops(41,43,False)
  43      #
  42      0-3-6-9-12-15-18-21-24-27-30-33-36-39-42-
  41      #
  """

  return_string = ""
  if is_Up == True:
    for num in range (min_num, max_num+1,1):
      if num % 5 == 0:
        line = str(num) + "\tFive Golden Rings!"
      elif num % 3 == 0:
        multiple_of_three = ""
        for i in range (0,num+1,3):
          multiple_of_three += str(i)+ "-"
        line = str(num) + "\t" + multiple_of_three
      elif num % 2 == 0:
        multiple_of_two = ""
        if min_num%2 !=0:
          min_num = min_num +1
        for j in range (min_num, num+1,2):
          multiple_of_two += str(j)+"_"
          line = str(num) + "\t" + multiple_of_two
      else:
        line = str(num)+"\t"+"#"
      return_string += line + "\n"
    return return_string
  elif is_Up == False:
    for num in range (max_num, min_num - 1, -1):
      if num % 5 == 0:
        line = str(num) + "\tFive Golden Rings!"
      elif num % 3 == 0:
        multiple_of_three = ""
        for i in range (0,num+1,3):
          multiple_of_three += str(i)+ "-"
        line = str(num) + "\t" + multiple_of_three
      elif num % 2 == 0:
        multiple_of_two = ""
        if min_num%2 !=0:
          min_num = min_num + 1
        for j in range (min_num, num+1,2):
          multiple_of_two += str(j)+"_"
          line = str(num) + "\t" + multiple_of_two
      else:
        line = str(num)+"\t"+"#"
      return_string += line + "\n"
    return return_string

#######################################################################
## Testing Area
test_mode = True
def myTests() -> None:

  print(isUp("up"))
  print(isUp("down"))

  print(isContinueGame("Y"))
  print(isContinueGame("y"))
  print(isContinueGame("nono"))
  
  print(sillyNumberGameWithLoops(5,20,True))
  print(sillyNumberGameWithLoops(40,55,False))
  print(sillyNumberGameWithLoops(2,15,True))

  x:str = "hi"
  y:str = "hello"
  print(x+y)
  print(x,y)

  x = 1 
  print(float(x))





## End of Testing Area
#######################################################################
## DO NOT EDIT ANYTHING BELOW HERE
def main() -> None:
  if (test_mode):
    myTests()
  else:
    playing = True
    while (playing):   
      min_num = int(input("Min:"))
      max_num = int(input("Max:"))
      direction = input("Direction (up/down):")
      sillyNumberGameWithLoops(min_num, max_num, isUp(direction))
      choice = input("Would you like to play again (Y or y for Yes)?")
      playing = isContinueGame(choice)
      
if __name__ == "__main__":
    main()