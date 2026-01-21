class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        self.nums = nums

        unique = list(set(nums))


        for i in range(len(unique)):
            # result = []
            occur = nums.count(unique[i])
            if occur == 1:
                return unique[i]

