# I'm just the one that executes the instructions!
import sys, math, json, operator, time
import mcpi.minecraft as minecraft
from PIL import Image as pillow
from blockid import get_block
import mcpi.block as block
import functions as pymc
from tqdm import tqdm
import tkinter as tk

# Functions

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
    pymc.chat(mc, "image is over 200 pixels, reducing height.", 1)

rim.convert('RGB')
im = rim.load()

pbar = tqdm(total=imhei*imwid)
for hei in range(imhei):
    for wid in range(imwid):
        smal = pymc.comp_pixel((im[wid, hei][0], im[wid, hei][1], im[wid, hei][2]), json_put)
        im[wid, hei] = smal[1]
        used.append(str(smal[2]))
        pbar.update(1)
pbar.close()

rim.save("result.GIF") # The result
json_file.close()

oldPos = mc.player.getPos()
playerPos = [round(oldPos.x), round(oldPos.y), round(oldPos.z)]
pymc.chat(mc, "Ready!")
pbar = tqdm(total=imhei*imwid)
num_temp = imhei*imwid-1
for hei in range(imhei):
    for wid in range(imwid):
        #print(used[wid + (imhei * hei)])
        gblock = get_block(used[num_temp])
        mc.setBlock(playerPos[0]+wid, playerPos[1]+hei, playerPos[2], gblock)
        num_temp -= 1
        pbar.update(1)
pbar.close()
pymc.chat(mc, "Done!!")
pymc.chat(mc, "Please star us on github if you like the result!", 2)
