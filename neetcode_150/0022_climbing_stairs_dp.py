# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def climbStairs(self, n: int) -> int:
        step_count = [1, 2]

        for i in range(2,n):
            step_count.append(step_count[i-1] + step_count[i-2])

        return step_count[n-1]
