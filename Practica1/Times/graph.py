from matplotlib import pyplot as plt
times = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
c_bubble = open("cpp_time_Bubble.txt",'r')
c_bubble_ger = c_bubble.readlines()
j_bubble = open("java_bubblesort.txt",'r')
j_bubble_ger = j_bubble.readlines()
p_bubble = open("python_bubble.txt","r")
p_bubble_ger = p_bubble.readlines()
#-------------------------------------------
c_insert = open("cpp_time_Insertion.txt",'r')
c_insert_ger = c_insert.readlines()
j_insert = open("java_insertsort.txt",'r')
j_insert_ger = j_insert.readlines()
p_insert = open("python_insertion.txt","r")
p_insert_ger = p_insert.readlines()
#-------------------------------------------
c_count = open("cpp_time_Counting.txt",'r')
c_count_ger = c_count.readlines()
j_count = open("java_CountingSortJ.txt",'r')
j_count_ger = j_count.readlines()
p_count = open("python_counting.txt","r")
p_count_ger = p_count.readlines()
#-------------------------------------------
c_merge = open("cpp_time_Merge.txt",'r')
c_merge_ger = c_merge.readlines()
j_merge = open("java_mergesort.txt",'r')
j_merge_ger = j_merge.readlines()
p_merge = open("python_merge.txt","r")
p_merge_ger = p_merge.readlines()
#-------------------------------------------
c_quick = open("cpp_time_Quick.txt","r")
c_quick_ger = c_quick.readlines()
j_quick = open("java_quicksort.txt","r")
j_quick_ger = j_quick.readlines()
p_quick = open("python_quick.txt","r")
p_quick_ger = p_quick.readlines()
#-------------------------------------------
c_heap = open("cpp_time_Heap.txt","r")
c_heap_ger = c_heap.readlines()
j_heap = open("java_heapsort.txt","r")
j_heap_ger = j_heap.readlines()
p_heap = open("python_heap.txt","r")
p_heap_ger = p_heap.readlines()
#-------------------------------------------
c_selec = open("cpp_time_Selection.txt","r")
c_selec_ger = c_selec.readlines()
j_selec = open("java_selection_sort.txt","r")
j_selec_ger = j_selec.readlines()
p_selec = open("python_selection.txt","r")
p_selec_ger = p_selec.readlines()
#-------------------------------------------
c_bubble_ = [float(i) for i in c_bubble_ger]
j_bubble_ = [float(i) for i in j_bubble_ger]
p_bubble_ = [float(i) for i in p_bubble_ger]

c_insert_ = [float(i) for i in c_insert_ger]
j_insert_ = [float(i) for i in j_insert_ger]
p_insert_ = [float(i) for i in p_insert_ger]

c_count_ = [float(i) for i in c_count_ger]
j_count_ = [float(i) for i in j_count_ger]
p_count_ = [float(i) for i in p_count_ger]

c_merge_ = [float(i) for i in c_merge_ger]
j_merge_ = [float(i) for i in j_merge_ger]
p_merge_ = [float(i) for i in p_merge_ger]

c_quick_ = [float(i) for i in c_quick_ger]
j_quick_ = [float(i) for i in j_quick_ger]
p_quick_ = [float(i) for i in p_quick_ger]

c_selec_ = [float(i) for i in c_selec_ger]
j_selec_ = [float(i) for i in j_selec_ger]
p_selec_ = [float(i) for i in p_selec_ger]

c_heap_ = [float(i) for i in c_heap_ger]
j_heap_ = [float(i) for i in j_heap_ger]
p_heap_ = [float(i) for i in p_heap_ger]

plt.plot(times,p_bubble_,color='r',label='Bubble python')
plt.plot(times,c_bubble_,color='b',label='Bubble c++')
plt.plot(times,j_bubble_,color='y',label='Bubble java')
plt.legend(title='Bubble Sort')
plt.savefig("Bubble_Sort_Comparasion.png")
plt.clf()

plt.plot(times,p_insert_,color='r',label='Insert python')
plt.plot(times,c_insert_,color='b',label='Insert c++')
plt.plot(times,j_insert_,color='y',label='Insert java')
plt.legend(title='Insertion Sort')
plt.savefig("Insertion_Sort_Comparasion.png")
plt.clf()

plt.plot(times,p_count_,color='r',label='Counting python')
plt.plot(times,c_count_,color='b',label='Counting c++')
plt.plot(times,j_count_,color='y',label='Counting java')
plt.legend(title='Counting Sort')
plt.savefig("Counting_Sort_Comparasion.png")
plt.clf()

plt.plot(times,p_merge_,color='r',label='Merge python')
plt.plot(times,c_merge_,color='b',label='Merge c++')
plt.plot(times,j_merge_,color='y',label='Merge java')
plt.legend(title='Merge Sort')
plt.savefig("Merge_Sort_Comparasion.png")
plt.clf()

plt.plot(times,p_quick_,color='r',label='Quick python')
plt.plot(times,c_quick_,color='b',label='Quick c++')
plt.plot(times,j_quick_,color='y',label='Quick java')
plt.legend(title='Quick Sort')
plt.savefig("Quick_Sort_Comparasion.png")
plt.clf()

plt.plot(times,p_selec_,color='r',label='Selection python')
plt.plot(times,c_selec_,color='b',label='Selection c++')
plt.plot(times,j_selec_,color='y',label='Selection java')
plt.legend(title='Selection Sort')
plt.savefig("Selection_Sort_Comparasion.png")
plt.clf()

plt.plot(times,p_heap_,color='r',label='Heap python')
plt.plot(times,c_heap_,color='b',label='Heap c++')
plt.plot(times,j_heap_,color='y',label='Heap java')
plt.legend(title='Heap Sort')
plt.savefig("Heap_Sort_Comparasion.png")
plt.clf()

plt.plot(times,p_bubble_,label='Bubble Sort')
plt.plot(times,p_insert_,label='Insert Sort')
plt.plot(times,p_selec_,label='Selection Sort')
plt.plot(times,p_count_,label='Counting Sort')
plt.plot(times,p_merge_,label='Merge Sort')
plt.plot(times,p_quick_,label='Quick Sort')
plt.plot(times,p_heap_,label='Heap Sort')
plt.legend(title='Algoritmos en Python')
plt.savefig("Python_all.png")
plt.clf()

plt.plot(times,j_bubble_,label='Bubble Sort')
plt.plot(times,j_insert_,label='Insert Sort')
plt.plot(times,j_selec_,label='Selection Sort')
plt.plot(times,j_count_,label='Counting Sort')
plt.plot(times,j_merge_,label='Merge Sort')
plt.plot(times,j_quick_,label='Quick Sort')
plt.plot(times,j_heap_,label='Heap Sort')
plt.legend(title='Algoritmos en Java')
plt.savefig("Java_all.png")
plt.clf()

plt.plot(times,c_bubble_,label='Bubble Sort')
plt.plot(times,c_insert_,label='Insert Sort')
plt.plot(times,c_selec_,label='Selection Sort')
plt.plot(times,c_count_,label='Counting Sort')
plt.plot(times,c_merge_,label='Merge Sort')
plt.plot(times,c_quick_,label='Quick Sort')
plt.plot(times,c_heap_,label='Heap Sort')
plt.legend(title='Algoritmos en C++')
plt.savefig("C++_all.png")
plt.clf()
