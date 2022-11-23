# NOTE: while I had watched the neetcode solution on youtube at https://youtu.be/A8NUOmlwOlM?t=696  
# earlier today as I knew that 1. I would be peer mock interviewing with this question tonight & 2. 
# that I was **way** too low on time to try to figure it out on my own today; 
# I did not actually look at any outside resources nor google anything while coding it up from memory 
# a number of hours later on in the evening & I would have to ask for critical feedback but my
# perception is that I explained my thinking process pretty well to somebody who mostly codes Java & no python 
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
                
        