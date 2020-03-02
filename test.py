"""
Name: test.py
Author: bangrenc
Time: 11/2/2020 10:38 AM
"""

m = 5
n = 3
dp = [[0] * (n + 1) for x in range(m + 1)]

print(dp)

strs = ["10", "0001", "111001", "1", "0"]

for s in strs:
    zero, one = s.count('0'), s.count('1')
    print("zero", zero)
    print("one", one)
    for x in range(m, zero - 1, -1):
        print("x", x)
        for y in range(n, one - 1, -1):
            print("y", y)
            dp[x][y] = max(dp[x - zero][y - one] + 1, dp[x][y])
            print("dp[x][y]", dp[x][y])
    print("test"*20)

print(dp[m][n])