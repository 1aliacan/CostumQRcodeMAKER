import pyqrcode


url = input("Olusturmak istedigin sitenin linkini gir : ")

qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg',scale=5)