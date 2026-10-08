class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_word = s.split()
        if len(pattern) != len(s_word):
            return False
        dic = {}
        used_value = set()
        for char1, char2 in zip(pattern,s_word):
            if char1 in dic and dic[char1] != char2:
                return False
            if char1 not in dic and char2 in used_value:
                return False
            dic[char1]=char2
            used_value.add(char2)
        return True
