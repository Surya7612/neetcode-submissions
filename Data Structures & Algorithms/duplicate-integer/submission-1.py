class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False # This gives us O(n^2) as TC

        # Sorting, we have TC as O(nlogn)
        # one sort the array and compare adjacent pairs
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        # Optimal Solution, Hashset: we use hashset to efficiently track of teh values we have already encountered. As we iterate through the array, we check whether the current value is already present in the set. If it is, that means we've seen this value before, so a duplicate exists. Thus, constant-time lookups.
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
