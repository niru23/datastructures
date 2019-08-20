#!/usr/bin/python
import unittest
import time
import psutil
import datetime as dt
'''
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
'''

def selection_sort(ll):
    for i in range(len(ll)):
        min_idx = i
        # find min idx
        for j in range(i+1,len(ll)):
            if ll[min_idx]>ll[j]:
                min_idx=j
        #swap to the begining of the array
        ll[i],ll[min_idx]=ll[min_idx],ll[i]
    return ll  
    

      


class Test(unittest.TestCase):
    data = [([64, 25, 12, 22, 11],[11,12, 22, 25, 64])]
    def  test_selection_sorts(self):
         print(self.data)
         for input,expected in self.data:
             n1=dt.datetime.now()
             actual = selection_sort(input)
             n2=dt.datetime.now()
             print('Execution Time ',(n2-n1).microseconds,' ms' )
             print('memory % used:', psutil.virtual_memory()[2],'%')
             self.assertEqual(actual,expected)     


if __name__ =="__main__":
   unittest.main()
