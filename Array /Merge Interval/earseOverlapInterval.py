intervals = [[1,2],[2,3],[3,4],[1,3]]

def eraseOverlapIntervals(intervals):

    result = []

    intervals.sort()

    result.append(intervals[0])

    count = 0

    for i in range(1,len(intervals)):

        if result[-1][1] > intervals[i][0]:

            result[-1][1] = min(intervals[i][1],result[-1][1])

            count += 1

        else:

            result.append(intervals[i])

    return count
        
print(eraseOverlapIntervals(intervals))