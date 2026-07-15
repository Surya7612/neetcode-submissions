class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # if there are duplicates then set length would not be equal to nums as set only includes unique values
        return len(set(nums)) < len(nums)