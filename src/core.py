# I'm just the one that executes the instructions!
from PIL import Image as pillow
import sys

im = pillow.open(sys.argv[1])
imwid, imhei = im.size

maxheight = 200
im.thumbnail((200, maxheight), pillow.ANTIALIAS)
im.save("oof.JPG")
