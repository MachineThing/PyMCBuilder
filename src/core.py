# I'm just the one that executes the instructions!
from PIL import Image as pillow
import sys, math, json, operator
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

def get_most_used(list):
    use_list = {}
    most_used = {}
    for key in list:
        if key in use_list:
            use_list[key] += 1
        else:
            use_list[key] = 1
    for i in range(9):
            cused = max(use_list.items(), key=operator.itemgetter(1))[0]
            most_used[cused] = use_list[cused]
            del(use_list[cused])
    return(most_used)

# Main code
json_file = open("blocks.json")
json_put = json.load(json_file)
rim = pillow.open(sys.argv[1])
orders = []
used = []

imwid, imhei = rim.size
maxheight = 200
rim.thumbnail((200, maxheight), pillow.ANTIALIAS)
imwid, imhei = rim.size

rim.convert('RGB')
im = rim.load()

pbar = tqdm(total=imhei*imwid)
for hei in range(imhei):
    for wid in range(imwid):
        smal = comp_pixel((im[wid, hei][0], im[wid, hei][1], im[wid, hei][2]), json_put)
        im[wid, hei] = smal[1]
        used.append(smal[2])
        pbar.update(1)
pbar.close()
most_used = get_most_used(used)

mu_blocks = []

for i in json_put:
    try:
        if i["Name"] in most_used:
            print(i)
            mu_blocks.append({"Color":i["Color"], "Name":i["Name"]})
    except ValueError:
        pass
print(mu_blocks)
pbar = tqdm(total=imhei*imwid)
for hei in range(imhei):
    for wid in range(imwid):
        smal = comp_pixel((im[wid, hei][0], im[wid, hei][1], im[wid, hei][2]), mu_blocks)
        im[wid, hei] = smal[1]
        used.append(smal[2])
        pbar.update(1)
pbar.close()

rim.save("result.JPG")
json_file.close()
