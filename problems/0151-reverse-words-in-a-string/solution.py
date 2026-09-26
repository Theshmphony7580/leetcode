class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split()
        str_r = list_s[::-1]
        reverse = " ".join(str_r)
        return reverse
        
