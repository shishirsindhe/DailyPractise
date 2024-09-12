# 1. Write a program to find the length of the string without using inbuilt function (len)**
# s="Length of the string"
# char_count=0
# for char in s:
#     char_count+=1
# print(char_count)

# **2. Write a program to reverse a string without using any inbuilt functions.**
s="Hai Hello How are you"
rev=""
# for char in s:
#     rev=char+rev
# print(rev)

# for index in range(len(s)-1,-1,-1):
#     rev+=s[index]
# print(rev)

# **3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".**
# s="Hello World"
# res=""
# for word in s.split():
#     if word =="World":
#         res+="Universe"
#     else:
#         res+=word+' '
# print(res)

# **4. How to convert a string to a list and vice-versa.**
# s="string and list"
# li=s.split()
# print(li)
# st=''
# for item in li:
#     st+=item+' '
# print(st)

# **5. Convert the string "Hello welcome to Python" to a comma separated string.**
# s="Hello welcome to Python"
# res=s.replace(' ',',')
# print(res)

# **6. Write a program to print alternate characters in a string.**
# s="Hello welcome to Python"
# res=''
# for index in range(len(s)):
#     if index % 2==0:
#         res+=s[index]
# print(res)

# **7. Write a Program to print ascii values of the characters present in a string.**
# s="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# caps=[]
# lower=[]
# for alpha in s:
#     if 'A'<=alpha<='Z':
#         caps+=[(ord(alpha))]
#     else:
#         lower+=[(ord(alpha))]
# print(caps)
# print(lower)

# **8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**
# s="ABDjsdnasjkJDNSJN"
# def conversion(string):
#     res_string=""
#     for char in string:
#         if "A"<=char<="Z":
#             res_string+=chr(ord(char)+32)
#         elif 'a'<=char<='z':
#             res_string+=chr(ord(char)-32)
#     return res_string
# print(conversion(s))

# **9. Write a program to swap two numbers without using the 3rd variable.**
# a=10
# b=20
# a=a*b
# b=a//b
# a=a//b
# print(a)
# print(b)

# **10. Write a program to merge two different lists.**
# a=[1,2,3,4]
# b=[5,6,7,8]
# print(a+b)
# print([*a,*b])

# **11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)**
# path=r"D:\PYTHON RMG\SANDEEP SIR\File Handelling\points.txt"
# with open (path,'r') as f:
#     n=50
#     line_count=0
#     for line in f:
#         line_count+=1
#         if line_count==n:
#             print(line)
#             break

# **12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)**
# path=r"D:\PYTHON RMG\SANDEEP SIR\File Handelling\points.txt"
# with open (path,'r') as f:
#     from itertools import islice
#     n=10
#     lines="".join(islice(f,n-1,n+5))
#     print(lines)

# **13 Program to print the last "N" lines of a file.**

# **14. Write a program to check if the given string is Palindrome or not without using reversed method.**
# s="racecar"
# pall=""
# for char in s:
#     pall=s[::-1]
# if pall ==s:
#     print("It's a Pallindrome")
# else:
#     print("It's not a pallindrome")

# **15 Write a program to search for a character in a given string and return the corresponding index.
# s="Welcome to India"
# char=input("Enter the character's index that u want")
# for index in range(len(s)):
#     if s[index]==char:
#         print(index)

# 16. Write a program to get the below output
# sentence = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
# out={}
# for word in sentence.split():
#     if word[0] not in out:
#         out[word[0]]=[word]
#     else:
#         out[word[0]]+=[word]
# print(out)

# **17 Write a to replace all the characters with - if the character occurs more than once in a string**
# ```python
# my_string = 'hellohai' # O/P should be '-e--o-ai'
# s="hellohai"
# res=""
# for char in s:
#     if char not in res:
#         res+=char
#     else:
#         res+='-'
# print(res)

# **18 write a decorator that returns only positive values of subtraction**

# **19 How to get the count of the number of instances of a class that is being created.**

# **20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer or float it should reverse it.**

class Employee:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

e1 = Employee("steve", "jobs", 26)
e2 = Employee("bill", "gates", 27)
e3 = Employee("amy", "masters", 28)
e4 = Employee("john", "dow", 22)

# Sort the below list of employees based on their "age".
employees = [e1, e2, e3, e4]

by_age=sorted(employees,key=lambda item:item.age)

# for i in by_age:
#     print(i.age)

# l=[1,2,3,4,5,6]
# for num in reversed(range(len(l)+1)):
#     print(num)

# numbers = [1, 3, 5, 7, 9]
# for num in range(10):
#     if num in numbers:
#         continue
#     else:
#         print(num)

s="welcome"
out=s[::3]
print(out)
res=""
for i in range(len(s)):
    if s[i] in s[::3]:
        res+=s[i].upper()
    else:
        res+=s[i]
print(res)