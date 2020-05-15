''' Leetcode #3: https://leetcode.com/problems/longest-substring-without-repeating-characters/ - Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

'''
Time Complexity: O(n) because it iterates through the string just once
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        encountered = {}
        longest = 0

        pointer = 0

        for i, letter in enumerate(s):
            if letter in encountered:
                pointer = max(pointer, encountered[letter] + 1)

            encountered[letter] = i
            longest = max(longest, i - pointer + 1)

            # print(f'{i} pointer {pointer}, {letter}, {encountered}')
        return longest

text = "amazing"
print(Solution().lengthOfLongestSubstring(text))