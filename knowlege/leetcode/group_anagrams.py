import collections

def groupAnagrams(strs):
	ans = collections.defaultdict(list)
	for s in strs:
		ans[tuple(sorted(s))].append(s)
	return ans.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))
