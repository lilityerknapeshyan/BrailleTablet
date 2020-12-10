
from tkinter import *
from Tablet import Tablet
from Book import Book
from Buttons import Buttons







print("Please, input the book text")
book_text = input()
book = Book(book_text)
print("Please, input amount of characters horizontally")
h = int(input())
print("Please, input amount of characters vertically")
v = int(input())
tablet = Tablet(h, v)
book.set_dimension(tablet)
root1 = Tk()
a = Buttons(root1)
a.set_book(book)
root1.mainloop()