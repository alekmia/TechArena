import numpy as np
import check
import shapely

global figure
global c1
global c2
from shapely.geometry import Polygon


def calc(rects):
    res = 0
    for i in rects:
        if check.checkIfIn(figure, i):
            res += 1 + c1 * i.area()
        else:
            res += 1 + c2 * i.area()
    return res


def func(params):
    rects = []
    for i in params:
        cloneI = i.copy()
        cloneI.append((i[1][0], i[0][1]))
        polyRect = Polygon(cloneI)
        rects.append(polyRect)
    if check.checkIfCovers(figure, rects):
        return calc(rects)
    else:
        return np.inf

a = np.array([[[1,2],[2,3]], [[4,1],[6,8]]])
for i in a:
    print(i[0][0], i[0][1])