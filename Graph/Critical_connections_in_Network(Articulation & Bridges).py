class Solution:
    def build_graph(self,edges,n):
        graph = {}
        for i in range(n):
            graph[i] = list()
            
        for edge in edges:
            parent = edge[0]
            child = edge[1]
            
            graph[parent].append(child)
            graph[child].append(parent)
            
        return graph
    
    def dfs(self,node,parent,timer):
        self.visited[node] = True
        self.discover_time[node] = timer
        self.lowest_time[node] = timer
        timer += 1
        
        for nbr in self.graph[node]:
            if nbr == parent:
                continue
            
            elif self.visited[nbr] is False:
                self.dfs(nbr,node,timer)
                self.lowest_time[node] = min(self.lowest_time[node],self.lowest_time[nbr]) 
                if self.lowest_time[nbr] > self.discover_time[node]:
                    self.bridges.append([node,nbr])
            
            else:
                self.lowest_time[node] = min(self.lowest_time[node],self.discover_time[nbr])
            
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.visited = [False]*(n)
        self.discover_time = [0]*(n)
        self.lowest_time = [0]*(n)
        
        self.bridges = []
        
        self.graph = self.build_graph(connections,n)
        timer = 0
        
        for node in range(n):
            if self.visited[node] is False:
                self.dfs(node,-1,timer)
        
        return self.bridges
