from Search_elements import *
from File import *


Sort = Sort_Controller()

print("Enter 1 to Sequential_Search\nEnter 2 to Fibonacci_Search\nEnter 3 Interpolation_Search")
variant = input("Your choose: ")

s = int(input("Enter the array size(100,1000): "))
var = int(input("Enter the element which we search: "))
Sort.Filling_array_random_elements(s)
if Sort.Searching(variant, var):
    print("Element is exist")
else:
    print("Element is not exist")
print(f"Array: {Sort.array}")
print(f"Array: {Sort.history_list}")
