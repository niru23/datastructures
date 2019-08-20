#!/usr/bin/python
import unittest
import time
import psutil
import datetime as dt
'''
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
12, 11, 13, 5, 6

Let us loop for i = 1 (second element of the array) to 4 (last element of the array)

i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
11, 12, 13, 5, 6

i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
11, 12, 13, 5, 6

i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position.
5, 11, 12, 13, 6

i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position.
5, 6, 11, 12, 13

Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.
Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
Sorting In Place: Yes
'''

def insertion_sort(ll):
    for i in range(len(ll)):
        temp =ll[i]
        j =i-1
        while j >=0 and temp < ll[j+1]:
            ll[j+1]= ll[j]
            j -=1
        ll[j+1]=temp
    return ll 

def insertion_sort_recursion(ll,n):
    if n <= 1:
        return ll
    insertion_sort_recursion(ll,n-1)
    last= ll[n-1]
    j = n-1-1
    while j >=0 and ll[j] >last:
              ll[j+1]=ll[j]
              j-=1
    ll[j+1] =last
    return ll  


class Test(unittest.TestCase):
    data = [([64, 25, 12, 22, 11],[11,12, 22, 25, 64])]
    data1 =[([64, 25, 12, 22, 11],5,[11,12, 22, 25, 64])]
    def  test_insertion_sort(self):
         print(self.data)
         for input,expected in self.data:
             n1=dt.datetime.now()
             actual = insertion_sort(input)
             n2=dt.datetime.now()
             print('Execution Time ',(n2-n1).microseconds,' ms' )
             print('memory % used:', psutil.virtual_memory()[2],'%')
             print('insertion sort recurssion')
         for input,n,expected in self.data1:
             n1=dt.datetime.now()
             actual = insertion_sort_recursion(input,n)
             n2=dt.datetime.now()
             print('Execution Time ',(n2-n1).microseconds,' ms' )
             print('memory % used:', psutil.virtual_memory()[2],'%')
             self.assertEqual(actual,expected)     


if __name__ =="__main__":
   unittest.main()
