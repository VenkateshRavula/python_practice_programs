def filledOrders(order, k):
    # Write your code here
    sorted_order = sorted(order, reverse=True)
    if k < 1 or k > 10**9 or len(order) < 1 or len(order) > 2*10**5 or sorted_order[0] > 10**9 or sorted_order[-1] < 1:
        return 0
    sorted_order = sorted(order, reverse=True)
    print(k, sorted_order)
    while len(sorted_order) != 0:
        if sum(sorted_order) <= k:
            return len(sorted_order)
        else:
            sorted_order.pop()
    return 0

def findSum(numbers, queries):
    # Write your code here
    out = []
    for query in queries:
        if 0 in numbers[query[0]-1:query[1]]:
            s = sum(numbers[query[0]-1:query[1]],query[2])
        else:
            s = sum(numbers[query[0]-1:query[1]])
        out.append(s)
    return out