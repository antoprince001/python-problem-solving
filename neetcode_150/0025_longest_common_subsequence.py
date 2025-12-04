# Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

# A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

# For example, "cat" is a subsequence of "crabt".
# A common subsequence of two strings is a subsequence that exists in both strings.


class Solution:
    def longestCommonSubsequenceHelper(self, text1: str, text1_index: int, text2: str,text2_index: int, helper_dict : dict) -> int:
        if text1_index == len(text1):
            return 0
        if text2_index == len(text2):
            return 0
        if (text1_index,text2_index) in helper_dict:
            return helper_dict[(text1_index,text2_index)]
        if text1[text1_index] == text2[text2_index]:
            helper_dict[(text1_index,text2_index)] = 1 + self.longestCommonSubsequenceHelper(
                text1,
                text1_index + 1,
                text2,
                text2_index + 1,
                helper_dict
            )
        else:
            helper_dict[(text1_index,text2_index)] = max(self.longestCommonSubsequenceHelper(text1,text1_index + 1,text2,text2_index,helper_dict),self.longestCommonSubsequenceHelper(text1,text1_index,text2,text2_index+1,helper_dict))
        return helper_dict[(text1_index,text2_index)]
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        helper_dict = {}
        return self.longestCommonSubsequenceHelper(
            text1,
            0,
            text2,
            0,
            helper_dict
        )



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)]
                 for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]
