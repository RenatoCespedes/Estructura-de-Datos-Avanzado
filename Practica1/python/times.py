from matplotlib import pyplot as plt
from time import time
from bubbleSort import *
from Counting_Sort import *
from heapsort import *
from insertionSort import *
from mergesort import *
from quicksort import *
from selectionsort import *
for i in range(10000,100001,10000):
    file = open('Array_'+str(i)+'.txt','r')
    aux = file.readlines()
    file.close()
    arr = [int(i) for i in aux[0].split()]
    a = arr
    file = open("python_bubble.txt",'a')
    start = time()
    BubbleSort(a)
    elapsed = time() - start
    file.write("Length "+str(i)+'\n')
    file.write(str(elapsed)+'\n')
    file.close()
    print('Bubble '+str(i)+' f')
    a = arr
    file = open("python_insertion.txt",'a')
    start = time()
    InsertionSort(a)
    elapsed = time() - start
    file.write("Length "+str(i)+'\n')
    file.write(str(elapsed)+'\n')
    file.close()
    print('Insert '+str(i)+' f')
    a = arr
    file = open("python_merge.txt",'a')
    start = time()
    mergeSort(a)
    elapsed = time() - start
    file.write("Length "+str(i)+'\n')
    file.write(str(elapsed)+'\n')
    file.close()
    print('Merge '+str(i)+' f')
    a = arr
    file = open("python_quick.txt",'a')
    start = time()
    quickSort(a,0,i-1)
    elapsed = time() - start
    file.write("Length "+str(i)+'\n')
    file.write(str(elapsed)+'\n')
    file.close()
    print('Quick '+str(i)+' f')
    a = arr
    file = open("python_selection.txt",'a')
    start = time()
    selectionsort(a)
    elapsed = time() - start
    file.write("Length "+str(i)+'\n')
    file.write(str(elapsed)+'\n')
    file.close()
    print('Selection '+str(i)+' f')
    a = arr
    file = open("python_counting.txt",'a')
    start = time()
    a=countingSort(a)
    elapsed = time() - start
    file.write("Length "+str(i)+'\n')
    file.write(str(elapsed)+'\n')
    file.close()
    print('Counting '+str(i)+' f')
    a = arr
    file = open("python_heap.txt",'a')
    start = time()
    heapSort(a)
    elapsed = time() - start
    file.write("Length "+str(i)+'\n')
    file.write(str(elapsed)+'\n')
    file.close()
    print('Heap '+str(i)+' f')
