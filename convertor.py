from PIL import Image

png_image = Image.open("logo.png")
png_image.save("logo.icns", format='ICNS', sizes=[(24, 24)])
