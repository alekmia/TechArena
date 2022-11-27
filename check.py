import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from shapely.geometry import Polygon
# from shapely import box, LineString, normalize, Polygon


def checkIfCovers(figureCoord, rects):
    polya = Polygon(figureCoord)
    polyDiff = polya
    for i in rects:
        i.append((i[1][0], i[0][1]))
        i.append(i.pop(1))
        i.append((i[0][0], i[2][1]))
        print(i)
        polyb = Polygon(i)
        polyDiff = polyDiff.difference(polyb)
    if polyDiff.area == 0:
        return True
    return False

def checkIfIn(container, inside):
    polyFig = Polygon(container)
    i = inside
    i.append((i[1][0], i[0][1]))
    i.append(i.pop(1))
    i.append((i[0][0], i[2][1]))
    polyRect = Polygon(i)
    print(i)
    # plt.plot(polyRect)
    # plt.show()
    return polyFig.contains(polyRect)