class Pragya:
    def build_graph(self,edges,v):
        graph = {}
        for i in range(v):
            graph[i] = list()

        for edge in edges:
            u = edge[0]
            v = edge[1]
            graph[u].append(v)
            graph[v].append(u)

        return graph

    def dfs(self,node,parent,timer):
        self.visited[node] = True
        self.discover_time[node] = timer
        self.lowest_time[node] = timer
        timer += 1
        child = 0

        for nbr in self.graph[node]:
            if nbr == parent:
                continue

            elif self.visited[nbr] is False:
                self.dfs(nbr,node,timer)
                #if child's low time altered, then its parent's low time also needs to be altered
                self.lowest_time[node] = min(self.lowest_time[node], self.lowest_time[nbr])

                #Our Formula to calculate Articulation point b/w u,v
                if self.lowest_time[nbr] >= self.discover_time[node] and parent != -1:
                    self.ap.add(node)

                child += 1

            #BackEdges
            else:
                self.lowest_time[node] = min(self.lowest_time[node], self.discover_time[nbr])

        #if our root node is ap
        if child >= 2 and parent == -1:
            self.ap.add(node)

            
    def find_articulation_points(self,edges,v):
        self.visited = [False]*(v)
        self.discover_time = [0]*(v)
        self.lowest_time = [0]*(v)

        self.ap = set()
        timer = 0
        self.graph = self.build_graph(edges,v)

        for node in range(v):
            if self.visited[node] is False:
                self.dfs(node,-1,timer)

        return self.ap

if __name__ == '__main__':
    edges = [[0,1],[0,2],[1,2],[1,3],[3,4],[3,6],[4,5],[5,6]]
    v = 7
    obj = Pragya()
    ans = obj.find_articulation_points(edges,v)

    print(ans)
    
