from tkinter import *
from tkinter import ttk

frame = ttk.Frame(parent)

# PADDING
frame["padding"] = 5  # 5 pixels on all sides
frame["padding"] = (5, 10)  # 5 on left and right, 10 on top and bottom
frame["padding"] = (5, 7, 10, 12)  # left: 5, top: 7, right: 10, bottom: 12

# BORDERS
frame["borderwidth"] = 2
frame["relief"] = "sunken"

# STYLES
s = ttk.Style()
s.configure("Danger.TFrame", background="red", borderwidth=5, relief="raised")
ttk.Frame(root, width=200, height=200, style="Danger.TFrame").grid()
