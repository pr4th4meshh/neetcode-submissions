class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left = 0 
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                left = max(mp[s[r]] + 1, left)
            mp[s[r]] = r
            res = max(res, r - left + 1)
        return res