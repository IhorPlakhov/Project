from Search_elements import *
from File import *

S = SearchController()

print("Enter 1 to SequentialSearch\nEnter 2 to FibonacciSearch\nEnter 3 InterpolationSearch\nEnter 4 HashFunctionSearch")
variant = input("Your choose: ")

history_list=[]
s = int(input("Enter the array size(100,1000): "))
S.filling_array_random_elements(s)
print(f"Array: {S.array}\n")
var = int(input("Enter the element which we search: "))
is_found, history_list =  S.searching(variant, var)
if is_found:
    print("Element is exist")
    print(f"History list: {history_list}")
    My_file = File()
    My_file.write_file(10, S.array, var)
else:
    print("Element is not exist")
