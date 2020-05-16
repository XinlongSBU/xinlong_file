'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
'''

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        leN = len(s)

        if leN == 0 or leN == 1:
            return leN

        cache = defaultdict(lambda: defaultdict(lambda: 0))
        #cache=[[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        for i in range(leN-1, -1, -1):
            for j in range(i, leN):
                if i == j:
                    cache[i][j] = 1
                else:
                    x = 0
                    if s[i] == s[j]:
                         cache[i][j]=2+cache[i+1][j-1]
                    else:
                        cache[i][j] = max(cache[i][j-1], cache[i+1][j])
        return cache[0][leN-1]

我的思路：
这道题考的是最长回文子序列，注意是序列而不是子串，序列的意思是组成回文的字符可以是不连续的，而回文子串则需要连续的，比如例子中的bbbab，最长回文序列是bbbb，最长回文子串是bbb或是bab。

当已知一个序列是回文时，添加首尾元素后的序列存在两种情况，一种是首尾元素相等，则最长回文的长度加2，当首尾元素不相等，则最长回文序列为仅添加首元素时的最长回文与仅添加尾元素时的最长回文之间的最大值。我们可以用dp[i][j]表示s[i…j]中的最长回文序列，而状态转移方程则是
1. i > j，dp[i][j] = 0；
2. i == j，dp[i][j] = 1；
3. i < j且s[i] == s[j]，dp[i][j] = dp[i + 1][j - 1] + 2；
4. i < j且s[i]！= s[j]，dp[i][j] = max(dp[i + 1][j]，dp[i][j - 1])；
从状态转移方程可以看出，计算dp[i][j]时需要用到dp[i+1][j - 1]和dp[i + 1][j]，所以对于i的遍历应该从尾部开始，最后返回dp[0][s.length() - 1]就行




改进思路：
上述的算法时间复杂度是，空间复杂度是。然而从状态转移方程来看，计算dp[i][x]时，只用到了dp[i][y]和dp[i + 1][z]，即计算当前行时，只用到了当前行和下一行，因此可以对上一个算法进行改进，需要用两行空间存储就能完成计算。

用一个变量cur表示当前行的下标，cur的取值为0或1，1 - cur表示的就是另外一行，因此状态转移方程变成了：
1. i > j，dp[cur][j] = 0；
2. i == j，dp[cur][j] = 1；
3. i < j且s[i] == s[j]，dp[cur][j] = dp[1 - cur][j - 1] + 2；
4. i < j且s[i]！= s[j]，dp[cur][j] = max(dp[1 - cur][j]，dp[cur][j - 1])；
注意每次计算完一个i后需要更新cur的值，即cur = 1 - cur。因为循环执行最后一次之后会多更新一次cur，所以返回的是dp[1 - cur][s.length() - 1]的值。



