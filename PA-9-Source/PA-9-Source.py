def print_list_spaced(arr):
    for item in arr:
        print(f"{str(item):<5}",end=" ")
    print()

class Node(): 
    def __init__(self, lt, number):
        self.lt = lt 
        self.number = number

class Graph():
    def __init__(self, Verticies):
        self.adj_mat = [[0] * Verticies for _ in range(Verticies)]
        self.adj_list = [[] for _ in range(Verticies)]
        self.adj_list_trans = [[] for _ in range(Verticies)]
    def add_edge(self,i,j):
        self.adj_mat[i][j] = 1

        self.adj_list[i].append(j)
        self.adj_list_trans[j].append(i)

    def display_adj_mat(self):
        for arr in self.adj_mat:
            print(arr)

    def display_adj_list(self):
        for i in range(len(self.adj_list)):
            print(f"{i}: ", end="")
            for j in self.adj_list[i]: 
                print(j, end=" ")
            print()

    def print_dfs(self): 
        color = "color"
        predecessor = "predecessor"
        first_time = "first time"
        last_time = "last_time"
        space= ""
        print(f"{space: <11}", end =" ")
        for V in range(len(self.adj_list)):
            print(f"{str(V):<5}", end=" ")
        print()
        print(f"{color:<11}", end =" ")
        print_list_spaced(self.color)
        print(f"{predecessor:<11}", end=" ")
        print_list_spaced(self.pred)
        print(f"{first_time: <11}", end =" ")
        print_list_spaced(self.first_time)
        print(f"{last_time: <11}", end = " ") 
        print_list_spaced(self.last_time)
        print()


    def dfs_visit(self,v): 
        self.color[v] = 'grey'
        self.first_time[v] = self.time 
        self.time +=1
        for V in self.adj_list[v]:
            if self.color[V] == 'white':
                self.pred[V] = v
                self.dfs_visit(V)
        self.color[v]= 'black'
        self.last_time[v] = self.time
        self.lt_nodes[v] = Node(self.time, v)
        self.time +=1
        self.print_dfs()
        return

    def dfs(self):
        self.color = ['white'] * len(self.adj_list)
        self.pred = [None] * len(self.adj_list)
        self.first_time = [0]* len(self.adj_list)
        self.last_time = [0] * len(self.adj_list)
        self.lt_nodes = [Node(-1,-1)]* len(self.adj_list)
        self.time = 0 
        for v in range(len(self.adj_list)):
            if(self.color[v] == 'white'):
                self.dfs_visit(v)

    def scc_vist(self, src):
        self.color_trans[src] = 'grey'
        print(f"{src} -> ", end ="")
        for V in self.adj_list_trans[src]:
            if self.color_trans[V] == 'white':
                self.pred_trans[V] = src 
                self.scc_vist(V)
        self.color_trans[src] = 'black'
        return 
        
    def scc(self):
        self.dfs()
        self.lt_nodes.sort(key = lambda x: x.lt, reverse = True)
        self.color_trans  = ['white'] * len(self.adj_list_trans)
        self.pred_trans   = [None] * len(self.adj_list_trans)
        
        for node in self.lt_nodes:
            if self.color_trans[node.number] == 'white':
                print(f"SCC: ", end ="")
                self.scc_vist(node.number)
                print()
            


def enterNumber(string):
    while True:
        try:
            num = int(input(string))
            return num
        except: 
            print("Please enter in a number")
def enterEdge(V):
    print(f"i and j must be between 0-{V}")
    while True:
        try: 
            i, j = input("Please enter in the edge in the following  format i,j: ").split(",")
            if (int(i)>=0 and int(i) <=V) and (int(j)>=0 and int(j)<=V):
                return(int(i), int(j))
            raise ValueError("i or j is out of range")

        except ValueError as e:
            print("An error occurred: ",e)


if __name__ == "__main__":
    print("Welcome to the Graph CLI <3")
    while True: 
        V = enterNumber("Please enter in the number of nodes in the Graph: ")
        E = enterNumber("Please enter in the number of edges in the Graph: ")
        usr_graph = Graph(V)
        for _ in range(E):
            i,j = enterEdge(V-1)
            usr_graph.add_edge(i,j)

        usr_graph.display_adj_mat()
        usr_graph.display_adj_list()
        usr_graph.scc() 

        stop = input("Do you wish to continue [Y/N]: ").lower()

        if stop != "y":
            break











