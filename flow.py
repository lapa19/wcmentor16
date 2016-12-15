# variables
a=5 #integers
print(a)
pi = 3.14 #float
my_name='aparna' #strings
var = True #boolean
my_var = 5  #integer
my_var = 'tree' #string

#strings:
#immutable
#string concatenation
x='ap'
y='arna'
x+y
#Indexing:strings are indexed
x[0] #gives 'a'
#negative indexing: 
x[-1]	#gives 'p'
#slicing: 
y[0:2] #gives 'ar'
len(x) #gives 2

#lists
mylist = [1, 4, 9, 16, 25]
diff = [2,'ap',True]
#indexing,slicing same as strings
a=[1,3,5]
b=[7,9,9]
c=a+b
c=[1,3,5,7,9]
len(c) #gives 5
c.append(7) #append 7 at the end
c.pop(3) #pop from position 3, pops 7

#tuples
#immutable
t = ("harry","potter",15,5)


#dictionaries
runs = {"virat":103,"vijay":"30", "yadav":"26"}
runs["virat"] #gives 103


#sets
s = {3,1,4,2,3}
s #removes duplicates

a=1
#control flow statements:
if a<5:
    #do something
    print("hi")
elif a<10:
    #do something
    print("hello")
else:
    #do something
    print("bye")

#for
for i in c:
    print(i)

#range
for i in range(5):
    print(i)


for i in range(len(c)):
	print (c[i])

#while
i=1
while i<5:
    print (i)
    i=i+1

#break
#continue

#2 lists
names=['virat','vijay','yadav']
runs = [103,30,26]
for n,r in zip(names,runs):
    print (n, r)

#Functions:
def odd(num):
    if num%2:
       return True
    else:
       return False

#function call
odd(5)

#Modules
#file1.py
def odd(num):
    if num%2:
       return True
    else:
       return False


def prime(n):
     for i in range(2,int(math.ceil(math.sqrt(n)))):
             if n%i == 0:
                return False
     return True

#importing
import file1.py
file1.odd(5)

from file1 import odd
odd(5)

from file1 import *
odd(5)
prime(5)

#reading and writing files
f = open('workfile', 'w')
f.read(1)
f.seek(5)
f.readline()
s = "myname"
f.write(s)

#HTML

#urllib
import urllib2
url = urllib2.urlopen("http://www.imdb.com/chart/top")
content = url.read()

#beautifulsoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index.html"))
soup = BeautifulSoup("<html>data</html>")
soup.p
soup.p['class']
soup.find_all('a')
soup.get_text()
tag = soup.b
tag.name
tag.name = "strong"

#<head><title>Harry potter</title></head>
head_tag = soup.head
head_tag.contents
title_tag = soup.title
title_tag
# <title>Harry Potter/title>
title_tag.parent
# <head><title>Harry Potter</title></head>
