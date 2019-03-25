from PIL import Image, ImageDraw, ImageFont
from collections import defaultdict
from statistics import mean, stdev


img = Image.open('output.png', mode='r')
total_pixels = img.size[0] * img.size[1]
hist = defaultdict(lambda: 0)

imgpx = img.load() # create the pixel map
for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        hist[imgpx[i,j]] += 1

# print(hist)
avg_freq = mean(hist.values())
std_dev = stdev(hist.values())
print(avg_freq, std_dev)

thresh = avg_freq + 1.5 * std_dev
for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        if hist[imgpx[i,j]] < thresh:
            imgpx[i,j] = (0,0,0)
img.show()
