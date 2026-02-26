""" This Python script is for you to test your code before submitting it. Please don't edit anything in this script. 

Usage: click "Shell" next to "Console", then type "python3 tests.py" as shown below:

~/Homework-Assignment-4$ python3 tests.py

Again, please don't edit anything in this script. 
"""

import unittest
from main import *

from unittest.mock import patch

import io
import sys
 

class SimpleTest(unittest.TestCase):

    def test_getRandomCitation(self):
        library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel Myerson', 'authors': 'Joel Myerson, Joel Myerson', 'publisher': 'Oxford University Press, USA', 'pubdate': 'Dec-00', 'pages': '752'}, {'title': 'Bombshells: War Stories and Poems by Women on the Homefront', 'firstAuthor': 'Missy Martin', 'authors': 'Missy Martin (Editor), Jesse Loren', 'publisher': 'OmniArts, LLC', 'pubdate': 'Jan-07', 'pages': '163'}, {'title': 'Imagination And Spirit', 'firstAuthor': 'J. Brent Bill', 'authors': 'J. Brent Bill (Editor), Shari Pickett Veach (Designed by), C. Michael Curtis (Foreword by), J. Brent Bill', 'publisher': 'Friends United Press', 'pubdate': 'Feb-06', 'pages': '292'}]
        book = getRandomCitation(library)
        citationlist = []
        for i in library:
            citationlist.append(getCitationInformation(i['title'], i['authors'], i['publisher'], i['pages'], i['pubdate']))
        self.assertIn(book, citationlist)
        
    def test_removeBookexception(self):
        library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel Myerson', 'authors': 'Joel Myerson, Joel Myerson', 'publisher': 'Oxford University Press, USA', 'pubdate': 'Dec-00', 'pages': '752'}, {'title': 'Bombshells: War Stories and Poems by Women on the Homefront', 'firstAuthor': 'Missy Martin', 'authors': 'Missy Martin (Editor), Jesse Loren', 'publisher': 'OmniArts, LLC', 'pubdate': 'Jan-07', 'pages': '163'}, {'title': 'Imagination And Spirit', 'firstAuthor': 'J. Brent Bill', 'authors': 'J. Brent Bill (Editor), Shari Pickett Veach (Designed by), C. Michael Curtis (Foreword by), J. Brent Bill', 'publisher': 'Friends United Press', 'pubdate': 'Feb-06', 'pages': '292'}]
        removeBook(library, 20)
  
    def test_removeBook(self):
        library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel Myerson', 'authors': 'Joel Myerson, Joel Myerson', 'publisher': 'Oxford University Press, USA', 'pubdate': 'Dec-00', 'pages': '752'}, {'title': 'Bombshells: War Stories and Poems by Women on the Homefront', 'firstAuthor': 'Missy Martin', 'authors': 'Missy Martin (Editor), Jesse Loren', 'publisher': 'OmniArts, LLC', 'pubdate': 'Jan-07', 'pages': '163'}, {'title': 'Imagination And Spirit', 'firstAuthor': 'J. Brent Bill', 'authors': 'J. Brent Bill (Editor), Shari Pickett Veach (Designed by), C. Michael Curtis (Foreword by), J. Brent Bill', 'publisher': 'Friends United Press', 'pubdate': 'Feb-06', 'pages': '292'}]
        removeBook(library, 1)
        removeBook(library, -1)
        targets = [{'title': 'Bombshells: War Stories and Poems by Women on the Homefront', 'firstAuthor': 'Missy Martin', 'authors': 'Missy Martin (Editor), Jesse Loren', 'publisher': 'OmniArts, LLC', 'pubdate': 'Jan-07', 'pages': '163'}, {'title': 'Imagination And Spirit', 'firstAuthor': 'J. Brent Bill', 'authors': 'J. Brent Bill (Editor), Shari Pickett Veach (Designed by), C. Michael Curtis (Foreword by), J. Brent Bill', 'publisher': 'Friends United Press', 'pubdate': 'Feb-06', 'pages': '292'}] 
        self.assertEqual(library, targets)

    def test_getTitles(self):
        library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel Myerson', 'authors': 'Joel Myerson, Joel Myerson', 'publisher': 'Oxford University Press, USA', 'pubdate': 'Dec-00', 'pages': '752'}, {'title': 'Bombshells: War Stories and Poems by Women on the Homefront', 'firstAuthor': 'Missy Martin', 'authors': 'Missy Martin (Editor), Jesse Loren', 'publisher': 'OmniArts, LLC', 'pubdate': 'Jan-07', 'pages': '163'}, {'title': 'Imagination And Spirit', 'firstAuthor': 'J. Brent Bill', 'authors': 'J. Brent Bill (Editor), Shari Pickett Veach (Designed by), C. Michael Curtis (Foreword by), J. Brent Bill', 'publisher': 'Friends United Press', 'pubdate': 'Feb-06', 'pages': '292'}]
        titles = getTitles(library)
        targets = ['Transcendentalism: A Reader', 'Bombshells: War Stories and Poems by Women on the Homefront', 'Imagination And Spirit']
        targets.sort()
        self.assertEqual(titles, targets)

    def test_addBook(self):
        library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel Myerson', 'authors': 'Joel Myerson, Joel Myerson', 'publisher': 'Oxford University Press, USA', 'pubdate': 'Dec-00', 'pages': '752'}]
        book = {'title': 'Bombshells: War Stories and Poems by Women on the Homefront', 'firstAuthor': 'Missy Martin', 'authors': 'Missy Martin (Editor), Jesse Loren', 'publisher': 'OmniArts, LLC', 'pubdate': 'Jan-07', 'pages': '163'}
        addBook(library, book)
        self.assertIn(book, library) 

    def test_createBookDictionary(self):
        title = "Opening Spaces: An Anthology of Contemporary African Women's Writing"
        firstAuthor = "Yvonne Vera"
        authors = "Yvonne Vera"
        publisher = "Heinemann"
        pubdate = "Sep-99"
        pages = 186
        self.assertEqual(createBookDictionary(title, firstAuthor, authors, publisher, pubdate, pages), {'title': "Opening Spaces: An Anthology of Contemporary African Women's Writing", 'firstAuthor': "Yvonne Vera", 'authors': "Yvonne Vera", "publisher": "Heinemann", "pubdate": "Sep-99", "pages": 186}) 

    def test_setupLibrary_data_structure(self):
        library = setupLibrary(10)
        self.assertIsInstance(library, list)
        self.assertIsInstance(library[0], dict)
        self.assertEqual(list(library[0].keys()).sort(), ['title', 'firstAuthor', 'authors', 'publisher', 'pubdate', 'pages'].sort())
    
    def test_saveToFile(self):
        library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel', 'authors': 'Joel Myerson', 'publisher': 'Oxford', 'pubdate': 'Dec-00', 'pages': '752'}]
        saveToFile(library, False, "saveTest.txt")
        file = open("saveTest.txt", "r")
        text = file.read()
        text = text.strip()
        file.close()
        self.assertEqual('Transcendentalism: A Reader;', text)

if __name__ == '__main__':  
  unittest.main()
 