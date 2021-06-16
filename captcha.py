from PIL import Image


image = Image.open("./sc/captcha.png")
image = image.crop((836, 483, 962, 520))  # defines crop points
image.save("./sc/captch.png", 'png')  # saves new cropped image


im = Image.open("./sc/captcha.png")
im = im.convert("P")
im2 = Image.new("P",im.size,255)

im = im.convert("P")

temp = {}

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        temp[pix] = pix
        for i in range(2,100):
            if pix == i:
                im2.putpixel((y,x),0)

im2.save("./sc/output.png")
