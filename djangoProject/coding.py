# -*- encoding: utf-8 -*-
"""
@File    : coding.py
@Time    : 2020/2/5 18:10
@Author  : David
@Contact : admin@mdavid.cn
@Github  : https://github.com/HEUDavid
@Desc    : 编码练习
"""


class Solution:
    def Fibonacci(self, n):
        # write code here
        if n < 0 or n > 39:
            return None
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]


if __name__ == '__main__':
    slv = Solution()
    res = slv.Fibonacci(5)
    print(res)
