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
    def searching_element(self, arr, element):
        pass

class SequentialSearch(Search):

    def searching_element(self, arr, element):
        ind_list = []
        for i in range(0,len(arr)):
            self.comparison_counter+=1
            ind_list.append(i)
            if arr[i] == element:
                return True, ind_list
            
        return False, ind_list
                
class FibonacciSearch(Search):

    def searching_element(self, arr, element):
        ind_list = []
        arr_size = len(arr)
        fib_num_2 = 0
        fib_num_1 = 1
        fib_num = 1

        while fib_num < arr_size:
            fib_num_2 = fib_num_1
            fib_num_1 = fib_num
            fib_num = fib_num_2 + fib_num_1
        
        offset = -1

        while fib_num > 1:
            i = offset + fib_num_2 if offset + fib_num_2 < arr_size-1 else arr_size-1
            ind_list.append(i)
            self.comparison_counter+=1
            if arr[i] < element:
                fib_num = fib_num_1
                fib_num_1 = fib_num_2
                fib_num_2 = fib_num - fib_num_1
                offset = i
            elif arr[i] > element:
                fib_num = fib_num_2
                fib_num_1 = fib_num_1 - fib_num_2
                fib_num_2 = fib_num - fib_num_1
            else:
                return True, ind_list
            
            self.comparison_counter += 1
            if fib_num_1 and arr[offset + 1] == element:
                ind_list.append(offset + 1)
                return True, ind_list
        
        return False, ind_list

class InterpolationSearch(Search):
    
    def searching_element(self, arr, element):
        ind_list = []
        low = 0
        high = len(arr)-1

        while low <= high and element >= arr[low] and element <= arr[high]:
            if arr[low] == arr[high]:
                ind_list.append(low)
                self.comparison_counter+=1
                if arr[low] == element:
                    return True, ind_list
                return False, ind_list
            
            pos = low + ((element-arr[low])*(high-low)//(arr[high]- arr[low]))
            ind_list.append(pos)
            self.comparison_counter+=1
            if arr[pos] == element:
                return True, ind_list
            elif arr[pos] < element:
                low = pos + 1
            else:
                high = pos - 1

        return False, ind_list

class HashFunctionSearch(Search):

    def __init__ (self):
        super().__init__()
        self.hash_table = None
        self.last_arr = None

    def searching_element(self, arr, element):
        self.table_check(arr)
        size = len(self.hash_table)

        ind = element % size
        
        for i in range(size):
            ind = (ind + i) % size
            
            self.comparison_counter += 1
            if self.hash_table[ind] == element:
                return True, []
            
            self.comparison_counter += 1
            if self.hash_table[ind] == -1:
                break
            
        return False, []

    def create_hash_table(self):
        size = len(self.last_arr) * 2 
        self.hash_table = array("i", [-1] * size) # It is necessary to specify the size of the hash table
    
        for key in self.last_arr:
            index = key % size
            
            for i in range(size):
                index = (index + i) % size
                
                if self.hash_table[index] == -1:
                    self.hash_table[index] = key
                    break
    
    def table_check(self, array):
        if(self.hash_table is None or self.last_arr is not array):
            self.last_arr = array
            self.create_hash_table()

class SearchController():

    def __init__(self):
        self._array = None

        self._variants = {
        "1" : SequentialSearch(),
        "2" : FibonacciSearch(),
        "3" : InterpolationSearch(),
        "4" : HashFunctionSearch()
    }
    
    @property
    def array(self):
        return self._array

    def filling_array_random_elements(self, size):
        if size >= 100 and size <= 1000:
            self._array= array('i', sample(range(0,size * 10),size))
        else:
            raise ArraySizeError(size)
    
    def searching(self, variant, target_element):
        new_sort = self._variants[variant]
        if variant == "2" or variant == "3":
            self._array = array('i',sorted(self._array))
        new_sort.comparison_counter = 0
        return new_sort.searching_element(self.array, target_element)
        
class ArraySizeError(Exception):
    
    def __init__(self, size):

        super().__init__(f"Error: Size of your array: {size}, but must be in range (100, 1000)")