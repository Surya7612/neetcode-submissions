class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force: we can sort both s and t and compare if both of them are same, # optimal: can use hash map/dictionaries, and can compare the counts of each character, if everything is same, its anagram, if length of both of the arrays are different, not an anagram
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
        # TC = O(nlogn + mlogm)

        # for optimal approach, we create two hash maps to create character frequencies for each string and iterate through each at the same time and after building both maps, we compare them
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #.get(key, default_value)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        # TC = O(n + m)

