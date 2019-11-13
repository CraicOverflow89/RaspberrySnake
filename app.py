from tkinter import *

# Create Application
app = Tk()
app.title("Raspberry Snake")
app.geometry("640x480")
app.resizable(False, False)

# Image Data
image_data = {}
def image_load(image):
	image_data[image] = PhotoImage(file = "resources/" + image + ".gif")
	return image_data[image]
# NOTE: this logic should be encapsulated inside a class

# Create Canvas
canvas = Canvas(app, bg = "black", width = 640, height = 480, highlightthickness = 0)

# Create Logo
logo = canvas.create_image(160, 160, image = image_load("logo"), anchor = NW)

# Pack Canvas
canvas.pack()

# Start Application
app.mainloop()