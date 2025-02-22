#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 4])) 
print(solution.containsDuplicate([1, 2, 3, 1]))  
