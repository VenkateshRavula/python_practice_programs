def minimumBribes(q):

    count = 0
    tooChaotic = False

    for i in range(len(q)):
        # to translate between q[i] and the position in a zero-indexed python list,
        # you have to add 1, so here it's i+3 rather than i+2
        if q[i] > i + 3:
            print("Too chaotic")
            tooChaotic = True
            break
        else:
            # q[i]-2 rather than q[i]-1 since python is zero-indexed
            # but the people in the queue start at 1
            start = max(0, q[i]-2)
            for j in range(start, i):
                if q[j] > q[i]:
                    count += 1

    if tooChaotic == False:
        print(count)

l = [2,1,5,3,4]
minimumBribes(l)