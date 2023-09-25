#(First assignment Task 1) To write a Python program which accepts the radius of a circle from the user and computes area.
x=int(input("Enter the radius of your choice to calculate the area of a cricle "))
y=3.14*x*x
print("The area of the circle with radius", x, "is", y)

#(First assignment Task 2) To write a Python program to accept a filename from the user and print the extension of that.
filename = input("Input the Filename: ")
f_ext = filename.split(".")
print ("The extension of the file is : " + repr(f_ext[-1]))
