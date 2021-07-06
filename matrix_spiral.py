l1 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
out = [1,2,3,6,9,8,7,4,5]

def spiralOrder(matrix):
    brow, erow = 0, len(matrix) - 1  # 0,2
    if erow == -1: return []  # incase of empty matrix
    bcol, ecol = 0, len(matrix[0]) - 1  #0,2
    a = []
    while brow <= erow and bcol <= ecol:  #0<=2 and 0<=2
        # for brow
        for j in range(bcol, ecol + 1):  #0,3
            a.append(matrix[brow][j])  #00, 01, 02,
        brow += 1
        if brow > erow: break

        # for ecol
        for i in range(brow, erow+1):  # 6,9
            #1,2
            a.append(matrix[i][ecol])
        ecol -= 1
        if bcol > ecol: break

        # for erow
        for i in range(ecol, bcol-1, -1):
            a.append(matrix[erow][i])
        erow -= 1

        # for bcol
        for i in range(erow, brow-1, -1):
            a.append(matrix[i][bcol])
        bcol += 1
    return a

print(spiralOrder(l1))