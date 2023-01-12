from collections import defaultdict 
from collections import deque 

# Note: studying topological sort; depth first search; cycles in directed graphs ("digraphs")
# solution is modified but almost verbatim from: 
# https://youtu.be/KptcDjF92pE?t=955 
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int: 
        N = n 
        graph = defaultdict(list) 
        in_degree = defaultdict(int) 
        
        for relation in relations: 
            prereq = relation[0] 
            course = relation[1] 
            graph[prereq].append(course) 
            in_degree[course] += 1 
        
        queue = deque([i for i in range(1, N+1) if i not in in_degree]) 
        number_of_semesters = 0 
        courses_taken = 0 
        
        while queue: 
            number_of_semesters += 1 
            
            que_length = len(queue) 
            for _ in range(que_length):
                vertex = queue.popleft() 
                courses_taken += 1 
                for neighbor in graph[vertex]:
                    in_degree[neighbor] -= 1 
                    if in_degree[neighbor] == 0: # remember we can take courses w/ no prereq remaining `in_degree` counts extant prereqs 
                        queue.append(neighbor) 
        return number_of_semesters if courses_taken == N else -1 
            
        
        