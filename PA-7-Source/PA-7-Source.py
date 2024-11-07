def print_list_spaced(arr):
    for item in arr:
        print(f"{str(item):<5}",end=" ")
    print()

class Graph():
    def __init__(self, Verticies):
        self.adj_mat = [[0] * Verticies for _ in range(Verticies)]
        self.adj_list = [[] for _ in range(Verticies)]

    def add_edge(self,i,j):
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1
        
        self.adj_list[i].append(j)
        self.adj_list[j].append(i)

    def display_adj_mat(self):
        for arr in self.adj_mat:
            print(arr)

    def display_adj_list(self):
        for i in range(len(self.adj_list)):
            print(f"{i}: ", end="")
            for j in self.adj_list[i]: 
                print(j, end=" ")
            print()

    def print_tracking(self):
        color = "color"
        distance = "distance"
        space= ""
        print(f"{space: <11}", end =" ")
        for V in range(len(self.adj_list)):
            print(f"{str(V):<5}", end=" ")
        print()
        print(f"{color:<11}", end =" ")
        print_list_spaced(self.visited) 
        print(f"{distance:<11}",end=" ")
        print_list_spaced(self.distance) 
        print(f"predecessor", end=" ")
        print_list_spaced(self.predecessor)
        print()

    def disconnected(self, src):
        self.visited = ["white"] * len(self.adj_list)
        self.predecessor = [None]*len(self.adj_list)
        self.distance = ["INF"]* len(self.adj_list)
        self.distance[src] = 0

        for V in range(len(self.adj_list)):
            if  self.visited[V]=="white":
                self.bfs(V)
        
    def bfs(self, src):
        que = []
        self.visited[src] = "grey"
        que.append(src)

        print(f"Queue: {que}")
        while que:
            curr = que.pop(0)
        
            for node in self.adj_list[curr]:
                if self.visited[node]=="white":
                    self.visited[node] = "grey"
                    self.distance[node] = self.distance[curr] +1 if self.distance[curr]!= "INF" else "INF"
                    self.predecessor[node] = curr
                    que.append(node)
            self.visited[curr] = "black"
            print(f"Queue: {que}")
            self.print_tracking()

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
        for e in range(E):
            i,j = enterEdge(V-1)
            usr_graph.add_edge(i,j)

        usr_graph.display_adj_mat()
        usr_graph.display_adj_list()
        src = enterNumber("Please enter in the source node: ")
        usr_graph.disconnected(src) 

        stop = input("Do you wish to continue [Y/N]: ").lower()

        if stop != "y":
            break





