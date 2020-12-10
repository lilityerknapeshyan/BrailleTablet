from tkinter import *


class Buttons:
    def __init__(self, root):
        
        self.root = root

        topframe = Frame(root)
        topframe.pack()
        bottomframe = Frame(root)
        bottomframe.pack(side=BOTTOM)

        button1 = Button(bottomframe, text="Next Page", fg="red", command=self.next_page)
        button2 = Button(bottomframe, text="Previous Page", fg="green", command=self.previous_page)
        button3 = Button(topframe, text="Turn Off", fg="purple", command=self.turn_off)
        button4 = Button(topframe, text="Turn On", fg="blue", command=self.turn_on)

        button1.pack(side=LEFT)
        button2.pack(side=LEFT)
        button3.pack(side=LEFT)
        button4.pack(side=LEFT)


    def set_book(self, book):
        self.book = book

    def next_page(self):
        self.book.next_page()
        return

    def previous_page(self):
        self.book.previous_page()
        return

    def turn_on(self):
        self.book.turn_on()
        return

    def turn_off(self):
        self.book.turn_off()
        return

