#!/usr/bin/env python3

class Shoe:
    '''blueprints shoe'''
    def __init__(self, brand, size):
        '''initialize attributes'''
        self.brand = brand
        self.size = size

    @property
    def size(self):
        '''shoe size property'''
        return self._size 
    
    @size.setter
    def size(self, size):
        '''set size with validation'''
        if type(size) not in (int, float):
            print("size must be an integer")
        else:
            self._size = size
        
    #size = property(get_size, set_size)

    def cobble(self):
        '''repais shoe'''
        print("Your shoe is as good as new!")
        self.condition = "New"


youth_shoe = Shoe("Adibas", 7)

print(youth_shoe.cobble())
print(youth_shoe.condition)