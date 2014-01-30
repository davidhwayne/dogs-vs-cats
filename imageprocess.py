import Image
import csv
import os

c=csv.writer(open('train.csv','wb'))
filelist=os.listdir("/home/david/Downloads/train")

for n in filelist:
	if n[0]=='c':
		imlist=[0]
		im=Image.open(n).convert('L')
		imr=im.resize((100, 100), Image.ANTIALIAS)
		for i in range(100):
			for j in range(100):
				k=imr.getpixel((i,j))
				imlist.append(str(k))
		c.writerow(imlist)
	elif n[0]=='d':
		imlist=[1]
		im=Image.open(n).convert('L')
		imr=im.resize((100, 100), Image.ANTIALIAS)
		for i in range(100):
			for j in range(100):
				k=imr.getpixel((i,j))
				imlist.append(str(k))
		c.writerow(imlist)




