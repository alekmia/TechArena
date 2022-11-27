from scipy.optimize import minimize, LinearConstraint
import numpy as np
import check
import function

test = 1
filename = "tests/0" + str(test) + ".txt"

f = open(filename, "r")
input = f.read()
a = [float(i) for i in input.split()]

n = int(a.pop(0))
c1 = a.pop(0)
c2 = a.pop(0)
coords = []
for i in range(len(a) // 2):
    coords.append([a.pop(0), a.pop(0)])

# print(coords)
left, right, top, bottom = float("inf"), 0-float("inf"), 0-float("inf"), float("inf")
for i in range(n):
    left = min(left, coords[i][0])
    right = max(right, coords[i][0])
    top = max(top, coords[i][1])
    bottom = min(bottom, coords[i][1])

bounds = [([left, bottom], [right, top]) for i in range(n)]

x0 = []
pointCount = 3
for i in range(pointCount):
    x = np.random.randint(left, right)


res = minimize(
    function.func,
    x0,
    # args=args,
    bounds=bounds
)



