intervals = [[1,3],[6,9]]

newInterval = [2,5]

def insertInterval(interval, newInterval):

    result = []

    flag = True

    for i in range(len(interval)):

        # If newInterval is greater than the first element of the interval

        if flag and interval[i][0] > newInterval[1] :
            result.append(newInterval)
            flag = False

        if interval[i][1] < newInterval[0]:
            result.append(interval[i])

        elif interval[i][1] <= newInterval[1]:

            newInterval[0] = min(newInterval[0], interval[i][0])
            newInterval[1] = max(newInterval[1],interval[i][1])

        else:

            if flag:
                result.append(newInterval)
                flag = False
            result.append(interval[i])

    if flag:

        result.append(newInterval)


    return result

print(insertInterval(intervals, newInterval))