import check

test = "2"
f = open("tests/0" + test + ".txt", "r")
input = f.read()
a = [float(i) for i in input.split()]
k = a.pop(0)
c1 = a.pop(0)
c2 = a.pop(0)
data = []
for i in range(len(a) // 2):
    data.append([a.pop(0), a.pop(0)])
print(data)

coord = [[1, 1], [2, 1], [2, 2], [1, 2], [0.5, 1.5]]
check.checkIf(data, [])
