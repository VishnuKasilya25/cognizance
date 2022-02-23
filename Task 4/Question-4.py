#Question 4

#To check if a number is palindrome

# Take input
print("Enter a random number")
number = int(input())
temp =number
reverse = 0

while(number>0):
    dig = number%10
    reverse = reverse *10 + dig
    number = number//10
print(reverse)

if temp==reverse:
    print("Number is a palindrome")
    print("True")
else:
    print("Number is not a palindrome")
    print("False")
