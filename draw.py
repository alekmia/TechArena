from PIL import Image
import operator

img = Image.open('foo.png')

# Count the pixels having RGB values in defined range

upper = (000, 000, 255)
lower = (000, 000, 254)
colors = set()
for i in img.getdata():
    if i[0] == 255:
        colors.add(i)
print(colors)
