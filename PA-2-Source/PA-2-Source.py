import random as rand
import math
import time
import os 

class ArrayStorage(): #class to store the array values and info that we want
    def __init__(self, unsorted, sorted, time):
        self.sorted = sorted
        self.unsorted = unsorted
        self.time = time
        self.n = len(sorted)
        self.log = round(self.n* math.log2(self.n),2)
        self.logtime = float(self.log/time)
    def unsortedToString(self):
        return('\n'.join(self.unsorted))
    def sortedToString(self):
        return('\n'.join(self.sorted))
    def toString(self):
        return(str(self.n) + ', ' + str(self.log) + ', ' + str(self.time) + ', ' + str(math.ceil(self.logtime))+'E'+"+{:e}".format(self.logtime).split('e')[1] +'\n')

def merge(L,R): #merge function used to merge two arrays in order
    n1 = len(L) #maxium length of the left array 
    n2 = len(R)#maxium length of the right array 
    arr = []

    i = 0
    j=0
    while i<n1 and j<n2: #while loop for comparsion between the array sizes
        if L[i] <= R[j]:
            arr.append(L[i])
            i+=1
        else:
            arr.append(R[j])
            j+=1

    arr.extend(L[i:]) #copies the rest of the Left array into the return array
    arr.extend(R[j:]) #copies the rest of the Right array into the return array

    return(arr)

def mergesort(arr): #MergeSort function
    if len(arr) <= 1: #pbase case for recursion
        return (arr)
    mid = len(arr)//2 #find the midpoint of the array
    l=mergesort(arr[:mid])
    r=mergesort(arr[mid:])
    return merge(l,r)

def secondsToNanoSeconds(t): #converts seconds to nanoseconds not used in this version of the program
    return t * pow(10,-9)

def saveToFile( filename, arr, header): #Save to file function
    try:
        os.remove(filename)
    except OSError:
        print("File doesn't exist")
    with open(filename,'a') as f:
        f.write(header+'\n')
        for item in arr:
            f.write(item.toString())


if __name__ == "__main__": #Start of main 
    storage = [] #Array storage, to be used as a way to recall the sorted and unsorted arrays later
    HEADER = "Input size n for Array_i, Value of nlogn, Time Spent nanoseconds, Value of nlogn/time" #Header for the csv file
    filename = "Mergesort_Time.csv"
    for i in range(1,10): #used to start the array creation
        arr = [rand.randint(0,1000) for i in range(i*1000)]
        start = time.perf_counter_ns()
        sortarr = mergesort(arr)
        end = time.perf_counter_ns() - start
        storage.append(ArrayStorage(arr, sortarr, end))
    saveToFile(filename, storage, HEADER)
    
    while True: #userinput loop
        userinput = input("Please enter the interger number 1-9 to access the arrays:")
        try:
            moduserinput = int(userinput) - 1
            if moduserinput>-1 and moduserinput<=8:
                print("Sorted, Unsorted")
                for i in range(len(storage[moduserinput].sorted)):
                    print(storage[moduserinput].sorted[i], storage[moduserinput].unsorted[i])
                userinput=input("Want to access another array: Y/N ")
                if userinput.lower() == 'y':
                    continue
                else: 
                    break
            else: 
                print("User entered a number greater than 9 or less than 1")
        except ValueError:
            print("User inputed a non number")


    

            
