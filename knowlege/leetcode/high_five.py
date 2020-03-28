def high_five(items):
	Dict = {}
	for item in items:
		if item[0] in Dict:
			Dict[item[0]].append(item[1])
		else:
			Dict[item[0]] = [item[1]]
	print(Dict)
	res = []
	for ID in Dict:
		Dict[ID].sort(reverse = True)
		res.append([ID,sum((Dict[ID])[0:5])/5])
		print(Dict[ID])
	return res

Input = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

Output = high_five(Input)
print(Output)
