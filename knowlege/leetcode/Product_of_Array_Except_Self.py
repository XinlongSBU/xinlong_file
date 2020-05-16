'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left_multiplier = 1
        right_multiplier = 1
        output = [1] * n
        
        for idx in range(0, n):
            output[idx] = output[idx] * left_multiplier
            left_multiplier = left_multiplier * nums[idx]
            
        for idx in range(n-1, -1, -1):
            output[idx] = output[idx] * right_multiplier
            right_multiplier = right_multiplier * nums[idx]
            
        return output
