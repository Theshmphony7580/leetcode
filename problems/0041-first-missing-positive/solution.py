class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # defalt = 0
        nums_set = set(nums)
        max_set = max(nums) if nums else 0
        if max_set < 1:
            return 1

        for i in range(1, max_set + 1):
            if i not in nums_set:
                return i

        return max_set+1


        
        # print(result)
                # return i
        # for i in nums_set:
        #     if i == defalt:
        #         print(defalt)
        #     defalt += 1
        # # print(defalt)
        
