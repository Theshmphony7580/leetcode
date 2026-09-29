class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candidates = [1]*n


        for j in range(1,n):
            if ratings[j] > ratings[j-1] and candidates[j]<= candidates[j]:
                candidates[j] = candidates[j-1] + 1
            
        for k in range(n-2,-1,-1):
            if ratings[k] > ratings[k+1] and candidates[k + 1] >= candidates[k]:
                candidates[k] = candidates[k+1] + 1

        return sum(candidates)
