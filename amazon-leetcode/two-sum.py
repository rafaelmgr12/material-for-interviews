class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Problem: Two Sum

        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Examples:
        1. Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        2. Input: nums = [3,2,4], target = 6
        Output: [1,2]

        3. Input: nums = [3,3], target = 6
        Output: [0,1]

        Solution:
        This solution utilizes a hash map to track the complement of each number (i.e., target - number) as we iterate through the list.
        If the complement exists, we've found the two numbers that sum up to the target.
        """
        seen = {}

        for i, value in enumerate(nums):
            remaining = target - value

            if remaining in seen:
                return [seen[remaining], i]
            seen[value] = i

        return []
