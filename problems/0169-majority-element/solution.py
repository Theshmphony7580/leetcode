class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        k = max_count = 0

        for n in nums:
            if max_count == 0:
                k = n 
            max_count += 1 if n == k else -1 

        return k 

