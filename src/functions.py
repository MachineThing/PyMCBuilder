import mcpi.minecraft as minecraft
import mcpi.block as block
import math

def chat(mc, string, type=3):
    if type == 0:
        start = "(ERROR:" # Danger
        pystart = '\033[91m'
    elif type == 1:
        start = "(warn: " # Warning
        pystart = '\033[93m'
    elif type == 2:
        start = "(info: " # Info
        pystart = '\033[94m'
    else:
        start = "(" # Normal
        pystart = '\033[0m'
    chat_string = start + "PyMcBuilder) " + string
    mc.postToChat(chat_string)
    print(pystart+string+'\033[0m')

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
