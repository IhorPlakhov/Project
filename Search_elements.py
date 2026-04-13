from abc import ABC, abstractmethod
from array import array
from random import sample

class Search(abs):

    def __init__(self):
        self._permutations_counter = 0
    
    @property
    def permutations_counter(self):
        return self._permutations_counter
    
    @permutations_counter.setter
    def permutations_counter(self, value):
        self._permutations_counter = value

    @abstractmethod
    def Searching_element(self, array):
        self.permutations_counter=0

class Sequential_Search(Search):
    
    pass

class Fibonacci_Search(Search):
    
    pass

class Interpolation_Search(Search):
    
    pass

class Hash_Function_Search(Search):
    
    pass

class Sort_Controller():

    def __init__(self):
        self.__target_element = None
        self.__array = None

    @property
    def target_element(self):
        return self.__target_element
    
    @target_element.setter
    def permutations_counter(self, value):
        self.__target_element = value
    
    @property
    def array(self):
        return self.__array
    
    @array.setter
    def permutations_counter(self, value):
        self.__array = value

    def Filling_array_random_elements(self, size):
        self.array('i',[0]*size)
        array = sample(range(0,size+1),size)

    def Choosing_kind_sort(self, variant):
        sort = None
        variants = {
            "s" : sort = Sequential_Search();
            "f" : sort = Fibonacci_Search();
            "i" : sort = Interpolation_Search();
            "h" : sort = Hash_Function_Search()
        }

        
