l1 = ['a', 'b', {"cc":22, "de":"dess"}, [1,2,3]]
l2 = ['a', 'b', {"cc":22, "de":"dess"}]
out = []
for i,v in enumerate(l1):
    out.append([i,v])
print(dict(out))
