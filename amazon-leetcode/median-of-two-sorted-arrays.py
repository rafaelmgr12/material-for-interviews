"""
# Problem: Median of Two Sorted Arrays

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
'''

def findMedianSortedArrays(nums1, nums2):
    # Combine the two arrays and sort the resulting array
    combined = sorted(nums1 + nums2)
    length = len(combined)
    
    # If the combined array has an odd length, return the middle element
    if length % 2 == 1:
        return combined[length // 2]
    # If the combined array has an even length, return the average of the two middle elements
    else:
        return (combined[length // 2 - 1] + combined[length // 2]) / 2.0

# Example usage
if __name__ == "__main__":
    print(findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
    print(findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        merged = []
        i, j = 0, 0

        # Merge nums1 and nums2 into a single sorted array
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Append any remaining elements from either nums1 or nums2
        while i < m:
            merged.append(nums1[i])
            i += 1
        while j < n:
            merged.append(nums2[j])
            j += 1

        # Calculate the median from the merged array
        total_len = m + n
        if total_len % 2 == 0:
            return (merged[total_len // 2 - 1] + merged[total_len // 2]) / 2
        else:
            return merged[total_len // 2]
