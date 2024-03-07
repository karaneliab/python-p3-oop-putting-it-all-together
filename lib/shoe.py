#!/usr/bin/env python3

class Shoe:

    def __init__(self,brand ,size):
        self.brand = brand
        self.size = size
        self.condition = 'New'
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,value):
        if isinstance(value , int):
            self._size = value
        else:
            print("size must be an integer")
    def cobble(self):
        print("The shoe has been repaired")
        self.condition = 'New'  


shoe = Shoe('Nike', 9)
print(f'Condition before repair: {shoe.condition}')
shoe.cobble()
print(f'Condition after repair: {shoe.condition}')
