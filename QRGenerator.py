import qrcode.constants

QR = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)

inputURL = str(input("What URL would you like to convert? : "))

QR.add_data("inputURL")
QR.make(fit=True)

image = QR.make_image(fill_color="black", back_color="white")

image.save('/Users/selin/Desktop/genQR.png')

print("Your QR code has been saved !")

