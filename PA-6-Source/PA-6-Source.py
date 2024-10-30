def print_header(seq):
    string ="_"
    print(f"{string:5}",end="")
    for c in seq:
        print(f"{c:5}", end="")
    print()

def initiliaze_arr(arr, gap):
    for i in range(1,len(arr[0])):
            arr[0][i] = arr[0][i-1] + gap

    for i in range(1,len(arr)):
            arr[i][0] = arr[i-1][0] + gap
   
def print_matrix(seq1,seq2, arr):
    print_header(seq1)
    for i,item in enumerate(arr):
        print(f"{seq2[i]}", end="")
        for obj in item:
            width = 5
            print(f"{obj:>{width}}",end="")
        print()
    print()

def charArr(string):
    return [c for c in string]

def cell_allignment(char1, char2, gap, match, mismatch):
    if char1 == char2:
        return match 
    elif char1 == "_" or char2== "_":
        return  gap
    return mismatch

def optimal_algingment(match, mismatch, gap, seq1, seq2):
    seq1.insert(0,'_')
    seq2.insert(0,'_')

    arr = [[0 for i in range(len(seq1))] for i in range(len(seq2))]
    print(len(arr))

    initiliaze_arr(arr, gap)
    print_matrix(seq1,seq2, arr)
    traceback = [[str(obj) for obj in item] for item in arr]
    for i in range(1,len(arr)):
        for j in range(1, len(arr[i])):
            diagonal = arr[i-1][j-1] + cell_allignment(seq1[j], seq2[i], gap, match, mismatch)
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
        


    
    
if  __name__ == "__main__":
    gap = -1
    mismatch = -1
    match = 1
    seq1 = ["G", "C", "A", "T", "G", "C", "G"]
    seq2 = ["G","A","T", "T", "A", "C", "A"]
    optimal_algingment(match, mismatch, gap, seq1, seq2)



