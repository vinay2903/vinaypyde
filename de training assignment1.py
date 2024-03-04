
#1 Write a Python program to sum all the items in a list.
l=[1,2,3]
x=0
for i in l:
    x=x+i
print(x) 

#2 Write a Python program to multiply all the items in a list.
def mult(l):
    t=1

    for i in l:
        t=t*i
    return t
l=[4,2,3]
print(mult(l))

#3. Write a Python program to get the largest number from a list.
def largest(l):
   if len(l)==0:
       return None
   b=l[0]
   for i in range(0,len(l)-1):
       if l[i]>l[i+1] and l[i]>=b:
           b=l[i]
   return b
l=[]
print(largest(l))

#4. Write a Python program to get the smallest number from a list.
def smallest(l):
   if len(l)==0:
       return None
   b=l[0]
   for i in l:
       if i<b:
           b=i
   return b
l=[1,2,3,4,5,6,7,8,9]
print(smallest(l))

#5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
	Sample List : ['abc', 'xyz', 'aba', '1221']
	Expected Result : 2
    
 def count_str(l):
    c=0
    for i in range(0,len(l)):
        if len(l[i])>=2:
            st=l[i]
            j=len(st)
            if(st[0]==st[j-1]):
                c=c+1
    return c
l=['abc', 'xyx', 'aa', '1221']
x=count_str(l)
print(x)

#6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
    
def last_tup(l):
    for i in range(0,len(l)):
        for j in range(i+1, len(l)):
            if(l[i][len(l[i])-1]>l[j][len(l[j])-1]):
                l[i] , l[j]= l[j],l[i]
    return l

l=[(2, 5,6), (1, 2), (4, 4), (2, 3), (2, 1)]
print(last_tup(l))

#7. Write a Python program to remove duplicates from a list.
def rem_dup(l):
    j=[]
    for i in l:
        if i not in j:
            j.append(i)
    return j

l=[1,2,2,3,3,3,4]
print(rem_dup(l))

#8 Write a Python program to check if a list is empty or not

def list_empty(l):
    if(len(l)==0):
        return "list is empty"
    else:
        return "list is not empty"

l=[]
print(list_empty(l))

#9 Write a Python program to clone or copy a list.
def co(l):
    c=l
    return c
l=[1,2]
b=co(l)
print("original list", l)
print("copied list",b)

#10. Write a Python program to find the list of words that are longer than n from a given list of words.
def list_word(l,n):
    b=[]
    for i in l:
        if len(i)>n:
            b.append(i)
    return b

l=["abc","ad","efth"]
n=3
print(list_word(l,n))


Dictionary Programs:

Strings:
#1. Write a Python program to calculate the length of a string.
n=input("enter the string ")
print(len(n))

#2. Write a Python program to count the number of characters (character frequency) in a string.
	Sample String : google.com'
	Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
 def charfreq(s):

    char_frequency = {}

    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return s + ":" + str(char_frequency)


s = 'google.com'
print("Character frequency in the string "+charfreq(s))

#3  Write a  Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
	Sample String : 'w3resource'
	Expected Result : 'w3ce'
	Sample String : 'w3'
	Expected Result : 'w3w3'
	Sample String : ' w'
	Expected Result : Empty String
    
 def first_two(s):
    if len(s)<2:
        return ""
    else:
        a=""
        a=s[0:2]+ s[-2:]
        return a

s="w"
print(first_two(s))

#4 Write a  Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
	Sample String : 'restart'
	Expected Result : 'resta$t'
 
def recur(s):

 j=''
 for i in s:
    if i not in j:
        j=j+i
    elif (i in j) and j[0]==i:
        i='$'
        j=j+i
    else:
        j=j+i
 return j

s='naveen'
print(recur(s))

#5Write a  Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
	Sample String : 'abc', 'xyz'
	Expected Result : 'xyc abz'
   
s1="abc"
s2="xyz"
a=s2[:2]+s1[2:]
b=s1[:2]+s2[2:]
print(a+ " " +b )

#6 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
	Sample String : 'abc'
	Expected Result : 'abcing'
	Sample String : 'string'
	Expected Result : 'stringly'
    
  def add_strin(s):

  if len(s)>=3:
    if s[-3:]=='ing':
         s=s+'ly'
    elif  s[-3:]!='ing':
         s=s+'ing'
  return s

s='virt'
print(add_strin(s))

#7 Write a  Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
	Sample String : 'The lyrics is not that poor!'
	'The lyrics is poor!'
	Expected Result : 'The lyrics is good!'
	'The lyrics is poor!'

def samp(s):
  x_not=index_sub(s,'not')
  x_poor=index_sub(s,'poor')
  if(x_not!=-1 and x_poor!=-1 and x_not<x_poor):
     s=s[:x_not]+ "good" + s[x_poor+4:]
  return s
def index_sub(s,sub):
    for i in range(0, len(s)-len(sub)+1):
        if(s[i:i+len(sub)])==sub:
            return i

    return -1


s='i like poor not  thing'
print(samp(s))



#8 Write a  Python function that takes a list of words and return the longest word and the length of the longest one.
	Sample Output:
	Longest word: Exercises
	Length of the longest word: 9
l=['appl', 'banan', 'grape', 'orang', '',]
x=0
d=[]
if not l:
    print("none")
else:
  for i in l:
      z=len(i)
      if z>x:
        x=z
        d=[i]
      elif z==x:
        d.append(i)

print(str(d) +" " + str(x))

#9 Write a Python program to remove the nth index character from a nonempty string.
def xt(s,n):
   if n<0 or n>=len(s):
      return "invalid index"
   else:
    t= s[0:n]+s[n+1:]
   return t

s='abdgdju'
n=6
print(xt(s,n))

#10  Write a  Python program to change a given string to a newly string where the first and last chars have been exchanged.
def exchange(s):
    if s=='':
        return "blank string"
    elif len(s)==1:
        return s
    else:

        t=s[-1]+ s[1:-1] +s[0]
    return t

s='bfgh'
print(exchange(s))


#Dictionary Programs:
--------------------------
#1. Write a Python script to sort (ascending and descending) a dictionary by value.

d = {'a': 3, 'b': 2, 'c': 6, 'd': 1}

a_d = {}
for key in sorted(d, key=d.get):
    a_d[key] = d[key]

d_d = {}
for key in sorted(d, key=d.get, reverse=True):
    d_d[key] = d[key]


print("Original Dictionary:", d)
print("Ascending Sorted Dictionary:", a_d)
print("Descending Sorted Dictionary:", d_d)

#2. Write a Python script to add a key to a dictionary.

	Sample Dictionary : {0: 10, 1: 20}
	Expected Result : {0: 10, 1: 20, 2: 30}
def add_key(d,k,v):
        d[k]=v
        return d
d={0:10, 1:20}
k=3
v=4
print(add_key(d,k,v))

#3. Write a Python script to concatenate the following dictionaries to create a new one.

	Sample Dictionary :
	dic1={1:10, 2:20}
	dic2={3:30, 4:40}
	dic3={5:50,6:60}
	Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict = {}
dict.update(dict1)
dict.update(dict2)
dict.update(dict3)
print(dict)

#4 Write a Python script to check whether a given key already exists in a dictionary.
def pres(d,k):
    flag=0
    for i in d.keys():
     if k==i:
        flag=1
        break
    if(flag==1):
     return "present"
    else:
     return "not present"

d={1:10, 2:20}
k=4
print(pres(d,k))

#5. Write a Python program to iterate over dictionaries using for loops.
d={1:10, 2:20}
for k,v in d.items():
    print(f"{k}:{v}")

for i in d.keys():
   print(i)

for i in d.values():
 print(i)
#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
	#Sample Dictionary ( n = 5) :
	#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    
def num(n):
    d={}
    for i in range(1,n+1):
        d[i]=i*i
    return d
n=5
print(num(n))
#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
	#Sample Dictionary
	#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
    
d={}
for i in range(1,16):
    d[i]=i*i
print(d)
#8 Write a Python script to merge two Python dictionaries.    
def merg(d1,d2):
    d1.update(d2)
    return d1
d1={0: 10, 1: 20}
d2={3: 30, 4: 40}
print(merg(d1,d2))

#9. Write a Python program to iterate over dictionaries using for loops.
d={1:10, 2:20}
for k,v in d.items():
    print(f"{k}:{v}")

for i in d.keys():
   print(i)

for i in d.values():
 print(i)
    
#10. Write a Python program to sum all the items in a dictionary
d={1:10, 2:20}
x=0
for i in d.items():
  x=x+sum(i)
print(x)

y=sum(d.keys())
z=sum(d.values())
print(x)
print(y)