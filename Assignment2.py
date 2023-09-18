# Python program to print all positive numbers in a range
x=int(input("Enter the number of elements you want in your list : "))
list1 = []
i=1
while i<=x:
    print("Enter the",i,"element you want to have in your list : ")
    y=int(input())
    list1.append(y)
    i=i+1
print("The list you entered is :",list1)
list2 = []
for j in list1:
    if(j>0):
        list2.append(j)
print("The new list is :",list2)
