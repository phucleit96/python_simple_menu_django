import qrcode
import PIL

image = qrcode.make("https://127.0.0.1:8002")
image.save("qr.png")

