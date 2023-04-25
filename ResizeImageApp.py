import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageResizer:
    def __init__(self, master):
        self.master = master
        master.title("Image Resizer")

        # Créer un widget Frame pour placer les champs et les boutons sur la même ligne
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.open_button = tk.Button(
            self.frame, text="Open Image", command=self.open_image
        )
        self.open_button.pack(side=tk.LEFT)

        self.width_label = tk.Label(self.frame, text="Width:")
        self.width_label.pack(side=tk.LEFT)

        self.width_entry = tk.Entry(self.frame)
        self.width_entry.pack(side=tk.LEFT)

        self.height_label = tk.Label(self.frame, text="Height:")
        self.height_label.pack(side=tk.LEFT)

        self.height_entry = tk.Entry(self.frame)
        self.height_entry.pack(side=tk.LEFT)

        self.save_button = tk.Button(
            self.frame, text="Save Image", command=self.save_image, state=tk.DISABLED
        )
        self.save_button.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(master)
        self.canvas.pack(side=tk.BOTTOM)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.config(width=self.image.width, height=self.image.height)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
            self.save_button.config(state=tk.NORMAL)

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_path:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            resized_image = self.image.resize((width, height), Image.ANTIALIAS)
            resized_image.save(file_path)


root = tk.Tk()
app = ImageResizer(root)
root.mainloop()
