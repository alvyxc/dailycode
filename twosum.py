'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

class Solution(object):
    def twoSumOn2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

        return [-1, -1]


    def twoSumOn(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        index_map = {}
        for i in range(0, len(nums)):
            index_map[nums[i]] = i

        for i in range(0, len(nums)):
            key = target - nums[i]
            if key in index_map.keys() and index_map[key] != i:
                return i, index_map[key]

        return [-1, -1]


sol = Solution()
ans = sol.twoSumOn2([2, 7, 11, 15], 9)
print("ans is: ", ans)

ans = sol.twoSumOn2([3, 2, 4], 6)
print("ans is: ", ans)

ans = sol.twoSumOn2([3, 3], 6)
print("ans is: ", ans)

ans = sol.twoSumOn([2, 7, 11, 15], 9)
print("ans is: ", ans)

ans = sol.twoSumOn([3, 2, 4], 6)
print("ans is: ", ans)

ans = sol.twoSumOn([3, 3], 6)
print("ans is: ", ans)


