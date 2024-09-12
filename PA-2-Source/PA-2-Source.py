import random as rand
import math
import time
import os 

class ArrayStorage():
    def __init__(self, unsorted, sorted, time):
        self.sorted = sorted
        self.unsorted = unsorted
        self.time = time
        self.n = len(sorted)
        self.log = self.n* math.log2(self.n)
        self.logtime = float(self.log/time)
    def unsortedToString(self):
        return('\n'.join(self.unsorted))
    def sortedToString(self):
        return('\n'.join(self.sorted))
    def toString(self):
        return(str(self.n) + ',' + str(self.log) + ',' + str(self.time) + ',' + "{:e}".format(self.logtime) +'\n')

def merge(L,R):
    n1 = len(L)
    n2 = len(R)
    arr = []

    i = 0
    j=0
    while i<n1 and j<n2:
        if L[i] <= R[j]:
            arr.append(L[i])
            i+=1
        else:
            arr.append(R[j])
            j+=1

    arr.extend(L[i:])
    arr.extend(R[j:])

    return(arr)

def mergesort(arr):
    if len(arr) <= 1:
        return (arr)
    mid = len(arr)//2
    l=mergesort(arr[:mid])
    r=mergesort(arr[mid:])
    return merge(l,r)

def secondsToNanoSeconds(t):
    return t * pow(10,-9)

def saveToFile( filename, arr, header):
    try:
        os.remove(filename)
    except OSError:
        print("File doesn't exist")
    with open(filename,'a') as f:
        f.write(header+'\n')
        for item in arr:
            f.write(item.toString())


if __name__ == "__main__":
    storage = []
    HEADER = "Input size n for Array_i, Value of nlogn, Time Spent nanoseconds, Value of nlogn/time"
    filename = "Mergesort_Time.csv"
    for i in range(1,10):
        arr = [rand.randint(0,1000) for i in range(i*1000)]
        start = time.perf_counter_ns()
        sortarr = mergesort(arr)
        end = time.perf_counter_ns() - start
        storage.append(ArrayStorage(arr, sortarr, end))
    saveToFile(filename, storage, HEADER)
    
    while True: 
        userinput = input("Please enter the interger number 1-9 to access the arrays:")
        moduserinput = int(userinput) - 1
        print("Sorted, Unsorted \n")
        for i in range(len(storage[moduserinput].sorted)):
            print(storage[moduserinput].sorted[i], storage[moduserinput].unsorted[i])
        userinput=input("Want to access another array: Y/N ")

        if userinput.lower() == 'y':
            continue
        else: 
            break
            1


    

            
