# Find the way with Maps
# Write a Python program to triple all numbers of a given list of integers. Use Python map.

num_list = []
size = int(input("Please provide the size of list:"))

for i in range(size):
    a = int(input("Please provide your input:"))
    num_list.append(a)
print("Your provided input:",num_list )

Output = list(map(lambda a:a*3,num_list))
print("Your output :",Output)