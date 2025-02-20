#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size

    def get_brand(self):    
        return self._brand  

    def set_brand(self, brand):
        self._brand = brand

    def get_size(self):     
        return self._size   

    def set_size(self, size):
        if not type(size) == int:   
            print("size must be an integer")
        else:
            self._size = size

    def cobble(self):
        print("Your shoe is as good as new!")
        condition = "New"
        self.condition = condition

    

    brand = property(get_brand, set_brand)  
    size = property(get_size, set_size)