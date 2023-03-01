class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ix, jx = float('inf'), float('inf')
        shortest_distance = float('inf')
        for pos, word in enumerate(wordsDict):
            if word == word1:
                ix = pos 
                distance = abs(jx - ix) 
                if distance < shortest_distance:
                    shortest_distance = distance 
            if word == word2: 
                jx = pos 
                distance = abs(jx - ix) 
                if distance < shortest_distance:
                    shortest_distance = distance  
        return shortest_distance 
                
                
        