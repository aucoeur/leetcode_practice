from typing import List

'''
Leetcode #1: https://leetcode.com/problems/two-sum/ - Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
            return [0, 1].
'''

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        
        # go through nums list
        for index, current_num in enumerate(nums):
            # subtract current number from target to get remainder
            remainder = target - current_num

            # if remainder has already been encountered, return its index and the current number's index
            if remainder in checked:
                return [checked[remainder], index]
            
            # else, if current_num has not yet been encountered, 
            # add to checked dict with its index as value
            checked[current_num] = index

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    answer = Solution().two_sum(nums, target)
    print(f"Indices of number in nums that add up to target: {answer}")
