#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#
def build_graph(cities, n):
    graph = {}
    for i in range(1,n+1):
        graph[i] = list()
        
    for city in cities:
        parent = city[0]
        child = city[1]
        
        graph[parent].append(child)
        graph[child].append(parent)
        
    return graph
    
def dfs(graph,vertex,visited,node_count):
    visited[vertex] = True
    node_count += 1
    
    for nbr in graph[vertex]:
        if visited[nbr] is False:
            node_count = dfs(graph,nbr,visited,node_count)
            
    return node_count
    
def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    if c_road > c_lib:
        return c_lib*(n)

    visited = [False]*(n+1)
    graph = build_graph(cities, n)
    l = []
    components = 0
    
    for vertex in range(1,n+1):
        if visited[vertex] is False:
            node_count = 0
            nodes = dfs(graph,vertex,visited,node_count)
            components += 1
            l.append(nodes)
            
    total = 0
    for ele in l:
        total = total + (c_road*(ele-1))
        
    total = total + (components*c_lib)
    
    return total
    
    #print(cities)
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
