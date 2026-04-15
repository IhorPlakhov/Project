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
    def Searching_element(self, arr, ind_list, element):
        pass

class Sequential_Search(Search):

    def Searching_element(self, arr, ind_list, element):
        self.comparison_counter = 0
        for i in range(0,len(arr)):
            self.comparison_counter+=1
            ind_list.append(i)
            if i == element:
                return True
            
        return False
                
class Fibonacci_Search(Search):

    def Searching_element(self, arr, ind_list, element):
        self.comparison_counter = 0
        arr = array('i',sorted(arr))
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
                return True
            
            self.comparison_counter += 1
            if fib_num_1 and arr[offset + 1] == element:
                ind_list.append(offset + 1)
                return True
        
        return False

class Interpolation_Search(Search):
    
    def Searching_element(self, arr, ind_list, element):
        self.comparison_counter = 0
        arr = sorted(arr)
        low = 0
        high = len(arr)-1

        while low <= high and element >= arr[low] and element <= arr[high]:
            if arr[low] == arr[high]:
                ind_list.append(low)
                self.comparison_counter+=1
                if arr[low] == element:
                    return True
                return False
            
            pos = low + ((element-arr[low])*(high-low)//(arr[high]- arr[low]))
            ind_list.append(pos)
            self.comparison_counter+=1
            if arr[pos] == element:
                return True
            elif arr[pos] < element:
                low = pos + 1
            else:
                high = pos - 1

        return False

class Hash_Function_Search(Search):
    
    def Searching_element(self, arr, ind_list, element):
        pass

class Sort_Controller():

    def __init__(self):
        self._history_list = []
        self._array = None

        self._variants = {
        "1" : Sequential_Search(),
        "2" : Fibonacci_Search(),
        "3" : Interpolation_Search(),
        "4" : Hash_Function_Search()
    }

    @property
    def history_list(self):
        return self._history_list
    
    @property
    def array(self):
        return self._array

    def Filling_array_random_elements(self, size):
        if size>= 100 and size <= 1000:
            self._array= array('i', sample(range(0,size),size))
        else:
            raise ArraySizeError(size)
    
    def Searching(self, variant, target_element):
        self._history_list.clear()
        new_sort = self._variants[variant]
        return new_sort.Searching_element(self.array, self.history_list, target_element)
        
class ArraySizeError(Exception):
    
    def __init__(self, size):

        super().__init__(f"Error: Size of your array: {size}, but must be in range (100, 1000)")