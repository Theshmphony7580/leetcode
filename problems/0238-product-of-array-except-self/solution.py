class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        left_products = [1] * n
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        right_products = [1]*n
        for i in range(n-2,-1,-1):
            right_products[i] = right_products[i+1]*nums[i+1]

        result = [left_products[i]*right_products[i] for i in range(n)]
        return result
        # out = []
        # for idx in range(len(nums)):
        #     if idx ==0 or nums[0] == 0:
        #         prod = 0
        #     else:
        #         prod = 1
        #     for p_e in range(len(nums)):
        #         if nums[p_e] == nums[idx]:
        #             continue
        #         prod *= nums[p_e]
        #     print(prod)
        #     out.append(prod)
        # return out

        
        
