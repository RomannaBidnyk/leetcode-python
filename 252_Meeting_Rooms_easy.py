# 252 - Meeting Rooms (Easy)

# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n)

from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True


intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
print(Solution().canAttendMeetings(intervals))  # Output: False

intervals = [Interval(5, 8), Interval(9, 150)]
print(Solution().canAttendMeetings(intervals)) # Output: True