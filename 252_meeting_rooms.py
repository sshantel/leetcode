"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

canAttendMeetings([[0,30],[5,10],[15,20]])
False

canAttendMeetings([[7,10],[2,4]])
True

"""


def canAttendMeetings(intervals):
    if not intervals:
        return True

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    print(sorted_intervals)
    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i - 1][1] > sorted_intervals[i][0]:
            return False

    return True


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n✨ ALL TESTS PASSED!\n")

