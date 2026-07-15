class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        count = {}
        max_f = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]]) 
            
            while (r - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, r - left + 1)
        return res