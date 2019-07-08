from image_to_pixel import *
import glob, operator, json
flammable_tex = glob.glob("mc_blocks/flammable/*.png")
unflammable_tex = glob.glob("mc_blocks/unflammable/*.png")
all_tex = []
json_file = open("../blocks.json", "w")

for i in range(len(flammable_tex)):
    flammable_tex[i] = all_tex.append({"Name":flammable_tex[i][20:], "Flammable?":True, "Color":calc_avg_pixel(flammable_tex[i])})
for i in range(len(unflammable_tex)):
    unflammable_tex[i] = all_tex.append({"Name":unflammable_tex[i][22:], "Flammable?":False, "Color":calc_avg_pixel(unflammable_tex[i])})

flist = sorted(all_tex, key = operator.itemgetter("Name"))
json_file.write(json.dumps(flist, indent=2, sort_keys=True))
json_file.truncate() # Make JSON file the size of the given text
json_file.close()
