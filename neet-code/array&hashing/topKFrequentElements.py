"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return [key for key, value in count.most_common(k)]


class Solution(object):
    def topKFrequent(self, nums, k):
        number_frequency = {}
        frequency_list = {}
        for i in nums:
            if i not in number_frequency:
                number_frequency[i] = 1
            else:
                number_frequency[i] += 1
        for key, value in number_frequency.items():
            if value not in frequency_list:
                frequency_list[value] = [key]
            else:
                frequency_list[value].append(key)
        result = []
        for i in range(len(nums), 0, -1):
            if i in frequency_list:
                result.extend(frequency_list[i])
            if len(result) >= k:
                break
        return result
