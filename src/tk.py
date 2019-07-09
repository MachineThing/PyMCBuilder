from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.image = ""
        master.title("PyMcBuilder")
        master.geometry("500x400")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        self.img_label = tk.Label(self, height=200)

        file = tk.Menu(menu)
        file.add_command(label="Open image", command=self.get_file)
        file.add_command(label="Save result", command=quit)
        #file.add_command(label="Save schematic", command=quit)
        file.add_command(label="Exit", command=quit)
        menu.add_cascade(label="File", menu=file)

        self.img_label.pack(expand="no")

    def get_file(self):
        file_get = filedialog.askopenfilename(title = "Select image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.image = file_get
        self.display_image()

    def display_image(self):
        load = Image.open(self.image)
        load.convert('RGB')
        load.thumbnail((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        # Load image
        self.img_label['image']=render
        self.img_label.image = render

root = tk.Tk()
app = Application(master=root)
app.mainloop()
