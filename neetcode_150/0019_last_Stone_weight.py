# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            heapq.heapify(stones)
            x, y = heapq.nlargest(2, stones)
            if x == y:
                stones.remove(x)
                stones.remove(y)
            else:
                diff = x - y
                stones.remove(x)
                stones.remove(y)
                stones.append(diff)
        if len(stones) == 1: 
            return stones[0] 
        else:
            return 0
            



        
