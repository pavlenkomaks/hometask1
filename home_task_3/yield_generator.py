def some_chain(*coll):
    for i in coll:
        for j in i:
            yield j

coll = some_chain([1, 2, 3], [4, 5, 6], [7, '888', 9])

for j in coll:
    print(j)


