# ------------------------------------------------------
#        Name:  Amy Tang
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------
#######################################################################
## Testing Area
test_mode = False
def myTests(): 
  print(isNoVowel("hello"))
  print(isNoVowel("welcome"))
  print(isNoVowel("today"))

  print(isIndex0Vowel("great"))
  print(isIndex0Vowel("computer"))
  print(isIndex0Vowel("science"))

  print(findIndexFirstVowel("orange"))
  print(findIndexFirstVowel("pear"))
  print(findIndexFirstVowel("watermelon"))

  print(pigLatinEncrypt("How are you."))
  print(pigLatinEncrypt("studying computer science right now"))
  print(pigLatinEncrypt("typing codes"))

  print(findIndexAsterisk("ow*hay are*~way ou.*yay"))
  print(findIndexAsterisk("udying*stay omputer*cay ience*scay ight*ray ow*nay"))
  print(findIndexAsterisk("ing*typay odes*cay"))

  print(pigLatinDecrypt("ow*hay are*~way ou.*yay"))
  print(pigLatinDecrypt("udying*stay omputer*cay ience*scay ight*ray ow*nay"))
  print(pigLatinDecrypt("ing*typay odes*cay"))
#######################################################################


def isNoVowel(word: str) -> bool:
  """This function takes a word as input and returns true is the word does not contain any vowels and false if the word contains
  :param word:(str) The input word that requires determining whether it has vowels
  :return :(bool) The result of whether it contains vowels. 
  >>> isNoVowel(Hi)
  False
  >>> isNoVowel(my)
  True
  >>> isNoVowel(how)
  False
  """
  if "a" in word or "e" in word or "i" in word or "o" in word or "u" in word: #Determines whether there's vowel in the word
    return False
  else:
    return True
  
def isIndex0Vowel(word: str) -> bool:
  """This function takes a word as input and returns true if the first character is vowel and else false.
  :param word:(str) The input word
  :return:(bool) The result of whethe first letter is vowel.
  >>> isIndex0Vowel(apple)
  True
  >>> isIndex0Vowel(juice)
  False
  >>> isIndex0Vowel(organize)
  True
  """
  if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u": #determines whether the first letter is vowel
    return True
  else:
    return False

def findIndexFirstVowel(word:str) -> int:
  """This function takes word as input and returns the index where the first vowel appears and returns false if there are no vowel.
  :param word:(str) This function takes the word as input
  :return :(int) This fucntion returns the first time for the first vowel to appear.
  >>> findIndexFirstVowel("apple")
  0
  >>> findIndexFirstVowel("my")
  -1
  >>> findIndexFirstVowel("visual")
  1
  """
  index = 0
  for i in word:
    if i in "aeiou":
      return index
    index += 1
  return -1
  
def pigLatinEncrypt(phrase: str) -> str:
  """The function converts original phrases to pig latin encrypt.
  :param phrase:(str) The input phrases
  :return :(str) The output converted string in pig latin encryption
  >>> pigLatinEncrypt("How are you")
  ow*hay are*~way ou.*yay
  >>> pigLatinEncrypt("studying computer science right now")
  udying*stay omputer*cay ience*scay ight*ray ow*nay
  >>> pigLatinEncrypt("typing codes")
  ing*typay odes*cay
  """
  encryptPhrase = []
  phrase:str = phrase.lower()
  separatePhrase = phrase.split( )
  for word in separatePhrase:
    if isIndex0Vowel(word) or isNoVowel(word):
      encrypted_word = word + "*~way"
    else:
      first_index = findIndexFirstVowel(word)
      encrypted_word = word[first_index:]+"*" + word[:first_index]+"ay"
    encryptPhrase.append(encrypted_word)
  return " ".join(encryptPhrase)

def findIndexAsterisk(word: str) -> int:
  """ This function returns the first time for asterisk to appear
  :param word:(str) The inputted word
  :return :(int) The index of the first asterisk to apepar in the word.
  >>> findIndexAsterisk("ow*hay")
  2
  >>> findIndexAsterisk("udying*stay")
  6
  >>> findIndexAsterisk("ing*typay")
  3
  """
  index = 0
  for j in word:
    if j in "*":
      return index
    index += 1
  return -1

def pigLatinDecrypt(phrase: str) -> str:
  """This function decipher the encrypted code
  :param phrase:(str) The inputed phrase
  :return:(str) the deciphered phrase
  >>> pigLatinDecrypt("ow*hay are*~way ou.*yay")
  how are you.    
  >>> pigLatinDecrypt("udying*stay omputer*cay ience*scay ight*ray ow*nay")
  studying computer science right now
  >>> pigLatinDecrypt("ing*typay odes*cay")
  typing codes
  """
  decrypted_words = []
  phrase:str = phrase.lower()
  splitPhrase = phrase.split( )
  for word in splitPhrase:
    asterisk_index = findIndexAsterisk(word)
    if asterisk_index == -1:
      decrypted_word = word
    elif "*~way" in word:
      decrypted_word = word[:-5]
    else:
      first = word[asterisk_index+1:-2]
      final = word[:asterisk_index]
      decrypted_word = first+final
    decrypted_words. append(decrypted_word)
  return " ".join(decrypted_words)


def main() -> None:
  phrase = input("Enter a phrase or 'quit' to end: ")
  if phrase != "quit":
    if "*" in phrase:
      print("ORIGINAL:",pigLatinDecrypt(phrase))
    else:
      print("PIG LATIN:",pigLatinEncrypt(phrase))
  elif phrase == "quit":
    print("Thank you for your business!")
  





#######################################################################
## DO NOT EDIT ANYTHING BELOW HERE 
if __name__ == "__main__":
  if (test_mode):
    myTests()
  else:   
    main()