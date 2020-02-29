def topten():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


def squares():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = topten()
print(values.__next__())
print(values.__next__())

squ = squares()
for i in squ:
    print(i)
