tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)

h = list(tuple1 + tuple2)
g = []

n = 0
while True:
    if n == len(h):
        break

    if h.count(h[n]) >= 2:
        g.append(h[n])
        h.remove(h[n])

    n += 1

h = tuple(sorted(h))
g = tuple(sorted(g))

print(f'합집합 : {h}')
print(f'교집합 : {g}')