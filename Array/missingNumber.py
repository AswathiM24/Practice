#Given an array nums containing n distinct numbers in the range [0, n],
#return the only number in the range that is missing from the array.

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i,v in enumerate(nums):
            if i!=v:
                return v-1
            if v==len(nums)-1:
                return v+1 

