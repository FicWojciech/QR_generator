#pip install qrcode

import qrcode

data = input("Pass Your link\n")

img_name = input("QR file name\n")

img = qrcode.make(data)

img.save(f"{img_name}.png")
