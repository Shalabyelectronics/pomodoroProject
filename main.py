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
FOCUS = 10
REST = 5
LONG_REST = 15
cycle = 0
marks = 1

#-------- Font ------#
FONT= "Coiny"
#---------------------- Count Down Functinality -------------------#
# Note we need to run the time as minutes:seconds
# So one minute have 60 second so each time 60 second done one minutes will added but for our count down will decremented
def call_count_down():
    # first we an expression argument that multiplay the minutes with the total seconds in a minutes.
    global cycle
    if cycle % 2 == 0 and cycle < 8:
        focus_state.config(text="Focus")
        count_down(FOCUS)
        cycle +=1
    elif cycle % 2 != 0:
        focus_state.config(text="Short break")
        count_down(REST)
        cycle +=1
    else:
        global marks
        check_marks.config(text="✅" * marks )
        marks +=1
        focus_state.config(text="Long break")
        count_down(LONG_REST)
        cycle = 0




def count_down(time):
    # We used math module because of floor method as it rounded the number to the small value for example 4.8 will be 4
    minutes = math.floor(time / 60)
    # we used modulo to get the current remaining seconds.
    seconds = time % 60
    # Refactor the code from this
    # we can use if or while statement here and it will check the total time if it is greater or equal to zero.
    # if time >= 0:
    #     # we checked the minutes if minutes are less than 10 so it will take a range of number from 9 to 0.
    #     if minutes <10:
    #         # Then it will check if the minutes are less than 10.
    #         if seconds < 10:
    #             # If true it will change the text canvas so we add zero as string leftof each minutes and seconds
    #             canvas.itemconfig(canvas_text, text=f"0{minutes}:0{seconds}")
    #         else:
    #             # Else if seconds are greater than 10 just change the whole seconds.
    #             canvas.itemconfig(canvas_text, text=f"0{minutes}:{seconds}")
    #     elif minutes > 9 :
    #         # Then it will check if the minutes are greater than 9 so it will take a range of number from 10 to infinte.
    #         if seconds < 10 :
    #             canvas.itemconfig(canvas_text, text=f"{minutes}:0{seconds}")
    #         else:
    #             canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
        # last line is the why we update the window each one second by calling the count_down function and decremented the time.
    # refactor it to this so I save more line of codes and it become easy to read.
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    #Note that python support Dynamic typing as we can change the data type of the variable in any stage of our programe
    # And only python support this techniqe as other programming languages can't change the data types assigned to their
    # Variables like C and Java for example.
    canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
    if time>0:
        window.after(1000, count_down, time - 1)
    return "Done"

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
focus_state = Label(text=" ", fg=NAVY_BLUE, bg=SAND_DOLLAR, font=(FONT, 25))
focus_state.grid(column=1, row=3)
# Create check_markes label
check_marks= Label(text=" ", fg=RED,bg=SAND_DOLLAR, font=(FONT,25) ,highlightthickness=0)
check_marks.grid(column=1, row=4)


window.mainloop()
