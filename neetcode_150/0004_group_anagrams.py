# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Naive solution
class Solution:
    def isAnagram(self, str1: str, str2: str)->bool:
        sorted_str1 =  list(str1)
        sorted_str1.sort()
        sorted_str2 =  list(str2)
        sorted_str2.sort()
        return "".join(sorted_str1) == "".join(sorted_str2)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        i = 0
        while len(strs) > 0:
            inner_anagrams = []
            inner_anagrams.append(strs[i])
            for j in range(i+1, len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                    inner_anagrams.append(strs[j])
            # inner_anagrams.sort()
            for st in inner_anagrams:
                strs.remove(st)
            anagrams.append(inner_anagrams)
        return anagrams



# Better solution
class Solution:
    def sortString(self, str1: str):
        sorted_str1 =  list(str1)
        sorted_str1.sort()
        return "".join(sorted_str1)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for i in range(0,len(strs)):
            sortedStr = self.sortString(strs[i])
            if sortedStr not in anagram_dict:
                anagram_dict[sortedStr] = [strs[i]]
            else:
                anagram_dict[sortedStr].append(strs[i])
        
        return list(anagram_dict.values())



