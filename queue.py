#!/usr/bin/python

class Queue:
    def __init__(self,capacity):
        self.size =0
        self.front = 0
        self.rear =capacity -1
        self.Q = [None]*capacity
        self.capacity = capacity
    def isFull(self):
        return self.size == self.capacity
    def isEmpty(self):
        return self.size ==0
    def enQueue(self,item):
        if self.isFull():
            print('Queue is full')
            return
        else:
             self.rear = (self.rear+1)%(self.capacity)
             self.size = self.size+1
             self.Q[self.rear]=item
             print('Added item to the Queue -',item)
    def deQueue(self,item):
         if self.isEmptyl():
             print('Queue is empty') 
             return
         else:
             self.front = (self.front+1)%(self.capacity)
             self.size = self.size -1
             item = self.Q[self.front]
             print('Removed item from queue ',item)
    def getQueueFront(self):
          if self.isEmpty():
              print('The queue is empty')
          else:
               print('The front of the queue is ',self.Q[self.front])
    def getQueueRear(self):
          if self.isEmpty():
              print('The queue is empty')
          else:
               print('The front of the queue is ',self.Q[self.rear])
               
queue = Queue(6)
queue.enQueue(2)
queue.enQueue(4)  
queue.enQueue(6)  
queue.enQueue(8)
queue.enQueue(10)
queue.enQueue(12)
queue.enQueue(14)
queue.getQueueFront()
queue.getQueueRear()