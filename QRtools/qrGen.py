import pyqrcode
import sys


if len(sys.argv) < 2:
    print("[-]ERROR\nplease enter the message you want to encrypt to QR !!!")
else :
	qr = pyqrcode.create(sys.argv[1])
	qr.png('HelloQr', scale=8)
