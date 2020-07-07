'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
'''


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        rest =  0  # 记录总的加油量和消耗，如果能够跑完一圈，遍历完就必须大于等于0
        start = 0
        flag = 0   # 记录从start能不能到达i+1.小于0到达不了。
        for i in range(len(gas)):
            rest += gas[i] - cost[i]
            flag += gas[i] - cost[i]
            if flag < 0:  # 到达不了i+1
                flag = 0  
                start = i + 1
        if rest < 0:   
            return -1
        else:
            return start
