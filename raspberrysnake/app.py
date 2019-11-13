from tkinter import *
from graphics.images import ImageLoader

# Create Application
app = Tk()
app.title("Raspberry Snake")
app.geometry("640x480")
app.resizable(False, False)

# Create Canvas
canvas = Canvas(app, bg = "black", width = 640, height = 480, highlightthickness = 0)

# Create Logo
logo = canvas.create_image(160, 160, image = ImageLoader.load("logo"), anchor = NW)

# Pack Canvas
canvas.pack()

# Start Application
app.mainloop()