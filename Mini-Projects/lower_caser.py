# Implement function ToLowerCase() that has a string parameter str,
# and returns the same string in lowercase.

def ToLowerCase(string):
    newstr = string.lower()
    return newstr


string = ToLowerCase(input("What's the sentence you want to make lowercase? "))
print(string)