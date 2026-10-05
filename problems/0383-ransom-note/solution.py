class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for l in magazine:
            dic[l] = dic.get(l, 0) + 1

        for i in ransomNote:

            if i not in dic or dic[i]<=0:
                return False
            dic[i] -= 1
        return True
