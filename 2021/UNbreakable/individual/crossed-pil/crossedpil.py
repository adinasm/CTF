import numpy as np
from PIL import Image
import random
img = Image.open('image.png')
pixels = list(img.getdata())
j=[]
for value in pixels:
	i = []
	for val_val in value:
		# hate me note for the var names ;)
		if val_val % 2:
			val_val = 0
		else:
			val_val = 255
		i.append(val_val)
	j.append(i)

img = Image.new('RGBA', [200,200], 255)
data = img.load()
count = 0
for x in range(img.size[0]):
	for y in range(img.size[1]):
		if j[count][0] and j[count][1] and j[count][2] and j[count][3]:
			data[x,y] = (255, 255, 255, 255)

		else:
			data[x,y] = (0, 0, 0, 0)
		count = count + 1

changed = True

while changed:
	changed = False
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			num_black_neigh = 0
			if x - 1 >= 0 and data[x-1,y] == (0, 0, 0, 0):
				num_black_neigh += 1
			if y - 1 >= 0 and data[x,y-1] == (0, 0, 0, 0):
				num_black_neigh += 1
			if x + 1 < img.size[0] and data[x+1,y] == (0, 0, 0, 0):
				num_black_neigh += 1
			if y + 1 < img.size[1] and data[x,y+1] == (0, 0, 0, 0):
				num_black_neigh += 1

			if num_black_neigh >= 3 and data[x,y] != (0, 0, 0, 0):
				data[x,y] = (0, 0, 0, 0)
				changed = True

img.save('flag.png')
