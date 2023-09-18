#Python program to print fibonacci series
n1=0
n2=1
n3=0
i=1
fibo = [0, 1]
terms=int(input("Enter the number of terms you want in fibonacci series after 0 and 1: "))
if(terms<=0):
    print("please enter a number greater than 0")
elif(terms==1):
    print("",fibo.append(1))
else:
    while i<=terms:
        n3=n1+n2
        fibo.append(n3)
        n1=n2
        n2=n3
        i=i+1
print(fibo)
