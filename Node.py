#as implemented in the textbook

class Node:    
    def __init__(self,d):
        self._data = d
        self._next = None

    def get_data(self):
        return(self._data)

    def get_next(self):
        return(self._next)

    def set_data(self,newData):
        self._data = newData

    def set_next(self,newNext):
        self._next = newNext

    def __str__(self):
        return self.data 