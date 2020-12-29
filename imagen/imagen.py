from PIL import Image, ImageFilter, ImageColor

img = Image.open("Digimon.Adventure.full.2286231.jpg")

nvaImg = img.resize((40,40), Image.BILINEAR)

imgRes = nvaImg.resize(img.size, Image.NEAREST)

imgRes.show()

imgRes.save("nueva.png")


#########################
#Utilizamos funciones

imgRes.rotate(45).show()
im1 = imgRes.filter(ImageFilter.MinFilter(3))
im1.ImageColor.getrgb("blue")

