import qrcode
qr=qrcode.make("https://www.google.com/")
qr.save("google.png")
print("QR code generated and saved as google.png")