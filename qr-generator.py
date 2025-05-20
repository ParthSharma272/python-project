import qrcode

data = input("Enter the data:")
version = int(input("Enter the version(complexity):"))
box_size = int(input("Enter the box size:"))

qr = qrcode.QRCode(version = version , box_size = box_size, border = 5)
qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save('img.png')

print("qr generated and saved in the gallery")