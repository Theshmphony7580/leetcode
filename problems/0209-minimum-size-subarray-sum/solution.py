class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        total = 0
        min_len = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                min_len = min(min_len,r-l+1)
                total -= nums[l]
                l += 1 

        return min_len if min_len!=float('inf') else 0

        # r = 1
        # lenh = []
        # total = 0
        # while l != r:
        #     total = sum(nums[l:r+1])
        #     print (total)
        #     if total < target:
        #         r += 1
        #         print (r)
        #     elif total >= target:
        #         lenth = r-l+1
        #         lenh.append(lenth)
        #         l += 1


            

            

        
