# ------------------------------------------------------
#        Name:  Amy Tang
#       Peers: NA
#  References: NA
# ------------------------------------------------------
import distributor
from random import randint

#######################################################################
## Testing Area
test_mode:bool = False
def myTests():
  printHeaderOrder() 
  pass

#######################################################################

def getRandomCitation(library: list) -> str:
  """ This function selects a book at random from the library and returns the citation information for that book.
  :param library:(list) The book dictionary.
  :return :(str) The citation of a random selected book.
  >>> library = [{"title":"Opening Spaces: An Anthology of Contemporary African Women's Writing","authors":"Yvonne Vera (Editor)\, Yvonne Vera","publisher":"Heinemann","pages":"186","pubdate":"Sep-99"}]
  >>> getRandomCitation(library)
  Yvonne Vera (Editor), Yvonne Vera.Opening Spaces: An Anthology of Contemporary African Women's Writing.Heinemann.186.Sep-99.
  """
  if len(library) == 0: # Checks if there are items in the list
    return "There is nothing in the library."
  else:
    i = randint(0,len(library)-1) # Generates random book in the library
    book = library[i]
    return getCitationInformation(book["title"],book["authors"],book["publisher"],book["pages"],book["pubdate"])


def printLibrary(library: list) -> None:
  """ This function prints out the citation information for each book in the library in order. 
      For each book, an index (starting at 1) should first be printed prior to the citation information.    
  :param library:(list) The book dictionary.
  >>> library = [{"title":"Opening Spaces: An Anthology of Contemporary African Women's Writing","authors":"Yvonne Vera (Editor)\, Yvonne Vera","publisher":"Heinemann","pages":"186","pubdate":"Sep-99"},{"title":"Voices in Our Blood: America's Best on the Civil Rights Movement", "authors":"Jon Meacham", "publisher":"Random House Publishing Group", "pages":"576", "pubdate":"Jan-03"}]
  >>> printLibrary(library)
  1. Yvonne Vera (Editor), Yvonne Vera.Opening Spaces: An Anthology of Contemporary African Women's Writing.Heinemann.186.Sep-99.
  2. Jon Meacham. Voices in Our Blood: America's Best on the Civil Rights Movement. Random House Publishing Group, 576, Jan-03.  
  """
  num = 1
  for book in library:
    print (str(num) + "." + getCitationInformation(book["title"],book["authors"],book["publisher"],book["pages"],book["pubdate"]))
    num += 1 


def removeBook(library: list, index: int) -> None:
  """ This function removes the entry at the index specified from the library list. 
      The indexes 1..n appear when the user selects the PRINT operation.
  :param library:(list) The book dictionary.
  >>> library = [{"title":"Opening Spaces: An Anthology of Contemporary African Women's Writing","authors":"Yvonne Vera (Editor)\, Yvonne Vera","publisher":"Heinemann","pages":"186","pubdate":"Sep-99"},{"title":"Voices in Our Blood: America's Best on the Civil Rights Movement", "authors":"Jon Meacham","publisher":"Random House Publishing Group", "pages":"576", "pubdate":"Jan-03"}]
  >>> removeBook(library, 1)
  [{"title":"Voices in Our Blood: America's Best on the Civil Rights Movement", "authors":"Jon Meacham","publisher":"Random House Publishing Group", "pages":"576", "pubdate":"Jan-03"}]
  """
  if index >= 1 and index <= len(library): #make sure the book that user want to remove is in the range of the library
    library.pop(index-1)
  else:
    print("The index you input is invalid.") #informs the use if their input is invalid

def createBookDictionary(title: str, firstAuthor:str, authors:str, publisher:str, pubdate:str, pages:str) -> dict:
  """ This function takes in the information for title, firstAuthor, authors, publisher, pages, and pubdate, 
      all as strings. The function creates a dictionary for the book with the following keys: 
      'title', 'firstAuthor', 'authors', 'publisher', 'pubdate', 'pages'. 
      Returns a dictionary holding the information for one book.
  :param title:(str) The title of the book that needs to be stored
  :param firstAuthor:(str) The first author of the book that needs to be stored
  :param authors:(str) The authors of the book that needs to be stored
  :param publisher:(str) The publisher of the book that needs to be stored
  :param pubdate:(str) The pubdate of the book that needs to be stored
  :param pages:(str) The pages of the book that needs to be stored
  >>> createBookDictionary("Opening Spaces: An Anthology of Contemporary African Women's Writing", "Yvonee Vera","Yvonne Vera (Editor)\, Yvonne Ver", "Heinemann", "186", "Sep-99")
  {"title":"Opening Spaces: An Anthology of Contemporary African Women's Writing", "firstAuthor":"Yvonee Vera","authors":"Yvonne Vera (Editor)\, Yvonne Ver", "publisher":"Heinemann", "pages":"186", "pubdate":"Sep-99")}
  """
  return {"title": title,"firstAuthor": firstAuthor,"authors": authors,"publisher": publisher,"pubdate": pubdate,"pages": pages}

def addBook(library: list, book: dict) -> None:
  """ This function adds a book dictionary to the library list.
  :param library:(list) The book dictionary
  :param book:(dict) The book that needs to be added to the library list
  >>> library = [{"title":"Opening Spaces: An Anthology of Contemporary African Women's Writing","authors":"Yvonne Vera (Editor)\, Yvonne Vera","publisher":"Heinemann","pages":"186","pubdate":"Sep-99"}]
  >>> book = {"title":"Voices in Our Blood: America's Best on the Civil Rights Movement", "authors":"Jon Meacham", "publisher":"Random House Publishing Group", "pages":"576", "pubdate":"Jan-03"}
  >>> addBook(library, book)
  [{"title":"Opening Spaces: An Anthology of Contemporary African Women's Writing","authors":"Yvonne Vera (Editor)\, Yvonne Vera","publisher":"Heinemann","pages":"186","pubdate":"Sep-99"},{"title":"Voices in Our Blood: America's Best on the Civil Rights Movement", "authors":"Jon Meacham", "publisher":"Random House Publishing Group", "pages":"576", "pubdate":"Jan-03"}]
  """
  library.append(book)

def setupLibrary(numBooks: int) -> list:
  """ This function sets up the book library to store all your books. numBooks is the number of books 
      the user wants to have initialized in the library, in the range of 0..100. 
      Returns the newly created library. If numBooks is zero, this function should return an empty list.
  :param numBooks:(int) the number of books the user want to include in the library
  :return :(list) the list of books information

  >>> setupLibrary(2)
  [{"title":"Opening Spaces: An Anthology of Contemporary African Women's Writing","firstAuthor":"Yvonee Vera", "authors":"Yvonne Vera (Editor)\, Yvonne Vera","publisher":"Heinemann","pages":"186","pubdate":"Sep-99"},{"title":"Voices in Our Blood: America's Best on the Civil Rights Movement", "firstAuthor":"Jon Meacham", "authors":"Jon Meacham", "publisher":"Random House Publishing Group", "pages":"576", "pubdate":"Jan-03"}]
  """
  if numBooks == 0: 
    return []
  else: 
    booklist = distributor.getRandomBookList(numBooks) #get the random book list from another file
    library = []
    for book in booklist:
      bookdict = createBookDictionary(book[0],book[1],book[2],book[5],book[6],book[7]) # only extract information that will be needed to generate the citation
      library.append(bookdict)
    return library

def getTitles(library: list) -> list:
  """ This function returns a list of the book titles in the library, sorted in alphabetical order.
  
  >>> my_library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel Myerson', 'authors': 'Joel Myerson, Joel Myerson', 
  'publisher': 'Oxford University Press, USA', 'pubdate': 'Dec-00', 'pages': '752'}, 
  {'title': 'Bombshells: War Stories and Poems by Women on the Homefront', 'firstAuthor': 'Missy Martin', 'authors': 'Missy Martin (Editor), 
  Jesse Loren', 'publisher': 'OmniArts, LLC', 'pubdate': 'Jan-07', 'pages': '163'}, {'title': 'Imagination And Spirit', 
  'firstAuthor': 'J. Brent Bill', 'authors': 'J. Brent Bill (Editor), Shari Pickett Veach (Designed by), C. Michael Curtis (Foreword by), 
  J. Brent Bill', 'publisher': 'Friends United Press', 'pubdate': 'Feb-06', 'pages': '292'}]
  >>> print(getTitles(my_library))
  ['Bombshells: War Stories and Poems by Women on the Homefront', 'Imagination And Spirit', 'Transcendentalism: A Reader']
  """
  if len(library) == 0:
    return []
  else:
    booklist =[]
    for book in library:
      booklist.append(book["title"]) 
    booklist.sort() 
    return booklist
    

def saveToFile(library: list,  saveAll: bool, file_name: str) -> None:
  """ This function writes library data to a file based on the given file name.
      It either writes the titles in the library when saveAll is False or
      the formatted output when saveAll is True.
  
  >>> my_library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel Myerson', 'authors': 'Joel Myerson, Joel Myerson', 
  'publisher': 'Oxford University Press, USA', 'pubdate': 'Dec-00', 'pages': '752'}]
  >>> saveToFile(my_library, False, test.txt)
  "Transcendentalism: A Reader;" is written to test.txt
  """
  file = open(file_name, "w")
  if saveAll == False:
    text = getTitles(library)
    for title in text:
      file.write(title + ";")
  else:
    for book in library:
      citation = getCitationInformation(book['title'], book['authors'], book['publisher'], book['pages'], book['pubdate'])
      file.write(citation + ";")
  file.close()

#######################################################################
## DO NOT EDIT ANYTHING BELOW HERE 
def getCitationInformation(title:str, authors:str, publisher:str, pages:str, date:str) -> str:
  """ This function returns the stylized citation for the book information passed as parameters.
  :param title: (str) full title of the book
  :param authors: (str) full list of authors full names
  :param publisher: (str) name of publishers
  :param pages: (str) number of pages
  :param date: (str) date of publication
  :return : (str) the formatted string of the citation
  
  >>> getCitationInformation("Voices in Our Blood: America's Best on the Civil Rights Movement", "Jon Meacham", 
  "Random House Publishing Group", "576", "Jan-03")
  Jon Meacham. Voices in Our Blood: America's Best on the Civil Rights Movement. Random House Publishing Group, 576, Jan-03.  
  """
  return authors + ". " + title + ". " + publisher + ", " + pages + ", " + date + "." 

def printHeaderOrder() -> None:
  """ This function has been added so that you can see how to call functions from the distributor module.
  """
  header = distributor.getHeader()
  print(f'Column names are {", ".join(header)}.')
  
def main() -> None:
  """ This function handles user input and the operations for the library.
  """
  option = ""
  library = []
  initial_books = int(input("How many books do you initially want in your library (0..100)?:"))
  if initial_books < 0 or initial_books > 100:
    option = "QUIT"
  else:
    library = setupLibrary(initial_books)

  while option != "QUIT":
    option = input("Select an option (ADD, REMOVE, PRINT, TITLES, RECOMMEND, SAVE, QUIT): ").upper()        

    if option == "ADD":
      title = input("Title:")
      firstAuthor = input("First Author:")
      authors = input("All Authors:")
      publisher = input("Publisher:")
      pubdate = input("Publication Date:")
      pages = input("Page Numbers:")
      book_entry = createBookDictionary(title, firstAuthor, authors, publisher, pubdate, pages)
      addBook(library,book_entry)

    elif option == "REMOVE":
      index = int(input("Which # would you like to remove? "))
      removeBook(library, index)
        
    elif option == "PRINT":
      printLibrary(library)
        
    elif option == "TITLES":
      titles = getTitles(library)
      for item in titles:
          print(item, end="; ")
      print("END")

    elif option == "RECOMMEND":
      print("I recommend you read", getRandomCitation(library))
    
    elif option == "SAVE":
      save_option = input("Select an option (TITLES, ALL): ").upper()
      file_name = input("Enter the files name to save the library (without an extension): ")
      if save_option == "TITLES" and file_name:
        saveToFile(library, False, file_name + ".txt")
      elif save_option == "ALL":
        saveToFile(library, True, file_name + ".txt")
      else:
        print("Invalid Input")

  print("Goodbye!")

if __name__ == "__main__":
  if (test_mode):
    myTests()
  else:   
    main()