import qrcode
import sys
import os

data = input('Enter the text or URL:').strip()
filename = input('Enter the filename:').strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(os.path.join(sys.argv[1], filename))
print(f'QR code saved as {filename}')
