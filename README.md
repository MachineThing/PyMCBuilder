# Python Minecraft image builder
This program builds an image that the user specifies into Minecraft via the RaspberryJamMod.
## Color algorithm
How the color algorithm will work is that the program will compare each pixel to each supported Minecraft block specified in the ```blocks.json``` file and will decrease size for images bigger than 200 pixels in height, resulting in poor quality for huge images with boat loads of different colors but good quality for small images. The (graphical) program will show what the image might look like in game.

**Note: I will add more blocks in the future**
