def print_header(seq):# function for printing the header with a certian spacing
    string ="_"
    print(f"{string:5}",end="")
    for c in seq:
        print(f"{c:5}", end="")
    print()

def initiliaze_arr(arr, gap): # Function for intilazing the scoring matrix/array
    for i in range(1,len(arr[0])):
            arr[0][i] = arr[0][i-1] + gap

    for i in range(1,len(arr)):
            arr[i][0] = arr[i-1][0] + gap
   
def print_matrix(seq1,seq2, arr): #Function for pringing the matrix out
    print_header(seq1)
    for i,item in enumerate(arr):
        print(f"{seq2[i]}", end="")
        for obj in item:
            width = 5
            print(f"{obj:>{width}}",end="")
        print()
    print()

def charArr(string): # Function for converting a string to a char array in python since strings are not just char arrays for some reason
    return [c for c in string]

def score(char1, char2, gap, match, mismatch): #Score finde for the diagonal case
    if char1 == char2:
        return match 
    elif char1 == "_" or char2== "_":
        return  gap
    return mismatch

def print_all_alingments(i, j, arr, seq1, seq2, mismatch, gap, match, alignA, alignB, align_score,alignments): # Recursive function for finding all optimal alignments 
    i = i
    j = j
    while(i>0 and j>0):
        if(i>0 and j>0 and arr[i][j] == arr[i-1][j-1] + score(seq1[j], seq2[i], gap, match, mismatch)):
            cp_alignA = alignA.copy()
            cp_alignB = alignB.copy()
            cp_alignA.insert(0,seq2[i])
            cp_alignB.insert(0,seq1[j])
            tmpi = i-1
            tmpj = j-1
            print_all_alingments(tmpi,tmpj, arr, seq1, seq2, mismatch, gap, match, cp_alignA, cp_alignB, align_score,alignments)
            
        if(i>0 and arr[i][j] == arr[i-1][j]+gap):
            cp_alignA = alignA.copy()
            cp_alignB = alignB.copy()
            cp_alignA.insert(0,seq2[i])
            cp_alignB.insert(0,"_")
            tmpi = i-1
            print_all_alingments(tmpi,j, arr, seq1, seq2, mismatch, gap, match, cp_alignA, cp_alignB, align_score,alignments)
        if(j>0 and arr[i][j] == arr[i][j-1]+gap):
            cp_alignA = alignA.copy()
            cp_alignB = alignB.copy()
            cp_alignA.insert(0,"_")
            cp_alignB.insert(0,seq1[j])
            tmpj = j - 1
            print_all_alingments(i,tmpj, arr, seq1, seq2, mismatch, gap, match, cp_alignA, cp_alignB, align_score,alignments)
        break
    if i==0 and j==0:
        if len(alignments) > 0:
            align_1 = "".join(alignA)
            align_2 = "".join(alignB)
            matches = 0
            for items in alignments:
                if align_1 == items[0] and align_2 == items[1]:
                    matches += 1
            if matches == 0:
                alignments.append([align_1,align_2])
        else: 
            alignments.append(["".join(alignA), "".join(alignB)])

def optimal_algingment(match, mismatch, gap, seq1, seq2): #Optimal alignment algorithim 
    try:
        index = seq1.index("_")
        seq1.pop(index)
        seq1.insert(0,"_")
    except:
        seq1.insert(0,"_")
    try:
        index = seq2.index("_")
        seq2.pop(index)
        seq2.insert(0,"_")
    except:
        seq2.insert(0,"_")       

    arr = [[0 for i in range(len(seq1))] for i in range(len(seq2))]
    print(len(arr))

    initiliaze_arr(arr, gap)
    print_matrix(seq1,seq2, arr)
    traceback = [[str(obj) for obj in item] for item in arr]
    for i in range(1,len(arr)):
        for j in range(1, len(arr[i])):
            diagonal = arr[i-1][j-1] + score(seq1[j], seq2[i], gap, match, mismatch)
            top = arr[i-1][j]+gap
            left = arr[i][j-1]+gap
            values = [diagonal, top, left]
            max_val = max(values)
            arr[i][j] = max_val
            item = charArr(str(max_val))
            if diagonal == max_val:
                item.insert(0,"⭦")
            if top == max_val:
                item.insert(0,"⭡")
            if left == max_val:
                item.insert(0,"⭠ ")


            item = "".join(item)
            traceback[i][j] = item
    print_matrix(seq1,seq2,traceback)
    alignments = []
    print_all_alingments(len(seq2)-1, len(seq1)-1, arr, seq1, seq2, mismatch, gap, match, [], [], arr[-1][-1], alignments)
    return (alignments, arr[-1][-1])


    
def print_alignments(alignments, total_score): # Print the alignments out 
    print(f"The maxium score for these sequnces is {total_score} for the following alignments: ")
    for alignA, alignB in alignments:
        print(alignA)
        print(alignB)
        print()
    

def enterNumber(string): # utils function for getting number input from a user
    flag = True
    while flag:
        try:
            num = int(input(string))
            flag = False
            return num
        except ValueError:
            print("\nPlease enter in a number")
def enterChar(): # utils function for getting char input from a user 
    flag = True
    while flag:
        try:
            character = input("Please enter in another character: ")[0].upper()
            flag = False
            return character
        except ValueError:
            print("Please enter in one character")


def enterSequence(): # Enter sequnce method to ensure the uisercan send a sequnce of any size
    flag = True 
    seq = []
    while flag:
        character = enterChar()
        seq.append(character)
        cont = input("Do you wish to continue Y/N: ")
        if cont.lower() != "y":
            flag = False
            break

    return seq
        
        

        

    
if  __name__ == "__main__": # Actual main of the program 
    while True:
        gap = enterNumber("Please enter in your gap value: ")
        mismatch = enterNumber("Please enter in your mismatch value: ")
        match = enterNumber("Please enter in your match value: ")
        print("You may now begin filing  in sequence 1")
        seq1 = enterSequence()
        print("You may now begin filing in sequence 2")
        seq2 = enterSequence()
        print(f"gap = {gap}")
        print(f"mismatch = {mismatch}")
        print(f"match = {match}")

        alignments, total_score = optimal_algingment(match, mismatch, gap, seq1, seq2)
        view_alignments = input("Do you wish to view all alignments Y/N: ")
        if view_alignments.lower() == "y":
            print_alignments(alignments, total_score)
        cont = input("Do you wish to continue Y/N: ")

        if cont.lower() != "y":
            print("Thank you for using this program")
            break 





