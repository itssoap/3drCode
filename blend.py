from PIL import Image
image1 = Image.open(r"out/1.png")
image2 = Image.open(r"out/2.png")
image3 = Image.open(r"out/3.png")
#image1.show()
#image2.show()
#image3.show()
image4 = image1.convert("RGBA")
image5 = image2.convert("RGBA")
image6 = image3.convert("RGBA")
alphaBlended = Image.blend(image5, image6, alpha=1/2)
#alphaBlended.show()
final1 = Image.blend(image4, alphaBlended, alpha=2/3)
#final1.show()
final1=final1.convert("RGB")
#bg = Image.new("RGBA", final1.size, "WHITE")
#bg.paste(final1,(0,0), final1)
#bg=bg.convert("RGB").save("muxed.jpg")
datas = final1.getdata()

new_image_data = []
for item in datas:
    if item==(0,0,0):
        new_image_data.append((255,255,255))
    else:
        new_image_data.append(item)
final1.putdata(new_image_data)
final1.show()
final1.convert("RGB").save("muxed.jpg")