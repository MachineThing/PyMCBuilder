from image_to_pixel import *
import glob, operator
flammable_tex = glob.glob("mc_blocks/flammable/*.png")
unflammable_tex = glob.glob("mc_blocks/unflammable/*.png")
all_tex = []

for i in range(len(flammable_tex)):
    flammable_tex[i] = all_tex.append([flammable_tex[i][20:], True, calc_avg_pixel(flammable_tex[i])])
for i in range(len(unflammable_tex)):
    unflammable_tex[i] = all_tex.append([unflammable_tex[i][22:], False, calc_avg_pixel(unflammable_tex[i])])

print(sorted(all_tex, key = operator.itemgetter(0)))
