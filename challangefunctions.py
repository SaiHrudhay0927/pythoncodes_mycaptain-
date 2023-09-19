"""Python code to create a function called most_frequent that takes a string and prints the letters in decreasing
order of frequency using dictionaries"""
name1=input("Please enter a string : ")
def most_frequent(string):
    f=string.lower()
    d=dict()
    for key in f:
        if key not in d:
            d[key]=1
        else:
            d[key]=d[key]+1
    return d
print(most_frequent(name1))
