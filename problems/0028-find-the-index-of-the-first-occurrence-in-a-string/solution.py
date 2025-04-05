class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        index = haystack.find(needle)
        right = 0

        while right < len(needle) and right < len(haystack) and needle[right] == haystack[right]:
            right += 1 
            if index == -1 :
                return -1 
        return index


        # for i in range(len(haystack)):
        #     if needle[right != haystack[right]
