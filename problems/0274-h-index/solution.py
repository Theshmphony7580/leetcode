class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations = sorted(citations, reverse=True)
        for i in range(len(citations)):
            if i + 1 > citations[i]:
                return i 
        return len(citations)
