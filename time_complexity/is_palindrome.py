''' Leetcode #9 - https://leetcode.com/problems/palindrome-number/ - Easy

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
''' Time Complexity
O(n) worst case, O(1) best case if x is negative or the first and last numbers are different
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        if x < 0:
            return False

        x = str(x).lower()
        left = 0
        right = len(x) - 1

        while left <= right:
            while not x[left].isalnum():
                left += 1
            while not x[right].isalnum():
                right -= 1
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True