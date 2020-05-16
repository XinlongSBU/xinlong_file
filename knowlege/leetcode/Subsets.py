'''
Given a set of distinct integers, nums, return all possible subsets (the power set)
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        ans.append([])
        if not nums: return ans
        for num in nums:
            ans.extend(
                [curr + [num] for curr in ans]
            )
        
        return ans
