from matplotlib import pyplot as plt
from time import time
from bubbleSort import *
arr = [56,21,1,89,99,50]
start = time()
bubbleSort(arr)
total = time() - start