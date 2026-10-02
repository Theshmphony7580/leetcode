class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, curr, j = 0, 0, 0
        m = set()
        for i in s:
            if i in m:
                while s[j] != i:
                    m.remove(s[j])
                    j += 1
                    curr -= 1
                j += 1
            else:
                curr += 1
                ans = max(curr, ans)
                m.add(i)
        return ans
