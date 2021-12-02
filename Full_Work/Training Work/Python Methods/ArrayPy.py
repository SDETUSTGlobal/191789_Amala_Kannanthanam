#array declaration
import array as myarray
abc = myarray.array('d', [2.5, 4.9, 6.7])
print(abc[0:3])
#access array elemnts
import array
balance = array.array('i', [300,200,100])
print(balance[1])
#access 2
import array as myarray
abc = myarray.array('d', [2.5, 4.9, 6.7])
print("Array first element is:",abc[0])
print("Array last element is:",abc[-1])
#acces3
import array as myarray
abc= myarray.array('q',[3,9,6,5,20,13,19,22,30,25])
print(abc[1:4])
print(abc[7:10])
#insert elements in array
import array
balance = array.array('i', [300,200,100])
balance.insert(2, 150)
print(balance)
#insert2
import array as myarr
a=myarr.array('b',[2,4,6,8,10,12,14,16,18,20])
a.insert(2,56)
print(a)
#modify elements
import array as myarr
a=myarr.array('b',[3,6,4,8,10,12,14,16,18,20])
a[0]=99
print(a)
#modify as concatenate
import array as myarr
first = myarr.array('b', [4, 6, 8])
second = myarr.array('b', [9, 12, 15])
numbers = myarr.array('b')
numbers = second + first
print(numbers)
#pop method in array
import array as myarr
first = myarr.array('b', [20, 25, 30])
first.pop(2)
print(first)
#delete
import array as myarr
no = myarr.array('b', [10, 4, 5, 5, 7])
del no[4]
print(no)
#remove element
import array as myarray
first = myarray.array('b', [2, 3, 4])
first.remove(3)
print(first)
#search for index
import array as myarray
number = myarray.array('b', [11,22,33,44,55,66,77,88])
print(number.index(88))
#reverse array
import array as myarray
number = myarray.array('b', [1,2,3])
number.reverse()
print(number)
#array to unicode
from array import array
p = array('u',[u'\u0050',u'\u0059',u'\u0054',u'\u0048',u'\u004F',u'\u004E'])
print(p)
q = p.tounicode()
print(q)
#count occurence
import array as myarr
number = myarr.array('b', [2, 3, 5, 4,3,3,3])
print(number.count(3))
#traverse array
import array
balance = array.array('i', [300,200,100])
for x in balance:
    print(x)