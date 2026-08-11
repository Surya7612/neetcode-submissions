class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute foce: O(n^2), SC = O(n)
        # res = 0
        # store = set(nums)

        # for num in nums:
        #     streak, curr = 0, num
        #     while curr in store:
        #         streak += 1
        #         curr += 1
        #     res = max(res, streak)
        # return res

        # '''Brute Force 2: Sort and count the consecutive streak, O(nlogn)'''
        # if not nums: # if array is empty return 0
        #     return 0
        # res = 0
        # nums.sort()

        # curr, streak = nums[0], 0
        # i = 0
        # while i < len(nums):
        #     if curr != nums[i]:
        #         curr = nums[i]
        #         streak = 0
        #     while i < len(nums) and nums[i] == curr:
        #         i += 1
        #     streak += 1
        #     curr += 1
        #     res = max(res, streak)
        # return res

        # Optimal: O(n) both, hash set
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
