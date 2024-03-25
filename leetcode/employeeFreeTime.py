"""
759. Employee Free Time
Hard
Topics
Companies
Hint
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
"""

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # initialize a heap and push the first interval of each employee onto the heap
        heap = [(employee[0].start, ei, 0) for ei, employee in enumerate(schedule)]
        # Create heap from array elements.
        heapq.heapify(heap)
        
        # Take an empty array to store the result
        res = []
        
        # Set 'previous' to the start time of first interval in heap.
        prev = schedule[heap[0][1]][heap[0][2]].start
        
        # Iterate till heap is empty
        while heap:
            # Pop an element from heap and set value of i and j
            _, i, j = heapq.heappop(heap)
            
            # Select an interval
            interval = schedule[i][j]
            # If selected interval's start value is greater than the
            # previous value, it means that this interval is free.
            # So, add this interval (previous, interval's end value) into result.
            if interval.start > prev:
                res.append(Interval(prev, interval.start))
            prev = max(prev, interval.end)

            # If there is another interval in current employees' schedule,
            # push that into heap.
            if j + 1 < len(schedule[i]):
                heapq.heappush(heap, (schedule[i][j+1].start, i, j+1))
    
        # When the heap is empty, return result.
        return res
        
        
    def employeeFreeTimeBruteForce(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        
        for employee in schedule:
            for interval in employee:
                intervals.append(interval)
        
        intervals.sort(key=lambda x: x.start)
        
        res = []
        
        prev = intervals[0]
        
        for i in range(1, len(intervals)):
            if intervals[i].start > prev.end:
                res.append(Interval(prev.end, intervals[i].start))
                prev = intervals[i]
            else:
                prev = Interval(prev.start, max(prev.end, intervals[i].end))
        
        return res
    
    
