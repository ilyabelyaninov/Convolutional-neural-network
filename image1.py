import numpy as np
from PIL import Image

im = Image.open('kemerovo.jpg')
im2arr = np.array(im)

for h in range(im2arr.shape[0]):
    for w in range(im2arr.shape[1]):
        for c in range(im2arr.shape[2]):
            # if c == 0:
            #     r = im2arr[h, w, c]
            if c != 2:
                tmp = im2arr[h, w, c] + 59
            # tmp = round(im2arr[h, w, c] + 255)
                tmp = tmp if tmp <= 255 else 255
                tmp = tmp if tmp >= 0 else 0

                im2arr[h, w, c] = tmp

img = Image.fromarray(im2arr, 'RGB')
img.show()
