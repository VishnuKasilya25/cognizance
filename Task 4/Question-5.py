#Question-5

#A Program to print the following pattern.

num = int(input("Enter the number of rows:"))
for i in range(1,num+1):
    print(" "*(num-i)+"* "*i)
