*** Settings ***
Library     ../source/library_kyewords.py
Library     BuiltIn

*** Test Cases ***
Test User Can Reserve And Take Book
    Create Book    Book_1    Author_1    100    12345
    Create User    Kate
    Reserve Book    Kate    Book_1
    Book Should Be Reserved    Book_1
    Take Book    Kate    Book_1
    Book Should Not Be Reserved    Book_1
    Book Should Be In Use    Book_1
    User Should Have Book    Kate    Book_1

Test User Cannot Take Reserved Book By Another User
    Create Book    Book_2    Author_2    200    23456
    Create User    Anna
    Create User    Kate
    Reserve Book    Anna    Book_2
    Book Should Be Reserved    Book_2
    Take Book    Kate    Book_2
    Book Should Be Reserved    Book_2
    Book Should Not Be In Use    Book_2
    User Should Not Have Book    Kate    Book_2
    Take Book    Anna    Book_2
    Book Should Not Be Reserved    Book_2
    Book Should Be In Use    Book_2
    User Should Have Book    Anna    Book_2

Test User Can Return Book
    Create Book    Book_3    Author_3    150    34567
    Create User    Kate
    Take Book    Kate    Book_3
    Book Should Be In Use    Book_3
    Return Book    Kate    Book_3
    Book Should Not Be In Use    Book_3
    User Should Not Have Book    Kate    Book_3
