import qrcode

# link da página
inputData = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

qr = qrcode.QRCode(version=1, box_size=4, border=5)

qr.add_data(inputData)
qr.make(fit=True)

img = qr.make_image(fill='black', back_collor='white')

# salvando a imagem
img.save('qrcode.png')