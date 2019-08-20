#!/usr/bin/python
import unittest
import time
import psutil
import datetime as dt
'''
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
'''
def mergesort(ll):
    if len(ll)>1:
        mid = round(len(ll)/2)
        left =ll[:mid]
        right = ll[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k =0
        while i < len(left) and j < len(right):
              if left[i] <right[j]:
                 ll[k] =left[i]
                 i+=1
              else:
                  ll[k] =right[j]
                  j+=1
              k+=1
        while  i < len(left):
              ll[k] =left[i]
              i+=1
              k+=1
        while  j < len(right):
               ll[k] =right[j]
               j+=1
               k+=1
    return ll
def merge(left, right): 
    if not len(left) or not len(right): 
        return left or right 
  
    result = [] 
    i, j = 0, 0
    while (len(result) < len(left) + len(right)): 
        if left[i] < right[j]: 
            result.append(left[i]) 
            i+= 1
        else: 
            result.append(right[j]) 
            j+= 1
        if i == len(left) or j == len(right): 
            result.extend(left[i:] or right[j:]) 
            break 
  
    return result 
  
def mergesort_iterative(list): 
    if len(list) < 2: 
        return list
  
    middle = round(len(list)/2)
    
    left = mergesort_iterative(list[:middle]) 
    right =mergesort_iterative(list[middle:]) 
  
    return merge(left, right) 
class Test(unittest.TestCase):
    data = [([4, 5, 12, 15, 14, 10, 8, 18, 19, 20],[4, 5, 8, 10, 12, 14, 15, 18, 19, 20])]
    def  test_mergesort(self):
         print(self.data)
         for input,expected in self.data:
             n1=dt.datetime.now()
             actual = mergesort(input)
             n2=dt.datetime.now()
             print('Execution Time ',(n2-n1).microseconds,' ms' )
             print('memory % used:', psutil.virtual_memory()[2],'%')
             print('merge sort sort iterative')
             n1=dt.datetime.now()
             actual = mergesort_iterative(input)
             n2=dt.datetime.now()
             print('Execution Time ',(n2-n1).microseconds,' ms' )
             print('memory % used:', psutil.virtual_memory()[2],'%')
             print('insertion sort recurssion')
         


if __name__ =="__main__":
   unittest.main()
