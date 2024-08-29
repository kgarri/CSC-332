#Keith Garri J00689732, August 28, 2024
import time as time
import random as random
from  statistics import mean,median 
import os as os


class gcfInfo(): #the gcf info class exists so the data struct is easy to recall later and print
    def __init__(self,num1,num2,gcf,time):
        self.num1 = num1
        self.num2 = num2
        self.gcf = gcf
        self.time = secondsToMilliSeconds(time)

    def toString(self): #toString method
        return (str(self.num1) +', '+ str(self.num2) +', '+ str(self.gcf)+', '+ str(self.time))
    

    
def bruteForceAlgV1(a,b): #brute force Alg version 1 going upwards till you hit the smaller of the two numbers
    gcf = 0
    if a<b:
        start = time.time()
        for i in range(1,a+1):
            if(b%i==0 and a%i==0): 
                gcf=i
    else:
        start = time.time()
        for i in range(1,b+1):
            if(b%i==0 and a%i==0): 
                gcf=i
    end = time.time()
    return(end-start,gcf)

def bruteForceAlgV2(a,b): #brute force Alg version 2 going downwards till it devides by 1
    gcf = 0
    if a<b:
        start = time.time()
        for i in range(a,1,-1):
            if(b%i==0 and a%i==0): 
                gcf=i
                break
        
    else:
        start = time.time()
        for i in range(b, 1, -1):
            if(b%i==0 and a%i==0): 
                gcf=i
                break
    if gcf == 0:
        gcf = 1
    end = time.time()
    return(end-start,gcf)

def orginaleEculidsAlg(a,b): #The first version of the eculids alg
    r=1 # in python you have to declare a variable before using it in a loop
    start = time.time()
    while r !=0:
        r = a - a/b*b
        a=b 
        b=r
    end = time.time()
    return(end-start, a)

def secEculidsAlg(a,b): #the second version of the eculids alg
    r = 1 # in python you have to declare a variable before using it in a loop
    start = time.time()
    while r !=0:
        r = a - b
        if r>=b:
            r=r-b
            if r>=b:
                r=r-b
                if r>=b:
                    r = a-b *a/b
        a=b 
        b=r
    end = time.time()
    return(end-start, a)

def eculidsAlgRecursive(a,b): # a recursive version of eculids alg
    if (a == 0):
        return(b)
    return(eculidsAlgRecursive(b%a, a))

def secondsToMilliSeconds(seconds): # function to convert time from seconds to milliseconds
    return (seconds/pow(10,-3))


    
def saveToFile(filename,arr,header): # the spreadsheet saving file
    try:
        os.remove(filename)
    except OSError:
        print("File doesn't exist")
    with open(filename,'a') as f:
        f.write(header)
        f.write("\n".join([item.toString() for item in arr]))

class stats(): # stats class used to calculate the stats and save them
    def __init__(self,objects):
        self.objects= objects

    def toString(self):
        arr = []
        arr.append("Maximum Time, " + str(max([item.time for item in self.objects])))
        arr.append("Minimum Time, " + str(min([item.time for item in self.objects])))
        arr.append("Average Time, " + str(mean([item.time for item in self.objects])))
        arr.append("Median Time, " + str(median([item.time for item in self.objects])))
        return('\n'.join(arr))
    
def objectCompairisons(objectarr1, objectarr2): # comparision function to compare the diffrent versions of euclids alg
    # we know that the order of objects will be the same no matter what do to how the orginal for loop is structured this is backed up by the file outputs
    arr = []
    diffarr = []
    for i in range(len(objectarr1)):
        if (objectarr1[i].time < objectarr2[i].time):
            arr.append(objectarr1[i])
            diffarr.append(objectarr2[i].time -objectarr1[i].time)
        if len(diffarr)<1:
            return(len(arr),0)
    return(len(arr), mean(diffarr))

def createConclusionsTxt(brute1, brute2, euclids1, euclids2): # function for creating conclussions.txt
    try:
        os.remove("Conclusions.txt")
    except OSError:
        print("File doesn't exist")

    with open("Conclusions.txt",'a') as f:
        com1, av1 = objectCompairisons(brute2,brute1)
        com2, av2 = objectCompairisons(euclids1,brute1)
        com3, av3 = objectCompairisons(euclids1,brute2)
        com4, av4 = objectCompairisons(euclids2,euclids1)
        com5, av5 = objectCompairisons(euclids2,brute1)
        com6, av6 = objectCompairisons(euclids2,brute2arr)
        f.write(f'(1)	Out of 1,000 pairs of integers, brute-force (v2) outperformed brute-force (v1) in {com1} pairs; and the average saved time for these pairs of integers was {av1} milliseconds.\n'+
             f"(2)	Out of 1,000 pairs of integers, the original version of Euclid outperformed brute-force (v1) in {com2} pairs; and the average saved time for these pairs of integers was {av2} milliseconds.\n"+
             f"(3)	Out of 1,000 pairs of integers, the original version of Euclid outperformed brute-force (v2) in {com3} pairs; and the average saved time for these pairs of integers was {av3} milliseconds.\n" +
             f"(4)	Out of 1,000 pairs of integers, the second version of Euclid outperformed the original version of Euclid in {com4} pairs; and the average saved time for these pairs of integers was {av4} milliseconds.\n"+
             f"(5)	Out of 1,000 pairs of integers, the second version of Euclid outperformed brute-force (v1) in {com5} pairs; and the average saved time for these x2 pairs of integers was {av5} milliseconds.\n"+
             f"(6)	Out of 1,000 pairs of integers, the second version of Euclid outperformed brute-force (v2) in {com6} pairs; and the average saved time for these x3 pairs of integers was {av6} milliseconds.\n")

        
        


        

    

if __name__ == "__main__": #Main for the project
    #results arrays
    brute1arr = []
    brute2arr = []
    eculid1arr = []
    eculid2arr = []
    eculid3arr = []
    #File Headers as consts
    HEADER1 = "Number One, Number Two, Their GCD, Time Spent(Milliseconds)\n"
    HEADER2 = "Statistics, Milliseconds\n"
    #seed for the random number gen
    seed = time.time()
    random.seed(seed)
    # For loop of 1000
    for i in range(1000): 
        #randint from 0,100000
        a = random.randint(0,100000) 
        b = random.randint(0,100000)

        #function calls for burteForceAlgV1
        algtime, gcf = bruteForceAlgV1(a,b)
        brute1arr.append(gcfInfo(a,b,gcf,algtime))

        #function calls for bruteForceAlgV2
        algtime, gcf = bruteForceAlgV2(a,b)
        brute2arr.append(gcfInfo(a,b,gcf,algtime))

        #function calls for first eculid alg
        algtime, gcf = orginaleEculidsAlg(a,b)
        eculid1arr.append(gcfInfo(a,b,gcf,algtime))
        
        #function calls for second eculids alg
        algtime, gcf = secEculidsAlg(a,b)
        eculid2arr.append(gcfInfo(a,b,gcf,algtime))

        #function calls for recursive eculids alg 
        start = time.time()
        gcf = eculidsAlgRecursive(a,b)
        algtime = time.time() - start
        eculid3arr.append(gcfInfo(a,b,gcf,algtime))

    #saveToFile Function Calls
    saveToFile("BF_v1_Results.csv",brute1arr,HEADER1)
    saveToFile("BF_v1_Statistics.csv", [stats(brute1arr)],HEADER2)

    saveToFile("BF_v2_Results.csv",brute2arr,HEADER1)
    saveToFile("BF_v2_Statistics.csv", [stats(brute2arr)],HEADER2)

    saveToFile("OE_Results.csv", eculid3arr,HEADER1)
    saveToFile("OE_Statistics.csv", [stats(eculid3arr)],HEADER2)

    saveToFile("RE_Results.csv", eculid3arr,HEADER1)
    saveToFile("RE_Statistics.csv", [stats(eculid3arr)],HEADER2)

    saveToFile("SE_Results.csv", eculid3arr,HEADER1)
    saveToFile("SE_Statistics.csv", [stats(eculid3arr)],HEADER2)

    #Function call conclussions.txt
    createConclusionsTxt(brute1arr,brute2arr,eculid1arr,eculid2arr)

    
        
