import qrcode
data ='''
name:bilalpatel813
roll no. : 16
class : fycs sem2
colllege : ismail yusuf college
'''
qr= qrcode.QRCode(version= 1,
error_correction= qrcode.constants.ERROR_CORRECT_H,
box_size =8,
border =2)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="darkblue",
back_color="white")
img.save("studentQR.png")