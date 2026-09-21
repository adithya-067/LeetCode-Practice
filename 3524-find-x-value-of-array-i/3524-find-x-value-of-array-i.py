class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for x in nums:
            ndp = [0] * k
            ndp[x % k] += 1

            for i in range(k):
                ndp[(i * x) % k] += dp[i]

            for i in range(k):
                ans[i] += ndp[i]

            dp = ndp

        return ans