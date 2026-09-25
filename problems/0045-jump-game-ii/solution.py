class Solution:
    def jump(self, nums: list[int]) -> int:
        near = 0 
        end = 0 
        farthest = 0 

        for i in range(len(nums)-1):
            farthest = max(farthest , i+nums[i])
            if farthest >= len(nums)-1:
                near += 1
                break
            if i == end :
                near += 1
                end = farthest

        return near        
