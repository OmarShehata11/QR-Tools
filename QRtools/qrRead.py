from pyzbar.pyzbar import decode
from PIL import Image
import sys

if len(sys.argv) < 2:
    print("[-]ERROR\nplease enter the QR image you want to decrypt !!!")
else:
	image = sys.argv[1]
	decode = decode(Image.open(image))
	# print("\nthe data : ", decode[0].data.decode('ascii'), end="\n\n--------------\n")
	print('another information : \n', decode, end="\n\n [+]DONE++\n")