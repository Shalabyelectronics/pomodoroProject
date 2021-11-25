# First we are going to import all classes from tkinter module.
from tkinter import *
import math

# ----------constants-----------#
# --- COLORS ----#
SAND_DOLLAR = "#E5DDC8"
TEAL = "#01949A"
NAVY_BLUE = "#004369"
RED = "#DB1F48"
# COLORED palate from https://www.canva.com/colors/color-palettes/
# ----- Timing ----# Note: All timing will convert later to seconds.
FOCUS = 25
REST = 5
LONG_REST = 30

#-------- Font ------#
FONT= "Coiny"
#---------------------- Count Down Functinality -------------------#
# Note we need to run the time as minutes:seconds
# So one minute have 60 second so each time 60 second done one minutes will added but for our count down will decremented
def call_count_down():
    count_down(1*60)

def count_down(time):
    minutes = math.floor(time / 60)
    seconds = time % 60
    if time >= 0:
        if minutes <10:
            if seconds == 0 or seconds < 10:
                canvas.itemconfig(canvas_text, text=f"0{minutes}:0{seconds}")
            else:
                canvas.itemconfig(canvas_text, text=f"0{minutes}:{seconds}")
        elif minutes > 9 :
            if seconds == 0 :
                canvas.itemconfig(canvas_text, text=f"{minutes}:0{seconds}")
            else:
                canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
        window.after(1000, count_down, time - 1)





# --------------------- Create application GUI --------------------#
window = Tk()
window.title("Pomodoro")
# Add padding to our window padx and pady and bg refer to back ground color.
window.config(padx=100, pady=50, bg=SAND_DOLLAR)
# create a pomodoro_img object from the class PhotoImage.
pomodoro_img = PhotoImage(file="pomodoro.png")
# Create the canvas object from canvas class also we add the same dimension for the image and we add the same color
# and we removed the boarder from highlightthickness to zero.
canvas = Canvas(width=500, height=500, bg=SAND_DOLLAR, highlightthickness=0)
# canvas.create_image is the way to add an image in tkinter module first parameter for x coordinate and the next is y
# coordinate.
canvas.create_image(250, 250, image=pomodoro_img)
# Create the text on the tomato image that refer to timing.
canvas_text= canvas.create_text(250, 275, text="00:00",fill="white" ,font=(FONT, 50))
canvas.grid(column=1, row=1)
# Create the timing label up from the tometo image
timing_label = Label(text="Timing", fg=NAVY_BLUE, bg=SAND_DOLLAR, font=(FONT, 50))
timing_label.grid(column=1, row=0)
# Create start button
start = Button(text="Start",fg=TEAL,bg=SAND_DOLLAR, font=(FONT,25) ,highlightthickness=0, command=call_count_down)
start.grid(column=0, row=2)
# create rest button
rest = Button(text="Rest",fg=TEAL,bg=SAND_DOLLAR, font=(FONT,25) ,highlightthickness=0)
rest.grid(column=2, row=2)
# Create check_markes label
check_marks= Label(text="✅", fg=RED,bg=SAND_DOLLAR, font=(FONT,25) ,highlightthickness=0)
check_marks.grid(column=1, row=3)


window.mainloop()
