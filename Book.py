import winsound
import json
from DoubleLinkedList import DoubleLinkedList
from HashMap import HashMap

class Book:
    def __init__(self, text):
        self.text = text
        self.current_page = 0
        self.pages_linked = DoubleLinkedList()
        self.current_node = None
        self.turned_on = False

    def set_dimension(self, tablet):
        self.tablet = tablet

    def get_char_capacity(self):
        char_capacity = self.tablet.get_char_capacity()
        return char_capacity

    def translate_text(self):
        with open('pun_to_braille.json') as data_file:
            pun_to_braille_dict = json.load(data_file)
        pun_to_braille = HashMap()
        for k, v in pun_to_braille_dict.items():
            pun_to_braille.put(k, v)

        with open('num_to_braille.json') as data_file:
            num_to_braille_dict = json.load(data_file)
        num_to_braille = HashMap()
        for k, v in num_to_braille_dict.items():
            num_to_braille.put(k, v)


        with open('alpha_to_braille.json') as data_file:
            alpha_to_braille_dict = json.load(data_file)
        alpha_to_braille = HashMap()
        for k, v in alpha_to_braille_dict.items():
            alpha_to_braille.put(k, v)

        translated_text = ""
        for char in self.text:
            if char == ' ':
                translated_text += ' '
                continue
            if alpha_to_braille.has_key(char):
                translated_text += alpha_to_braille.get(char)
            if num_to_braille.has_key(char):
                translated_text += num_to_braille.get(char)
            if pun_to_braille.has_key(char):
                translated_text += pun_to_braille.get(char)
        file = open("translated_text.json", "w")
        file.write(json.dumps(translated_text))
        file.close()

    def get_translated_text(self):
        self.translate_text()
        with open("translated_text.json") as file:
            translated_text = json.load(file)
        return translated_text

    def set_current_page(self, index):
        self.current_page = index

    def separate_pages(self):
        translated_text = self.get_translated_text()
        char_capacity = self.get_char_capacity()
        char_count = len(translated_text)
        char_remain = len(translated_text)
        char_index = 0
        pages = []
        while char_remain > 0:
            if char_index + char_capacity < char_count:
                if translated_text[char_index + char_capacity] == " ":
                    pages.append(translated_text[char_index: char_index + char_capacity])
                    char_remain = char_remain - len(translated_text[char_index:char_index + char_capacity])
                    char_index = char_index + char_capacity

                else:
                    i = 1
                    while translated_text[char_index + char_capacity - i] != " ":
                        i = i + 1
                    pages.append(translated_text[char_index:char_index + char_capacity - i])
                    char_remain = char_remain - len(translated_text[char_index:char_index + char_capacity - i])
                    char_index = char_index + char_capacity - i
            else:
                pages.append(translated_text[char_index:])
                char_remain = char_remain - len(translated_text[char_index:])
        file = open("pages.json", "w")
        file.write(json.dumps(pages))
        file.close()

    def turn_on(self):
        winsound.Beep(200, 300)
        if self.turned_on == False:
            self.separate_pages()
            with open('pages.json') as data_file:
                pages_list = json.load(data_file)
            for i in pages_list:
                self.pages_linked.add_last(i)
            self.turned_on = True
        if self.current_node == None:
            self.current_node = self.pages_linked.head
            print(self.current_node.data)
        else:
            print(self.current_node.data)

    def next_page(self):
        winsound.Beep(400, 300)
        if self.current_node.next != None:
            self.current_node = self.pages_linked.get_next_node(self.current_node)
            print(self.current_node.data)

    def previous_page(self):
        winsound.Beep(600, 300)
        if self.current_node.prev != None:
            self.current_node = self.pages_linked.get_prev_node(self.current_node)
            print(self.current_node.data)

    def turn_off(self):
        winsound.Beep(300, 300)