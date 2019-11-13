import tkinter as tk

# Create Application
app = tk.Tk()
app.title("Raspberry Snake")
app.geometry("640x480")
app.resizable(False, False)

# Create Canvas
canvas = tk.Canvas(app, bg = "black", width = 640, height = 480, highlightthickness = 0)
canvas.pack()

# Start Application
app.mainloop()