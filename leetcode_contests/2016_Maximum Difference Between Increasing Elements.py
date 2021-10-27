# 2016. Maximum Difference Between Increasing Elements
# Given a 0-indexed integer array nums of size n, 
# find the maximum difference between nums[i] and nums[j] 
# (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
#
# Return the maximum difference. If no such i and j exists, return -1.
#
# class Solution:
#    def maximumDifference(self, nums: List[int]) -> int:


def maximumDifference(nums) -> int:
        max_difference = -1
        nums_list = nums
        len_nums_list = len(nums_list)
        
        for i in range(0, len_nums_list-1):
            for j in range(i+1, len_nums_list):
                if nums_list[i] < nums_list[j]:
                    if (nums_list[j] - nums_list[i]) > max_difference:
                        max_difference = nums_list[j] - nums_list[i]
        return max_difference
    


#test_case = [7,1,5,4]
#test_case = [9,4,3,2]
test_case = [1,5,2,10]

my_max_difference = maximumDifference(test_case)
print(f"{my_max_difference}")



"""
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        self.max_difference = -1
        self.nums_list = nums
        self.len_nums_list = len(self.nums_list)
        for i in range(0, self.len_nums_list-1):
            for j in range(i+1, self.len_nums_list):
                if self.nums_list[i] < self.nums_list[j]:
                    if (self.nums_list[j] - self.nums_list[i]) > self.max_difference:
                        self.max_difference = self.nums_list[j] - self.nums_list[i]
        return self.max_difference
    
test_case = [7,1,5,4]
#test_case = [9,4,3,2]
#test_case = [1,5,2,10]

my_solution = Solution
my_max_difference = my_solution.maximumDifference(test_case)
print(f"{my_max_difference}")

"""