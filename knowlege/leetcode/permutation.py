def permutation(nums):
	if nums == []:
		return []
	elif len(nums) == 1:
		return [nums]
	else:
		res = []
		for i,item in enumerate(nums):
			rest = nums[0:i]+nums[i+1:len(nums)]
			combs = permutation(rest)
			for comb in combs:
				res.append([item]+comb)
		return res


nums = [1,2,3,4]
print(nums)
print("*************")
[print(comb) for comb in permutation(nums)]
