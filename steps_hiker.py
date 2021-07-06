def countingValleys(path):
    # Write your code here
    d = {'U': 1, 'D': -1}
    sum = 0
    count = 0
    flag = 0
    for step in path:
        if step == 'D':
            flag = 1
        #if flag == 1:
        sum += d[step]
        if step == 'U' and sum == 0 and flag == 1:
            flag = 0
            count += 1
        print(">>> step: {}, count: {}, flag: {}, sum: {}".format(step, count, flag, sum))
    return count

inp = 'DDUUDDUDUUUD'
print(countingValleys(inp))