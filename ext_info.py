
import sys
import os
import functools

if len(sys.argv) != 2:
	print("Usage %s <directory>"%sys.argv[0])
	exit()

(_,directory)= sys.argv

files = {}

for x in os.listdir(directory):
	files.setdefault(os.path.splitext(x)[1],[] ).append(x)


for key in files:
	print(key[1:],end=" ")
	print(len(files[key]),end=" ")
	size = 0
	for f in files[key]:
		size+=os.path.getsize(os.path.join(directory,f))

	print(size)