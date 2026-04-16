from Search_elements import *
from File import *


S = Sequential_Controller()

print("Enter 1 to Sequential_Search\nEnter 2 to Fibonacci_Search\nEnter 3 Interpolation_Search")
variant = input("Your choose: ")

s = int(input("Enter the array size(100,1000): "))
var = int(input("Enter the element which we search: "))
S.Filling_array_random_elements(s)
if S.Searching(variant, var):
    print("Element is exist")
else:
    print("Element is not exist")
print(f"Array: {S.array}")
print(f"Array: {S.history_list}")
