import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def checkIf(figureCoord, rectCoord):
    figureCoord.append(figureCoord[0])  # repeat the first point to create a 'closed loop'

    xs, ys = zip(*figureCoord)  # create lists of x and y values

    plt.figure()
    plt.axis('equal')
    plt.fill(xs, ys)

    for i in rectCoord:
        a = i[0]
        b = i[1]
        width = abs(b[0] - a[0])
        height = abs(b[1] - a[1])
        plt.gca().add_patch(Rectangle(a, width, height, color="red"))

    plt.savefig('foo.png')
