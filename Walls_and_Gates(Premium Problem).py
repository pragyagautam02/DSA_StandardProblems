from typing import (
    List,
)
from collections import deque
import math

class Node:
    def __init__(self,x,y,time):
        self.x=x
        self.y=y
        self.time=time

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, grid: List[List[int]]):
        # write your code here
        empty=2147483647

        row=len(grid)
        cols=len(grid[0])
        queue=deque()

        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 0:
                    node = Node(i,j,0)
                    queue.append(node)

        while(queue):
            curr_node = queue.popleft()
            x=curr_node.x
            y=curr_node.y
            time=curr_node.time

            if x-1>=0 and grid[x-1][y]==empty:
                grid[x-1][y] = time+1
                node=Node(x-1,y,time+1)
                queue.append(node)

            if x+1<row and grid[x+1][y]==empty:
                grid[x+1][y] = time+1
                node=Node(x+1,y,time+1)
                queue.append(node)
            
            if y-1>=0 and grid[x][y-1]==empty:
                grid[x][y-1] = time+1
                node=Node(x,y-1,time+1)
                queue.append(node)

            if y+1<cols and grid[x][y+1]==empty:
                grid[x][y+1] = time+1
                node=Node(x,y+1,time+1)
                queue.append(node)
