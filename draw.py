from PIL import Image
import operator

img = Image.open('foo.png')

# Count the pixels having RGB values in defined range

for i in img.getdata():
    print(i)

