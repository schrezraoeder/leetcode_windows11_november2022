class Solution(object):
    def _find_minimum(self, start, end): 
        if start > end:
            return -1 
        if start == end: 
            if self.array[start] < self.min_so_far:
                return self.array[start] 
            else: 
                return self.min_so_far 
            
        mid = start + (end - start) // 2 
        if self.array[mid] > self.supremum: 
            return self._find_minimum(mid+1, end) 
        elif self.array[mid] < self.supremum: 
            if self.array[mid] < self.min_so_far:
                self.min_so_far = self.array[mid] 
            return self._find_minimum(start, mid)  
        else: 
            return self.min_so_far 


        # min_so_far = arr[len(arr)-1] 
        # min_so_far = self.array[end] 
        # supremum = arr[0] 
        # mid = start + (end - start) // 2 
        # if arr[mid] > supremum: arr[0..index_of_max] 
        # if arr[mid] < supremum: arr[index_of_max+1..end_of_array_index]:
        #     min_so_far = arr[mid] 
        #     binary_search(start, mid) 

    def findMin(self, array): # [3,1,2] 
        self.array = array 
        # edge case: there is no rotation index, the entire array is sorted 
        if self.array[0] < self.array[len(self.array)-1]:
            return self.array[0] 
        self.supremum = self.array[0] 
        self.min_so_far = self.array[len(self.array)-1] 
        return self._find_minimum(0, len(array)-1)
    
# NOTE: this code I wrote after failing miserably to explain my thinking process with Apoorva tonight. 
# so it is straight from de kopf. Well... Apoorva helped me a bit in spite of being unable to follow 
# what the heck I was doing **probably** [massively understated] b/c i miserably failed to explain my
# thinking process. -- ejs 

'''
sorted array, search element
[2,3,4,6,8,13] ==> 1 return index of the element ==> -1 if d.n.e.  
search for 3
'''

# **binary search** 
# O(log n) 

# class BinarySearch: 
#     def _binary_search(self, start, end):
#         if start > end: # edge case 
#             return -1 
#         if start == end: 
#             if self.target == self.array[start]:
#                 return start 
#             return -1 # hardcoded value for d.n.e. 
#         # else: start < end [x y] 
#         mid = start + (end - start) // 2 # edge cases?  <--- 
#         if self.array[mid] == self.target: 
#             return mid 
#         elif self.array[mid] < self.target: 
#             # search to the right of mid 
#             return self._binary_search(mid+1, end) 
#         else: # self.target < self.array[mid] 
#             # search to the left of self.array[mid] 
#             return self._binary_search(start, mid-1)  
         
#     def binary_search(self, array, target):
#         self.array = array 
#         self.target = target 
#         return self._binary_search(0, len(array)-1)


# binarySearch = BinarySearch() 
# #print (binarySearch.binary_search([2,3,4,6,8,13,17], 9)) 





# # [o o o - - - x . . . o o o]  
# # [2,3,4,|6,8,13]  

# # middle <- 6 
# # compare(middle, search_element) 
# # binary_search(array[:middle_index]) 
# # binary_search(array == [3, 4]) 

# '''
# arr = [6,7, 0, 1,2,3,4,5]
# Find the minimum element in this rotated sorted array
 
# arr = [0,1,2,3,4,5]


# arr = [4,5,6,7,0,1,2,3]



# '''

# # O(log n) 

# # # edge case: there is no rotation index, the entire array is sorted 
# # if arr[0] < arr[len(arr)-1]:
# #     return arr[0] 
# # min_so_far = arr[len(arr)-1] 
# # supremum = arr[0] 
# # mid = start + (end - start) // 2 
# # if arr[mid] > supremum: arr[0..index_of_max] 
# # if arr[mid] < supremum: arr[index_of_max+1..end_of_array_index]:
# #     min_so_far = arr[mid] 
# #     binary_search(start, mid) 
# [3,1,2]
# min_so_far = 2
# supremum= 3

# class MinimumSearch: 
#     def _find_minimum(self, start, end): 
#         if start > end:
#             return -1 
#         if start == end: 
#             if self.array[start] < self.min_so_far:
#                 return self.array[start] 
#             else: 
#                 return self.min_so_far 
            
#         mid = start + (end - start) // 2 
#         if self.array[mid] > self.supremum: 
#             return self._find_minimum(mid+1, end) 
#         elif self.array[mid] < self.supremum: 
#             if self.array[mid] < self.min_so_far:
#                 self.min_so_far = self.array[mid] 
#             return self._find_minimum(start, mid)  
#         else: 
#             return self.min_so_far 


#         # min_so_far = arr[len(arr)-1] 
#         # min_so_far = self.array[end] 
#         # supremum = arr[0] 
#         # mid = start + (end - start) // 2 
#         # if arr[mid] > supremum: arr[0..index_of_max] 
#         # if arr[mid] < supremum: arr[index_of_max+1..end_of_array_index]:
#         #     min_so_far = arr[mid] 
#         #     binary_search(start, mid) 

#     def find_minimum(self, array): # [3,1,2] 
#         self.array = array 
#         # edge case: there is no rotation index, the entire array is sorted 
#         if self.array[0] < self.array[len(self.array)-1]:
#             return self.array[0] 
#         self.supremum = self.array[0] 
#         self.min_so_far = self.array[len(self.array)-1] 
#         return self._find_minimum(0, len(array)-1)



# minSearch = MinimumSearch() 

# arr0 = [6,7, 0, 1,2,3,4,5]
# # Find the minimum element in this rotated sorted array
 
# arr = [0,1,2,3,4,5]


# arr1 = [4,5,6,7,0,1,2,3]

# arr2 = [7,0,1]
# print (minSearch.find_minimum(arr2)) 
        