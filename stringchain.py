class Solution(object):
    def longestStrChain(self, words):
        import collections
        words.sort(key = len)
        dp = collections.defaultdict(int)
        for word in words:
            dp[word] = max([dp[word[:i] + word[i + 1:]] for i in range(len(word))]) + 1
        return max(dp.values()) 
val=Solution()
n=int(input())
words=list(map(str,input().split()))
print(val.longestStrChain(words))
