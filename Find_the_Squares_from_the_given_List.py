# Find the Squares from the given List
# Write a Python program to square the elements of a list using map() function.

num_list = []
size = int(input("Please provide the size of list:"))

for i in range(size):
        a = int(input("Please provide your input:"))
        num_list.append(a)
print("Your provided input:",num_list)

def square(lst):
    return lst**2

output = list(map(square,num_list))
print("Your output:",output)