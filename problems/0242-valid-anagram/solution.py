class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        # freq_t = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for char in t:
            freq[char] = freq.get(char, 0) -1
        for i in freq:
            if freq.get(i) != 0:
                return False
        return True

        # print(freq)
        # if sorted(s) == sorted(t):
        #     return True
        # return False



