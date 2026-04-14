from abc import ABC, abstractmethod
from array import array
from random import sample

class Search(ABC):

    def __init__(self):
        self._comparison_counter = 0
    
    @property
    def comparison_counter(self):
        return self._comparison_counter
    
    @comparison_counter.setter
    def comparison_counter(self, value):
        self._comparison_counter = value

    @abstractmethod
    def Searching_element(self, array, ind_list):
        pass

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
        self._history_list = []
        self._target_element = None
        self._array = None

    @property
    def target_element(self):
        return self._target_element

    @property
    def history_list(self):
        return self._history_list
    
    @property
    def array(self):
        return self._array

    _variants = {
        "s" : Sequential_Search,
        "f" : Fibonacci_Search,
        "i" : Interpolation_Search,
        "h" : Hash_Function_Search
    }

    def Filling_array_random_elements(self, size):
        self._array= array('i',[0]*size)
        self._array = sample(range(0,size+1),size)

    def Choosing_kind_sort(self, variant):
        new_sort = self._variants[variant]
        new_sort.Searching_element(self.target_element,self.history_list)

        

        
