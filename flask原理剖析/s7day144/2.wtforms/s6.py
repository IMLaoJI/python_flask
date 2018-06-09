v = [11,22,334,4,2]
v.sort()
print(v)


v1 = [
    (11,'alex1'),
    (2,'alex2'),
    (2,'alex3'),
    (7,'alex4'),
]
v1.sort(key=lambda x:(x[0],x[1]))
print(v1)