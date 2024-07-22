import qrcode

data = 'Qr code base'

img = qrcode.make(data)


qr = qrcode.QRCode(version= 2, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('C:/Users/sandr/OneDrive/Documentos/Github/Qr code/imag/myqrcode3.png')


