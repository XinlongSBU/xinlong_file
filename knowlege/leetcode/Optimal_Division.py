'''
Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.
'''

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if(len(nums)==1):
            return str(nums[0])
        elif(len(nums)==2):
            return str(nums[0])+"/"+str(nums[1])
        strings=str(nums[0])+"/("
        for i in nums[1:]:
            strings+=str(i)+"/"
        strings=strings[:len(strings)-1]
        strings=strings+")"
        return strings


class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        if len(nums) <= 2:
            return '/'.join(nums)
        return '{}/({})'.format(nums[0], '/'.join(nums[1:]))


