from collections import deque 
# thoughts from a software engineering coaching session I had last night 
'''
grid = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
]
Output: -1

Input: grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
    ]

curr_level = [tuple1, tuple2, tuple3, tuple4]
next_level =  []

while data_struct:
    1. pop the node/evaluated the node 
    2. node operation 
    3. node traversal 
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def no_fresh_oranges(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return False 
            return True 
        
        def in_bounds(node, direction):
            return ((0 <= node[0] + direction[0] < len(grid)) and (0 <= node[1] + direction[1] < len(grid[0])))
        
        def plus(node, direction):
            return (node[0] + direction[0], node[1] + direction[1])
        
        def not_visited(node, direction, visited):
            return (plus(node, direction) not in visited) 
        
        
        def four_directional_neighbors(node, visited):
            up = (0, -1)
            down = (0, 1) 
            left = (-1, 0) 
            right = (1, 0) 
            canonical_directions = [up, down, left, right] 
            canonical_neighbors = [] 
            for direction in canonical_directions: 
                if in_bounds(node, direction) and not_visited(node, direction, visited): 
                    neighbor = plus(node, direction) 
                    if grid[neighbor[0]][neighbor[1]]: # only if it is non-zero 
                        canonical_neighbors.append(neighbor)
            return canonical_neighbors   
            
        def BFS(queue, grid, visited): #return's timestamp or level an integer 
            # curr_level = queue.pop() 
            timestamp = 0 
            next_level = True
            curr_level = queue 
            #while next_level:
            #next_level = deque() 
            while next_level:
                next_level = deque() 
                while queue:
                    next_node = queue.pop() 
                    grid[next_node[0]][next_node[1]] = 2 
                    neighbors = four_directional_neighbors(next_node, visited) 
                    for neighbor in neighbors: 
                        next_level.append(neighbor) 
                        visited.add(neighbor) 
                queue = next_level 
                if no_fresh_oranges(grid):
                    return timestamp 
                timestamp += 1 
                print (timestamp) 
            return timestamp 

        queue = deque() 
        visited = set() 
        # 1. Find all the 2s (& boolean senintel if any 1s so return 0 if none) & enqueue for BFS level order 
        for i in range(len(grid)): # rows 
            for j in range(len(grid[0])): # columns 
                if grid[i][j] == 2:
                    # enqueue (i, j) 
                    queue.append((i, j)) 
                    visited.add((i, j)) 
        
        if no_fresh_oranges(grid):
            return 0 

        # 2. level order traversal BFS and keep track of the level == timestamp (timestamp will be returned) 
        timestamp = BFS(queue, grid, visited) 

        #3.  if there are still fresh oranges return -1 else return level/timestamp. 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1 
        return timestamp 
        
        
        
        

        
        