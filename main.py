from tkinter import *

# ----------constants-----------#
# --- COLORS ----#
SAND_DOLLAR = "#E5DDC8"
TEAL = "#01949A"
NAVY_BLUE = "#004369"
RED = "#DB1F48"
# COLORED palate from https://www.canva.com/colors/color-palettes/

# First we are going to import all classes from tkinter module.

# --------------------- Create application GUI --------------------#
window = Tk()
window.title("Pomodoro")
# Add padding to our window padx and pady.
window.config(padx=100, pady=50)
# create a pomodoro_img object from the class PhotoImage.
pomodoro_img = PhotoImage(file="pomodoro.png")
canvas = Canvas(width=500, height=500)
canvas.create_image(250, 250, image=pomodoro_img)
canvas.pack()

window.mainloop()
