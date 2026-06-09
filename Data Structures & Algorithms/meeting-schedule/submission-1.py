class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 1. Sort the intervals by their start time
        intervals.sort(key=lambda x: x.start)

        # 2. Iterate through the sorted intervals starting from the second one
        for i in range(1, len(intervals)):
            # If the current meeting starts before the previous one ends, there's a conflict
            if intervals[i].start < intervals[i - 1].end:
                return False
        
        # If we loop through without finding any overlaps, they can attend all meetings
        return True