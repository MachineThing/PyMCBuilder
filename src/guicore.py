# I'm the graphical version of clcore!
from tkinter import filedialog, messagebox
import mcpi.minecraft as minecraft
from PIL import Image, ImageTk
from random import randint
import mcpi.block as block
import tkinter.ttk as tk2
import functions as pymc
import os, json, time
import tkinter as tk

img_filename = os.path.join(os.getcwd(), '.'+str(randint(10000000, 99999999))+'PMB.GIF')

class Application(tk.Frame):
    def __init__(self, master=None):
        self.mc_linked = False
        self.img_loaded = False
        self.result_made = False
        self.bytes = 0
        self.maxbytes = 0
        super().__init__(master)
        self.master = master
        self.image = ""
        master.title("PyMcBuilder")
        master.geometry("325x293")
        master.iconbitmap(os.path.join(os.getcwd(), 'images\\Logo.ico'))

        self.pack()

        try:
            self.mc = minecraft.Minecraft.create()
            pymc.chat(self.mc, "Minecraft is linked!")
            self.mc_linked = True
        except:
            pass

        try:
            json_file = open("blocks.json")
            self.json_put = json.load(json_file)
        except:
            messagebox.showerror("PyMcBuilder", "blocks.json is not found!\nplease reinstall PyMcBuilder.")
            sys.exit(1)

        self.create_widgets()

    def create_widgets(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        self.image = os.path.join(os.getcwd(), 'images\\pImage.JPG')
        self.img_label = tk.Label(self, height=200)
        self.display_image()

        self.alerts_label = tk.Label(self, text="No image!", fg="red")
        self.progress = tk2.Progressbar(self, orient='horizontal',length=500,mode='determinate')
        self.b_frame = tk.Frame(self)
        self.get_result = tk.Button(self.b_frame, text="Make result", state="disabled", command=self.generate_result)
        self.link_mc = tk.Button(self.b_frame, text="Link Minecraft", state="active", command=self.link_minecraft)
        self.print_img = tk.Button(self.b_frame, text="Build image!", state="disabled", command=self.print_image)

        if self.mc_linked == True:
            self.link_mc['state']="disabled"

        self.alerts_label.pack(side="top")
        self.progress.pack(side="bottom")
        self.img_label.pack(expand="no")
        self.get_result.grid(row=0, column=0)
        self.link_mc.grid(row=0, column=1)
        self.print_img.grid(row=0, column=2)
        self.b_frame.pack(side="bottom")

        file = tk.Menu(menu)
        file.add_command(label="Open image", command=self.get_file)
        file.add_command(label="Save result", command=quit)
        #file.add_command(label="Save schematic", command=quit)
        file.add_command(label="Exit", command=quit)
        menu.add_cascade(label="File", menu=file)

    def get_file(self):
        types = (
        #('gif','gif'),
        ('jfif','jfif'),
        ('jpeg','jpg'),
        )
        alltypes = ""
        alltype = []
        for type in types:
            alltype.append(type[1])
        alltypes = " *.".join(alltype)
        lstypes = [("All supported files",alltypes),("all files","*.*")]

        for ntype in types:
            file = ntype[0]+' files', '*.'+ntype[1]
            lstypes.append(file)

        stypes = tuple(lstypes)

        try:
            file_get = filedialog.askopenfilename(title = "Select image",filetypes = stypes)
            if file_get != '':
                self.image = file_get
                self.display_image()
                self.get_result['state']="active"
        except:
            print("Bad image!")

    def display_image(self):
        self.mim = Image.open(self.image)
        self.mim.convert('RGB')
        self.mim.thumbnail((200, 200), Image.ANTIALIAS)
        self.imwid, self.imhei = self.mim.size
        render = ImageTk.PhotoImage(self.mim)
        self.im = self.mim.load()
        # Load image
        self.img_label['image'] = render
        self.img_label.image = render
        # Change label
        if self.img_loaded == False:
            self.img_loaded = True
        else:
            if self.mc_linked == False:
                self.alerts_label['fg']='red'
                self.alerts_label['text']='Minecraft is not linked!'
            else:
                if self.result_made == False:
                    self.alerts_label['fg']='red'
                    self.alerts_label['text']='No MC version image made!'
                else:
                    self.alerts_label['fg']='black'
                    self.alerts_label['text']='Ready!'
                    pymc.chat(self.mc, "Ready!")

    def read_bytes(self):
        max = self.progress["maximum"]
        # simulate reading 500 bytes; update progress bar
        self.bytes += 500
        self.progress["value"] = self.bytes
        if self.bytes < max:
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)

    def generate_result(self):
        self.progress["maximum"] = self.imhei*self.imwid
        self.bused = []
        for hei in range(self.imhei):
            for wid in range(self.imwid):
                smal = pymc.comp_pixel((self.im[wid, hei][0], self.im[wid, hei][1], self.im[wid, hei][2]), self.json_put)
                self.im[wid, hei] = smal[1]
                self.bused.append(str(smal[2]))
                self.progress["value"] += 1
                self.read_bytes()
        self.mim.save(img_filename)
        nimage = Image.open(img_filename)
        nimage.convert('RGB')
        nimage.thumbnail((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(nimage)
        self.img_label['image'] = render
        self.img_label.image = render
        self.result_made = True

    def link_minecraft(self):
        try:
            self.mc = minecraft.Minecraft.create()
            pymc.chat(self.mc, "Minecraft is linked!")
            self.mc_linked = True
        except ConnectionRefusedError:
            messagebox.showerror("PyMcBuilder", "Minecraft is not linked!\nDo you have the RaspberryJamMod and is Minecraft open?")
    def print_image(self):
        pass

root = tk.Tk()
app = Application(master=root)
app.mainloop()
try:
    os.remove(img_filename)
except:
    pass
