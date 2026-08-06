class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force: two loops i and j, we add each pair element possible and check if it's equal to the target. O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # 2nd approach could be using sorting and use two pointer approach to find the two numbers that sum up to the target.
        '''so the approach is: we create a copy of the array and sort it in ascending order, we initialize two pointers, one at the beginning and one at the end of the array. We iterate through the array with the two pointers and check if the sum of the two numbers is equal to the target. if the sum is equal to the target, we return the indices. If the sum is lesser than the target, move the i to the right, which increases the sum or if the sum is greater than the target, we move j to the left until we find the correct output. TC being O(nlogn)'''
        # A = []
        # for i, num in enumerate(nums):
        #     A.append([num, i]) #enumerate helps to make the value and index pair

        # A.sort()
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     cur = A[i][0] + A[j][0]
        #     if cur == target:
        #         return [min(A[i][1], A[j][1]),
        #                 max(A[i][1], A[j][1])]
        #     elif cur < target:
        #         i += 1
        #     else:
        #         j -= 1
        # return []

        ''' Optimal solution is Hash Map and it can be done in two ways: Two pass and one pass. In two pass, we use a hash map to store the value of each element in the array. Then, we can iterate through the array and check if the complement of the current element exists in the hash map. Since we cant use the same element twice, the complement must be a differnt element. With Hashmap, the TC would be O(n) because the lookup and insertion of a hashmap is O(1)'''
        # indices = {} # val -> index

        # for i, n in enumerate(nums):
        #     indices[n] = i

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in indices and indices[diff] != i:
        #         return [i, indices[diff]]
        # return []

        '''One pass: here we create a hash map to store the value and index of each element in the array and iterate through the array using index i and compute the complement of the current element, which is target - nums[i]. We then check if the complement exists in the hash map'''
        prevMap = {} # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
