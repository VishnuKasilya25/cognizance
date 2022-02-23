#Question - 3

# PROGRAM TO CREATE A 2D LIST CONSISTING OF STUDENTs DETAIL AND PRESENTING THEM

L = []
n = int(input("Enter number of students record to be inserted in 2D List:"))
for i in range(n):
    Name  = input("Enter name Of the Student:")
    Roll = int(input("Enter roll number of the Student:"))
    Marks = int(input("Enter Marks obtained by the Student:"))
    L.append([Name, Roll, Marks])

print()
print("Presenting Student Records")
print("Name\t\t Roll No\t\t Marks")
for i in L:
    print(i[0], "\t\t\t", i[1], "\t\t", i[2])

# PROGRAM TO DISPLAY THE 2ND ROW FROM THE  2D LIST

print()
print("Displaying 2nd record from 2D List")
print("Name\t\t Roll No\t\t Marks")
for i in range(len(L)):
    if i == 1:
        print(L[i][0], "\t\t\t", L[i][1], "\t\t", L[i][2])
