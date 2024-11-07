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
    def bfs(self, src):
        que = []
        visited = [False] * len(self.adj_list)
        visited[src] = True
        que.append(src)
        path = []

        while que:
            print(f"{que}, {visited}", end ="-> ")
            curr = que.pop(0)
            path.append(curr)

            for node in self.adj_list[curr]:
                if not visited[node]:
                    visited[node] = True
                    que.append(node)
        print()
        for node in path:
            print(node, end =" ")
        print()

if __name__ == "__main__":
        V = 5

        usr_graph = Graph(V)
        usr_graph.add_edge(0, 1)
        usr_graph.add_edge(0, 2)
        usr_graph.add_edge(1, 3)
        usr_graph.add_edge(1, 4)
        usr_graph.add_edge(2, 4)
        print(usr_graph.display_adj_mat())
        print(usr_graph.display_adj_list())
        usr_graph.bfs(0)





