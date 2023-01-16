# naive brute force method 

class MedianFinder:

    def __init__(self):
        self.all_numbers = [] 
        

    def addNum(self, num: int) -> None:
        self.all_numbers.append(num) 
        

    def findMedian(self) -> float:
        self.all_numbers = sorted(self.all_numbers) 
        if len(self.all_numbers) % 2 == 0: 
            return (self.all_numbers[len(self.all_numbers)//2] + self.all_numbers[len(self.all_numbers)//2 - 1]) / 2
        else:
            return self.all_numbers[len(self.all_numbers)//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()