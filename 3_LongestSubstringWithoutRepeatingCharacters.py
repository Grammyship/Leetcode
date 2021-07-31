"""
3. Longest Substring Without Repeating Characters
Time Submitted: 07/26/2021 11:09
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = left = right = 0
        temp = {}
        while right < len(s):
            if s[right] in temp and temp[s[right]] >= left:
                left = temp[s[right]] + 1
            ans = max(ans, right-left+1)
            temp[s[right]] = right
            right += 1
        return ans
