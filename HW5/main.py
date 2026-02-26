# ------------------------------------------------------
#        Name: Amy Tang
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------
import random   # Do not edit/remove this line.
#######################################################################
## Testing Area
test_mode:bool = False
def myTests():
  print(changeCase("Hello","U"))
  print(changeCase("Good morning","L"))
  print(changeCase("Good night","T"))

  print(doubleVowel("Hello from Amy!"))
  print(doubleVowel("Hello from Ada!"))
  print(doubleVowel("Hello from Amelie!"))

  print(abbreviate("How are you doing?"))
  print(abbreviate("What are you doing?"))
  print(abbreviate("Why are you writing homework?"))

  print(capEachWord("My favorite animal is fish."))
  print(capEachWord("Ada's favorite animal is cat."))
  print(capEachWord("Amelie's favorite animal is dolphin."))

  print(reverse("I'm at Smith College."))
  print(reverse("Ada is at Wellesly College."))
  print(reverse("Amelie is at Mount Holyoke College."))

  print(moreSmith("Do you like fish?"))
  print(moreSmith("Sorry, I don't like fish."))
  print(moreSmith("I want to each McDonalds for dinner."))

  print(prettify("Nice to meet you."))
  print(prettify("See you next time."))
  print(prettify("Hope not to see you anymore."))


## End of Testing Area
#######################################################################
#######################################################################
## Write your here...

def randomLetter() -> str:
  """ This function randomly selects a letter from U, L and T to convert the string to upper case, lower case or title case.
  :return :(str) The output is a randomly selected letter, either U or L or T.

  >>> randomLetter()
  "U"
  >>> randomLetter()
  "L"
  >>> randomLetter()
  "T"
  """
  return random.choice(['U', 'L', 'T'])

def changeCase(phrase:str, choice:str) -> str:
  """This function accepts user's input phrases and a randomly-generated choice of conversion and output the phrases in upper case or lower case of title case. 
  :param phrase:(str) The phrase user input. 
  :param choice:(str) The randomly selected choice from randomLetter.
  :return :(str) The converted phrase in either upper case, lower case, or title case.

  >>> changeCase("Hello","U")
  "HELLO"
  >>> changeCase("Amy","L")
  "amy"
  >>> changeCase("Good afternoon", "T")
  "Good Afternoon"
  """
  if choice == "U":
    return phrase.upper()
  if choice == "L":
    return phrase.lower()
  if choice == "T":
    return phrase.title()
  else:
    return phrase

def doubleVowel(phrase:str) -> str:
  """This function accepts user's input phrases and a randomly-generated choice of conversion and output the phrases in upper case or lower case of title case. 
  :param phrase:(str) The phrase user input. 
  :return :(str) The converted string with double vowel. 

  >>> doubleVowel("I love Smith College.")
  "I loovee Smiith Coolleegee."
  >>> doubleVowel("Do you love MA?")
  "Doo yoouu loovee MA?"
  >>> doubleVowel("Good afternoon")
  "Gooood Afteernoooon"
  """
  phrase1 = ""
  for char in phrase:
    if char in "aeiou":
      phrase1+=char*2
    else:
      phrase1+=char
  return phrase1

def abbreviate(phrase:str) -> str:
  """Thie function abbreviate the strong to first 5 characters and last 5 characters. 
  :param phrase:(str) The user's input phrase.
  :return :(str) The converted string with abbreviation. 

  >>> abbreviate("I ordered delivery for dinner today.")
  "I ord...oday."
  >>> abbreviate("I ate at Ziskind for lunch.")
  "I ate...unch."
  >>> abbreviate("I didn't have breakfeast.")
  "I did...east."
  """
  a:int=len(phrase)
  if a>10:
    phrase2=phrase[:5]+"..."+phrase[-5:]
    return phrase2
  else:
    return phrase

def capEachWord(phrase:str) -> str:
  """This function caplitalize the first letter in each word in the phrase. 
  :param phrase:(str) The user's input phrase.
  :return :(str) The converted string with first letter in each word capitalized.

  >>> capEachWord("Good morning")
  "Good Morning"
  >>> capEachWord("I get up at 9 today.")
  "I Get Up At 9 Today."
  >>> capEachWord("I go to first class at seelye.")
  "I Go To First Class At Seelye."
  """
  capWords=[]
  capitalize = True
  for char in phrase:
    if capitalize:
      capWords.append(char.upper())
      capitalize = False
    else:
      capWords.append(char)
    if char ==" ":
      capitalize = True
  return "".join(capWords)

def reverse(phrase:str) -> str:
  """This function reverse the order of the string inputed.
  :param phrase:(str) The user's input phrase.
  :return :(str) The converted string with reversed order of letters

  >>> reverse("How's your day going?")
  "?gniog yad ruoy s'woH"
  >>> reverse("I've been in US for 6 months.")
  ".shtnom 6 rof SU ta neeb ev'I"
  >>> reverse("The weather is good today.")
  ".yadot doog si rehtaew ehT"
  """
  return phrase[::-1]

def moreSmith(phrase:str) -> str:
  """This function converts the string to returning the word Smith according to the times of a appears in the string.
  :param phrase:(str) The user's input phrase.
  :return :(str) The converted string with smith being repeated for times that a appears in the original string.

  >>> moreSmith("apple")
  "Smith"
  >>> moreSmith("How are you doing today?")
  "SmithSmith"
  >>> moreSmith("My friend is a girl")
  "College"
  """
  num = 0
  for char in phrase:
   if char == "a":
      num+=1
  if num >0:
    return "Smith" * num
  else:
    return "College"
  
def prettify(phrase:str) -> str:
  """This function formats the phrases nicely centered. 
  :param phrase:(str) The string user inputed. 
  :return:(str) The converted string that's centered. 

  >>> prettify("How's your day going?")
  "|           How's your day going?"           |"
  >>> prettify("I've been at US for 6 months.")
  "|              I've been at US for 6 months.               |"
  >>> prettify("The weather is good today.")
  "|             The weather is good today."              |"
  """
  length = len(phrase)*2
  return "|"+ phrase.center(length)+"|"


def printFunnyPhrases(user_phrase: str) -> None:
  """This function prints list of converted user input phrases.
  :param user_phrase:(str) The inputed string from user.

  >>> printFunnyPhrases("The weather is good today.")
  "0. The weather is good today."
  "1. THE WEATHER IS GOOD TODAY."
  "2. Thee weeaatheer iis gooood toodaay."
  "3. The w...day."
  "4. The Weather Is Good Today."
  "5. .yadot doog si rehtaew ehT“
  "6. SmithSmith”
  "7. |             The weather is good today.              |"   
  >>> printFunnyPhrases("I've been at US for 6 months.")
  “0. I've been at US for 6 months.”
  “1. I've been at US for 6 months.”
  “2. I'vee beeeen aat US foor 6 moonths.”
  "3. I've ...nths."
  "4. I've Been At Us For 6 Months."
  "5. .shtnom 6 rof SU ta neeb ev'I"
  "6. Smith"
  "7. |              I've been at US for 6 months.               |"
  >>> printFunnyPhrases("How's your day going?")
  "0. How's your day going?"
  "1. how's your day going?"
  "2. Hoow's yoouur daay gooiing?"
  "3. How's...ing?"
  "4. How's Your Day Going?"
  "5. ?gniog yad ruoy s'woH"
  "6. Smith"
  "7. |           How's your day going?"           |"
  """
  print("0.", user_phrase)
  print("1.", changeCase(user_phrase, randomLetter()))
  print("2.", doubleVowel(user_phrase))
  print("3.", abbreviate(user_phrase))
  print("4.", capEachWord(user_phrase))
  print("5.", reverse(user_phrase))
  print("6.", moreSmith(user_phrase))
  print("7.", prettify(user_phrase))





#######################################################################
## DO NOT EDIT ANYTHING BELOW HERE

def randomLetter() -> str:
  """ Returns a random character for use in calling the changeCase function from printFunnyPhrases.
  :return : (str) return 'T' for Title Case, 'U' for Upper Case, 'L' for Lower Case, or other letters.
  >>> randomLetter()
  'L'
  >>> randomLetter()
  'T'
  >>> randomLetter()
  'U'
  """
  return random.choice('ULTRA')

def main() -> None:
  """ This main function either calls the myTests function or calls the printFunnyPhrases function
      after getting user input.
  """
  if (test_mode):
    myTests()
  else:
    # Ask for initial input
    phrase:str = input("Enter a sentence (STOP to end):")
    while (phrase != "STOP"):
      printFunnyPhrases(phrase)
      phrase = input("Phrase (STOP to end):")

if __name__ == "__main__":
    main()