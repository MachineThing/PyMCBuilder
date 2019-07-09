# I'm just the one that executes the instructions!
import sys, math, json, operator, time, sys
import mcpi.minecraft as minecraft
from PIL import Image as pillow
from blockid import get_block
import mcpi.block as block
import functions as pymc
from tqdm import tqdm

# Functions

def color_dist(c1, c2):
    # Thx stack overflow
    (r1,g1,b1) = c1
    (r2,g2,b2) = c2
    return math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2)

def comp_pixel(rgb, blist):
    smallest_rgb = ()
    smallest_num = 999
    smallest_name = ""
    for i in blist:
        irgb = (list(i["Color"])[0], list(i["Color"])[1], list(i["Color"])[2])
        col_num = color_dist(rgb, irgb)

        if col_num < smallest_num:
            smallest_num = col_num
            smallest_rgb = irgb
            smallest_name = i["Name"]
    return([smallest_num, smallest_rgb, smallest_name])

# Main code
mc = minecraft.Minecraft.create()
try:
    json_file = open("blocks.json")
    json_put = json.load(json_file)
except:
    pymc.chat(mc, "blocks.json not found, exiting!", 0)
    sys.exit(1)
try:
    rim = pillow.open(sys.argv[1])
except:
    pymc.chat(mc, "bad image, exiting!", 0)
    sys.exit(1)
orders = []
used = []

imwid, imhei = rim.size
if imhei > 200:
    maxheight = 200
    rim.thumbnail((200, maxheight), pillow.ANTIALIAS)
    imwid, imhei = rim.size
    pymc.chat(mc, "image is over 200 pixels, reducing height.", 2)

rim.convert('RGB')
im = rim.load()

pbar = tqdm(total=imhei*imwid)
for hei in range(imhei):
    wid_list = []
    for wid in range(imwid):
        smal = comp_pixel((im[wid, hei][0], im[wid, hei][1], im[wid, hei][2]), json_put)
        im[wid, hei] = smal[1]
        wid_list.append(smal[2])
        pbar.update(1)
    used.append(wid_list)
pbar.close()

rim.save("result.JPG")
json_file.close()

oldPos = mc.player.getPos()
playerPos = [round(oldPos.x), round(oldPos.y), round(oldPos.z)]
pymc.chat(mc, "Ready!")
pbar = tqdm(total=imhei*imwid)
for hei in range(imhei):
    list = used[hei]
    for wid in range(imwid):
        pass
        mc.setBlock(playerPos[0]+imwid, playerPos[1]+imhei, playerPos[2], get_block(list[wid]))
pbar.close()
