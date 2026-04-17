from Search_elements import *
from File import *


S = Search_Controller()

print("Enter 1 to Sequential_Search\nEnter 2 to Fibonacci_Search\nEnter 3 Interpolation_Search")
variant = input("Your choose: ")

s = int(input("Enter the array size(100,1000): "))
var = int(input("Enter the element which we search: "))
S.Filling_array_random_elements(s)
print(f"Array: {S.array}\n\n")
if S.Searching(variant, var):
    print("Element is exist")
    print(f"Array: {S.history_list}")
    My_file = File()
    My_file.Write_File(10, S.array, var)
else:
    print("Element is not exist")


