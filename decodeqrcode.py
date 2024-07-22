from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/sandr/OneDrive/Documentos/Github/Qr code/imag/myqrcode.png')

result = decode(img)


print(result)