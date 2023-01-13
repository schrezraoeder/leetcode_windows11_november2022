# from a coaching session 
# i did need assistance & it took too long 

from collections import deque 

class Solution:
    def in_bounds(self, location, direction, grid):
        return 0 <= (location[0] + direction[0]) < len(grid) and 0 <= (location[1] + direction[1]) < len(grid[0])
    
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        queue = deque() 
        visited = set() 
        for ix, row in enumerate(grid):
            for jx, column in enumerate(row): 
                if grid[ix][jx] == 1: # add all the sources to the queue since it is multi-source BFS 
                    queue.append((ix, jx)) 
                    visited.add((ix, jx)) 
        if len(visited) == len(grid) * len(grid[0]):
            return -1 

        distance = -1 # level of the multi-source BFS 
        up = [-1, 0] 
        down = [1, 0] 
        right = [0, 1] 
        left = [0, -1] 
        directions = [up, down, right, left] 
        while queue: 
            size = len(queue) # how many nodes are in the current level 
            for _ in range(size):
                node = queue.popleft() 
                for direction in directions: 
                    next_node = (node[0] + direction[0], node[1] + direction[1])
                    if self.in_bounds(node, direction, grid) and next_node not in visited: 
                        queue.append(next_node)
                        visited.add(next_node) 
            distance +=1
        return distance 
        
        