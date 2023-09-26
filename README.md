# Group-4-LMS
Library Mangement system using python
Here we have used Classes:
bookclass: Represents a book with attributes like book number, title, author, publication, subject, cost, and status (available or issued).
memberclass: Represents a library member with attributes like member code, name, address, phone number, joining date, validity date, account balance, and status (book issued or not).
issue: Represents a book issued to a member, with attributes like member code, member name, book name, book code, issue date, and return date.
We have also imported some basic libraries which are mentioned below:
from pickle import load, dump
import os
import datetime
Overall, this code provides a basic library management system with functionalities for adding, 
modifying, searching, issuing, and reporting on books and members. Users can interact with the program through a menu-driven interface.
