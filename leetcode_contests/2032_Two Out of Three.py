# 2032. Two Out of Three
# Given three integer arrays nums1, nums2, and nums3, return a distinct array 
# containing all the values that are present in at least two out of the three arrays. 
# You may return the values in any order.
#
#class Solution:
#    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

# Test data        
#nums1 = [1,1,3,2]
#nums2 = [2,3]
#nums3 = [3,4,5]
nums1 = [3,1]
nums2 = [2,3]
nums3 = [1,2,4]
#nums1 = [1,2,2]
#nums2 = [4,3,3]
#nums3 = [5]

#combine_unic_list = []
result_list = []

# simple brootforce conditional to get numbers in at least two nums lists
for unic_item in set(nums1+nums2+nums3):
    if (((unic_item in nums1) and (unic_item in nums2)) or ((unic_item in nums1) and (unic_item in nums3)) or ((unic_item in nums2) and (unic_item in nums3))):
        result_list.append(unic_item)

print(f"{result_list}")