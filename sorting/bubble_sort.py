#!/usr/bin/python
import unittest
import time
import psutil
import datetime as dt
'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
Example:
First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

Third Pass:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

The  function always runs O(n^2) time even if the array is sorted. It can be optimized by stopping the algorithm if inner loop didn’t cause any swap.
'''

def bubble_sort(ll):
    for i in range(len(ll)):
        for j in range(i+1,len(ll)):
            if ll[i]>ll[j]:
                ll[i],ll[j] =ll[j],ll[i]
    return ll    


def bubble_sort_recursion(ll):
    try:
        for i in range(len(ll)):
            val =ll[i]
            if ll[i] > ll[i+1]:
                ll[i] =ll[i+1]
                ll[i+1] =val
                bubble_sort_recursion(ll)
            
    except IndexError:
        pass
    return ll


class Test(unittest.TestCase):
    data = [([64, 25, 12, 22, 11],[11,12, 22, 25, 64])]
    def  test_bubble_sorts(self):
         print(self.data)
         for input,expected in self.data:
             n1=dt.datetime.now()
             actual = bubble_sort(input)
             n2=dt.datetime.now()
             print('Execution Time ',(n2-n1).microseconds,' ms' )
             print('memory % used:', psutil.virtual_memory()[2],'%')
             print('bubble sort recurssion')
             n1=dt.datetime.now()
             actual = bubble_sort_recursion(input)
             n2=dt.datetime.now()
             print('Execution Time ',(n2-n1).microseconds,' ms' )
             print('memory % used:', psutil.virtual_memory()[2],'%')
             self.assertEqual(actual,expected)     


if __name__ =="__main__":
   unittest.main()
