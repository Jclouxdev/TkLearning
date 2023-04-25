import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import json


class ImageResizer:
    def __init__(self, master):
        # Langues
        f = open("./Langs/FR.json")
        Strings = json.load(f)

        self.master = master
        master.title("Image Resizer")

        # Create the menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # Create the "File" menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.option_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=Strings["menu"]["file"], menu=self.file_menu)
        self.menu_bar.add_cascade(
            label=Strings["menu"]["options"], menu=self.option_menu
        )

        # Add "Open" and "Save As" options to the "File" menu
        self.file_menu.add_command(
            label=Strings["menu"]["open"]["label"],
            command=self.open_image,
            accelerator="Ctrl+O",
        )
        self.master.bind("<Control-o>", self.open_image)  # shortcut

        self.file_menu.add_command(
            label=Strings["menu"]["save_as"]["label"],
            command=self.save_image,
            state=tk.DISABLED,
            accelerator="Ctrl+S",
        )
        self.master.bind("<Control-s>", self.save_image)  # shortcut

        # Add "Exit"
        self.option_menu.add_command(
            label=Strings["menu"]["quit"]["label"], command=exit, accelerator="Ctrl+Q"
        )
        self.master.bind("<Control-q>", exit)  # Shortcut

        # Créer un widget Frame pour placer les champs et les boutons sur la même ligne
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.open_button = tk.Button(
            self.frame,
            text=Strings["widgets"]["frame"]["open_button"],
            command=self.open_image,
        )
        self.open_button.pack(side=tk.LEFT)

        self.width_label = tk.Label(
            self.frame, text=Strings["widgets"]["frame"]["width_label"]
        )
        self.width_label.pack(side=tk.LEFT)

        self.width_entry = tk.Entry(self.frame)
        self.width_entry.pack(side=tk.LEFT)

        self.height_label = tk.Label(
            self.frame, text=Strings["widgets"]["frame"]["height_label"]
        )
        self.height_label.pack(side=tk.LEFT)

        self.height_entry = tk.Entry(self.frame)
        self.height_entry.pack(side=tk.LEFT)

        self.format_var = tk.StringVar(value="JPEG")
        self.format_menu = tk.OptionMenu(
            self.frame, self.format_var, "JPEG", "PNG", "BMP"
        )
        self.format_menu.pack(side=tk.LEFT)

        self.save_button = tk.Button(
            self.frame,
            text=Strings["widgets"]["frame"]["save_button"],
            command=self.save_image,
            state=tk.DISABLED,
        )
        self.save_button.pack(side=tk.LEFT)

        self.error_label = tk.Label(master, text="", fg="red")
        self.error_label.pack(side=tk.TOP)

        self.canvas = tk.Canvas(master)
        self.canvas.pack(side=tk.BOTTOM)

    def open_image(self, event=None):
        f = open("./Langs/FR.json")
        Strings = json.load(f)

        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.config(width=self.image.width, height=self.image.height)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
            self.save_button.config(state=tk.NORMAL)
            self.file_menu.entryconfig(
                Strings["menu"]["save_as"]["label"], state=tk.NORMAL
            )

    def save_image(self, event=None):
        width = self.width_entry.get()
        height = self.height_entry.get()

        if not width or not height:
            self.error_label.config(text="Please enter a width and height")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension="." + self.format_var.get().lower()
        )
        if file_path:
            width = int(width)
            height = int(height)
            format = self.format_var.get()
            resized_image = self.image.resize((width, height), Image.ANTIALIAS)
            resized_image.save(file_path, format=format)

            self.error_label.config(text="Image saved successfully")
            # reset fields
            self.width_entry.delete(0, tk.END)
            self.height_entry.delete(0, tk.END)
            self.canvas.delete("all")
            self.save_button.config(state=tk.DISABLED)


root = tk.Tk()
app = ImageResizer(root)
root.mainloop()
