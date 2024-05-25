#!/usr/bin/env python3

class Book:
    '''blueprints a book'''
    def __init__(self,title,page_count):
        '''initialie attributes'''
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        '''age_count property'''
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        '''set page_count'''
        if type(page_count) in (int, float):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
            
    #page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        '''turns book page'''
        print("Flipping the page...wow, you read fast!")



kid_book = Book("Aman", 20)

print(kid_book.turn_page())
        