# I just get the average color of an image!
from PIL import Image as pillow
import sys

def calc_avg_pixel(image):
    im = pillow.open(image)
    pix = im.load()
    imwid, imhei = im.size
    imwid = imwid - 1
    imhei = imhei - 1

    red, green, blue = [],[],[]
    tred, tgreen, tblue = 0,0,0

    for hei in range(imhei):
        for wid in range(imwid):
            red.append(pix[wid, hei][0])
            green.append(pix[wid, hei][1])
            blue.append(pix[wid, hei][2])

    for i in red:
        tred = tred + i
    tred = tred / len(red)
    for i in green:
        tgreen = tgreen + i
    tgreen = tgreen / len(green)
    for i in blue:
        tblue = tblue + i
    tblue = tblue / len(blue)

    fred = int(round(tred,0))
    fgreen = int(round(tgreen,0))
    fblue = int(round(tblue,0))

    return([fred, fgreen, fblue])
