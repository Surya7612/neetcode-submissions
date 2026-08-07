class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''brute force: sort and group, create a hash map where each key is the sorted version og a string, and the value is a list of strings belonging to that anagram group. we iterate through each string in the i/p list and sort the characters of the string to form a key, and then append the original string to the list correspondign to this key. After processing all the strings, return all values from the hash map, which represent the grouped anagram'''
      #  res = defaultdict(list) # it is a subclass of the standard dict that provideds a default value for keys that do not exist yet. When you try to access or modify a missing key in a normal dictionart, python raises a KeyError. A defaultdict avoids this error by automatically calling a factory function(like list, int, or set) to create a default value for any missing key on the spot.
        '''defaultdict(list): best for grouping items or building adjacency lists for graphs. Initial value: []
        defaultdict(int): best for counting occurences or frequencies of items. Initial value: 0
        defaultdict(set): best for storing unique values per key without duplicates'''
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values()) # TC: O(m*n log n), SC: O(m*n) m = number of strings and n is the length of the longest string

        ''' Optimal Solution: Hash Table: Instead of sorting each string, we can represent every string by the frequency of its characters. Since the problem uses lowercase English letters, a fixed-size array of length 26 can capture how many times each character appears. Two strings are anagrams if and only if their frequencies arrays are identical. By using this frequency array (converted to a tuple so it can be a dictioanry key), we can group all string that share the same character counts.'''
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values()) # TC O(m*n)


