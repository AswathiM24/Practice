#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in nums:
            count = 0
            for j in nums:
                if j == i:
                    count += 1
            if count > len(nums) // 2:
                return i
        return -1  
sol = Solution()
nums = [3, 3, 4, 2, 3, 3, 3]
result = sol.majorityElement(nums)
print(result)
