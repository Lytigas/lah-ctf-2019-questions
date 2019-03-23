from random import randrange, choice
from PIL import Image, ImageDraw, ImageFont

IMG_WIDTH = 500
IMG_HEIGHT = 500

text_colors = [randrange(2**24) for i in range(20)] # random 8 bit colors
other_colors = [randrange(2**24) for i in range(IMG_WIDTH * IMG_HEIGHT // 10)]
all_colors = text_colors + other_colors

flag = "N3V3r_TRu57_4_PRNG_T0_H1De_yoU"


mask = Image.new('1', (IMG_WIDTH, IMG_HEIGHT), 0)
draw = ImageDraw.Draw(mask)
font = ImageFont.truetype('arial.ttf', 15)
for y in range(100, 300, 30):
    draw.text((100, y), flag, 1, font=font)
maskpx = mask.load()

text = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), 0)
textpx = text.load() # create the pixel map
for i in range(text.size[0]): # for every pixel:
    for j in range(text.size[1]):
            textpx[i,j] = choice(text_colors)

bg = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), 0)
bgpx = bg.load() # create the pixel map
for i in range(bg.size[0]): # for every pixel:
    for j in range(bg.size[1]):
            bgpx[i,j] = choice(all_colors)

# bg.show()

composite = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), 0)
cpx = composite.load()
for i in range(composite.size[0]): # for every pixel:
    for j in range(composite.size[1]):
        if maskpx[i,j]:
            cpx[i,j] = textpx[i,j]
        else:
            cpx[i,j] = bgpx[i,j]

# composite.show()
composite.save("output.png", format="PNG")
