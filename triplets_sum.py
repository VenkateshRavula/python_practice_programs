l = [-90, 80, 801, -5, 3, 2, 7, 10]

sorted_l = sorted(l)
n = len(sorted_l)
for i in range(n-1):
    low = i+1
    upp = n-1 # last index value
    while low < upp:
        if sorted_l[i] + sorted_l[low] + sorted_l[upp] == 0:
            print(sorted_l[i], sorted_l[low], sorted_l[upp])
            low += 1
            upp -= 1
        elif sorted_l[i] + sorted_l[low] + sorted_l[upp] > 0:
            upp -= 1
        else:
            low += 1
