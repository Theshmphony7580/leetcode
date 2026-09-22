class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        reached=-1
        mindistance=101
        for d in range(len(drones)):
            x=drones[d][0]
            y=drones[d][1]
            range_i=drones[d][2]
            distance=abs(x-target[0])+abs(y-target[1])

            if distance>range_i:
                continue
            if distance<=range_i and distance<mindistance:
                mindistance=distance
                reached=d
                
        return reached
