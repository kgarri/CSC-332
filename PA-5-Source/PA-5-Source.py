import time as time 
from itertools import combinations

#This is a class that acts like a binary tree structur in the way that each leaf is a diffrent task that the user could chose to do
class Task:
    def __init__(self,profit, task_num, start, end):
        self.profit = profit
        self.task_num = task_num
        self.start = start
        self.end = end

    def __repr__(self): 
        return f"{self.task_num}"

    def __str__(self):
        return f"{self.task_num}, {self.start}, {self.end}, {self.profit}"

    def __eq__ (self,other):
        if not isinstance(other,Task):
            return False
        return self.task_num == other.task_num
    def __hash__(self):
        return hash((self.task_num, self.start, self.end, self.profit))

    #Sets the task to point to a previus task
    def setPrevTask(self,prev_task):
        self.prev_task = prev_task 

    #Sets the task to point to a task that precedes it in duration
    def setPrevMax(self, max):
        self.prev_max = max

    def isInPath(self,val):
        self.path = val

    def hasAnAltPath(self,val):
        self.alt_path = val

    def setAsLast(self,val):
        self.last = val

    def getMaxPaths(self, path, paths):
        path.append(self)
        if self.path == False:
            path.pop()
            self.prev_task.getMaxPaths(path, paths)
        elif self.prev_max != None:
            self.prev_max.getMaxPaths(path, paths)
            path.pop()
        else:
            paths.append(list(path))
            path.pop()
            return
        if self.alt_path:
            self.prev_task.getMaxPaths(path, paths)
        

#this comes from PA-2-Source.py
def merge(L,R): #merge function used to merge two arrays in order
    n1 = len(L) #maxProfitium length of the left array 
    n2 = len(R)#maxProfitium length of the right array 
    arr = []

    i = 0
    j= 0
    while i<n1 and j<n2:
        if L[i].end <= R[j].end:
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

def binary_search(arr, x):
    mid = 0
    low = 0
    high = len(arr)
    while low<=high:
        mid = low + (high -low) //2

        if arr[mid].end == x:
            return mid

        elif arr[mid].end< x:
            low=mid+1

        else: 
            high = mid-1

    while (mid > -1 and arr[mid].end>x):
        mid -=1

    if (arr[mid].end < x): 
        return mid

    return -1
# this is brute force as it still goes through every possible solution in the end, not using max as there is other things that need to happen in order to print out the task list
def maxProfitRecBF(task):  
    if task.prev_max != None: 
        currprofit = maxProfitRecBF(task.prev_max) + task.profit
    else:
        currprofit = task.profit
    if task.prev_task !=None:
        prevprofit = maxProfitRecBF(task.prev_task)
    else: 
        prevprofit = 0
    if currprofit > prevprofit:
        task.isInPath(True) #This is used for printing
        task.hasAnAltPath(False) #This is used for printing as well
        return currprofit
    elif currprofit == prevprofit:
        task.hasAnAltPath(True)
        task.isInPath(True)
        return currprofit
    else:
        task.isInPath(False) 
        task.hasAnAltPath(False)
        return prevprofit

#the arr acts as a cache bypassing calculating all the subproblems
def maxProfitRecDyn(task,arr=[]):
    if task.prev_max != None:
        if task.prev_max.task_num in arr:
            currprofit = arr[task.prev_max.task_num] + task.profit
        else:
            currprofit = maxProfitRecBF(task.prev_max) + task.profit
    else:
        currprofit = task.profit

    if task.prev_task !=None:
        if task.prev_task.task_num in arr:
            prevprofit = arr[task.prev_task.task_num]
        else:
            prevprofit = maxProfitRecBF(task.prev_task)
    else: 
        prevprofit = 0

    if currprofit > prevprofit:
        task.isInPath(True)
        task.hasAnAltPath(False)
        arr.append(currprofit)
        return currprofit
    elif currprofit == prevprofit:
        task.hasAnAltPath(True)
        task.isInPath(True)
        arr.append(currprofit)
        return currprofit
    else:
        task.isInPath(False) 
        task.hasAnAltPath(False)
        arr.append(currprofit)
        return prevprofit

#Dynamic algorithim for finding the max profit, this works because all you are worrying about is the final profit solution
def dynMaxProfit(arr):
    solution = [0]
    for i,task in enumerate(arr):
        solution.append(max(task.profit + solution[task.prev_max.task_num if task.prev_max != None else 0], solution[i]))
    return solution[-1]

#prints the tasks to a chart
def printTaskChart(arr):
    print("\nTask Number, Start Time, End Time, Cost")
    for task in arr:
        print(str(task))

#used to find the previous tasks, and have them prelinked in order to take advantage of the task data structure 
def linkTasks(task_arr):
    for i,task in enumerate(task_arr):
        task.task_num = i+1
        if i == 0: 
            task.setPrevTask(None)
            task.setPrevMax(None)
        else:
            task.setPrevTask(task_arr[i-1])
            task.setPrevMax(None if binary_search(task_arr,task.start) == -1 else task_arr[binary_search(task_arr, task.start)])
        
#genric enternumber string used in order to catch any erronious inputs
def enterNumber(string):
    flag = True
    while flag:
        try:
            num = int(input(string))
            flag = False
            return num
        except ValueError:
            print("\nPlease enter in a number")

#A variable args function used in order to allow the user the ability to time any function they desire
def timeit(func,*argv):
    start = time.process_time_ns()
    val = func(*argv)
    end = (time.process_time_ns() - start)*pow(10,-6)
    return (end, val)



#No_overlap is making sure that the actual subsets have no_overlap over the times
def no_overlap(subset):
    sorted_tasks = sorted(subset, key=lambda t: t.start)
    for i in range(1, len(sorted_tasks)):
        if sorted_tasks[i-1].end > sorted_tasks[i].start:
            return False
    return True

#Checks to see if a subset is a subset of another subset just to make sure they all work
def is_legitimate(subset, all_subsets):
    for other in all_subsets:
        if subset != other and subset.issubset(other):
            return False
    return True

#Start of the main loop of control
if __name__ == '__main__':
    print("Welcome to the task scheduler CLI Program, hope you enjoy :).")
    nothing = input("Press any key to continue")
    
    #This is the main loop of the function itself that controls the CLI
    while True:
        n = enterNumber("Enter in the total number n of paid tasks: ")
        task_arr=[]

        assert n is not None # this is making sure that n the number recived from the user is not nothing, else the program will through an error for the user  
        for i in range(n):
            flag = True
            start_time = enterNumber("\nPlease enter in a start time for this task: ")
            end_time = enterNumber("Please enter in a end time for this task: ")
            profit =  enterNumber("Please enter in a profit associated with this task: ")
            tmp = Task(profit=profit, task_num = 0, start = start_time, end = end_time)
            task_arr.append(tmp)

        #Mergesort of the array that way the tasks are poroperly sorted by end time
        task_arr =  mergesort(task_arr)
        
        #Links together the tasks in order to take advantage of the task data structure
        linkTasks(task_arr)

        arr = []
        
        printTaskChart(task_arr) 

        rec_time_bf,max_profit =timeit(maxProfitRecBF,task_arr[-1])
        rec_time_dyn,max_profit_recdyn = timeit(maxProfitRecDyn,task_arr[-1],arr )
        dyn_time ,dyn_maxprofit = timeit(dynMaxProfit, task_arr)

        print(f"\nThe time elapsed in the brute-force algorithm is {rec_time_bf} ms and value is {max_profit}")
        print(f"The time elapsed in the recursive DP algorithm is {rec_time_dyn} ms and value is {max_profit_recdyn}")
        print(f"The time elapsed in the non-recursive DP algorithm is {dyn_time} ms and value is {dyn_maxprofit}")

        #This function is used to get all the possible max paths a task has
        paths = []
        task_arr[-1].getMaxPaths([],paths)
        
        #printing out of the tasks
        for path in paths:
            path.reverse()
            for task in path:
                print(f"Task_{task.task_num}->",end="")
            print(f"with a total earning of {max_profit}")

        # start of set wizardry and combinations, since we are taking advantage of pythons iter libary and sets being  able to auto filter out types that don't belong in them
        all_subsets = [set(comb) for i in range(1, len(task_arr)+1) for comb in combinations(task_arr, i)] #getting all possible sets of tasks

        valid_subsets = [subset for subset in all_subsets if no_overlap(subset)] # making sure to only keep valid sets, i.e sets that don't share an overlap in terms of task scheduling, no two tasks running at the same time

        legitimate_sets = [subset for subset in valid_subsets if is_legitimate(subset, valid_subsets)] #only keeping the legitmate_sets really the ones that aren't a subset of others so the last item in the set doesn't have a task it could go to and the first item isn't preceded by another item

       #print out the total earnings like the recuirments said too 
        print(f"\nThere are {len(legitimate_sets)} obtions to select different sets of tasks.")
        for i, subset in enumerate(legitimate_sets, 1):
            total_earning = sum(task.profit for task in subset)

            subset = list(subset)# sets are not ordered in python so you have to order them by converting them to a list
            sorted_tasks= mergesort(subset) # running the same mergesort again 
            print(f"Option {i}: {' -> '.join(f"Task_{task.task_num}" for task in sorted_tasks)}, with a total earning of {total_earning}") #printing them out using list compressionm

        cont = input("Do you wish to cont [y/n]: ")
        
        if cont.lower() != 'y':
            break



    

       

