from abc import ABC, abstractmethod
from array import array
from random import sample
from math import sqrt

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

        hash1 = self.first_hashing(element, size)
        hash2 = self.second_hashing(element, size)
        for i in range(size):
            ind = (hash1 + i*hash2) % size
            
            index = self.hash_table[ind]

            self.comparison_counter += 1
            if index == -1:
                break

            self.comparison_counter += 1
            if arr[index] == element:
                return True, []
            
        return False, []
    
    def first_hashing(self, key, size):
        return key % size
    
    def second_hashing(self, key, size):
        return 1 + (key % (size-1))

    def first_prime_number(self, size):
        prime_number = size
        is_found = False
        while not is_found:
            for i in range(2,int(sqrt(prime_number))+1):
                if (prime_number % i == 0):
                    prime_number+=1
                    break
            else:
                is_found = True
    
        return prime_number

    def create_hash_table(self):
        size = self.first_prime_number(len(self.last_arr) * 2)
        self.hash_table = array("i", [-1] * size)

        for index in range(len(self.last_arr)):
            element = self.last_arr[index]
            
            hash1 = self.first_hashing(element, size)
            hash2 = self.second_hashing(element, size)
            for i in range(size):
                ind = (hash1+ i*hash2) % size

                if self.hash_table[ind] == -1:
                    self.hash_table[ind] = index
                    break
    
    def table_check(self, new_array):
        if(self.hash_table is None or self.last_arr is not new_array):
            self.last_arr = new_array
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
        return *(new_sort.searching_element(self.array, target_element)), new_sort.comparison_counter
        
class ArraySizeError(Exception):
    
    def __init__(self, size):

        super().__init__(f"Error: Size of your array: {size}, but must be in range (100, 1000)")