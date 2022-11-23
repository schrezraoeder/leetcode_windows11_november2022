# NOTE: this is the neetcode solution on youtube at https://youtu.be/A8NUOmlwOlM?t=696  
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        answer = [] 
        for ix, interval in enumerate(intervals): 
            # if newInterval is *completely* before interval 
            if newInterval[1] < interval[0]: 
                answer.append(newInterval) 
                answer = answer + intervals[ix:]
                return answer 

            elif interval[1] < newInterval[0]: 
                answer.append(interval) 

            # if there is any partial overlap: combine newInterval with interval 
            # newInterval = merge newInteral with interval 
            else: # double check this is exhaustive & doesn't include anything we don't want 
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])] 
                # newInterval == [3, 10] 
                # answer = [1, 2] 

        answer.append(newInterval) 

        return answer 
                
        