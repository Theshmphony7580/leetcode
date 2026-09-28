class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)

        cf = 0
        start = 0
        for i in range(n):
            cf += gas[i] - cost[i]
            if cf < 0:
                cf = 0
                start = i + 1
        return start
            
             

        
