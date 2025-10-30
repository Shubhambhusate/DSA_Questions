intervals = [[1,4],[2,3]]

def mergeInterval(interval):

    interval.sort()

    result = []
    
    result.append(interval[0])

    for i in range(1,len(interval)):

        if result[-1][1] >= interval[i][0] and result[-1][1] >= interval[i][1]:

            pass

        elif result[-1][1] >= interval[i][0]:

            result[-1][1] = interval[i][1]

        else:

            result.append(interval[i])

    return result

print(mergeInterval(intervals))






        
        
