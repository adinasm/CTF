## crossed-pil

**Flag: ctf{3c7f44ab3f90a097124ecedab70d764348cba286a96ef2eb5456bee7897cc685}**

I found a hidden image in [image.zip](image.zip):
```
binwalk -e image.zip 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, uncompressed size: 153442, name: image.png
76            0x4C            PNG image, 200 x 200, 8-bit/color RGBA, non-interlaced
117           0x75            Zlib compressed data, default compression
153371        0x2571B         End of Zip archive, footer length: 22
```

Then I found the python code which generated the image in [image.png](image.png):
```
strings image.png
```
```
import numpy as np
from PIL import Image
import random
img = Image.open('flag.png')
pixels = list(img.getdata())
oioi=[]
for value in pixels:
    oi = []
    for oioioi in value:
        # hate me note for the var names ;)
        if oioioi == 255:
            oioioi = random.choice(range(0, 255, 2))
        else:
            oioioi = random.choice(range(0, 255, 1))
        oi.append(oioioi)
    oioi.append(oi)
img = Image.new('RGBA', [200,200], 255)
data = img.load()
count = 0
for x in range(img.size[0]):
    for y in range(img.size[1]):
        data[x,y] = (
            oioi[count][0],
            oioi[count][1],
            oioi[count][2],
            oioi[count][3],
        )
        count = count + 1

img.save('image.png')
```

I created the script [crossedpil.py](crossedpil.py) in which I tried to obtain the initial
image. I did the same procedure, but if a number was even, then the new value was 255, otherwise 0.
I saw that a picture similar to a QR code was generated, so if all the values
from a pixel were not black, then I made them white, otherwise black. The QR
code was incomplete, so I turned black the pixels which had at least 3 black
neighbours.
Then I [scanned](https://online-barcode-reader.inliteresearch.com/) [the QR code](flag.png) and obtained the flag.


[Back](../unbreakable.md)
