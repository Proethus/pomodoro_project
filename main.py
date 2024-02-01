import math
from tkinter import *
import datetime
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
INTERVAL = 25
GENERAL_BREAK = 5
CYCLE_END_BREAK = 25
TOTAL_ITERATIONS = 4


def start_timer():
    reset_button_var.set(False)
    window.after(1000, update_time, True, 0, INTERVAL, 0, check_mark_text)


def reset_timer():
    if not reset_button_var.get():
        title_text.configure(text="Work", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
        canvas.itemconfig(time_text, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
        check_marks.configure(text=check_mark_text, font=("WINGDINGS", 20, "normal"), bg=YELLOW, fg=GREEN,
                              highlightthickness=0)
        reset_button_var.set(True)


def update_time(started, iteration, interval, seconds, check_mark):
    if started and not reset_button_var.get():
        if interval * 60 - seconds < 1:
            hrs, mins, secs = str(datetime.timedelta(seconds=0)).split(":")
            canvas.itemconfig(time_text, text=f"{mins}:{secs}")
            if iteration < TOTAL_ITERATIONS:
                if interval == INTERVAL:
                    update_title("Break")
                    window.after(1000, update_time, started, iteration, GENERAL_BREAK, 0, check_mark)
                else:
                    if iteration == TOTAL_ITERATIONS - 1:
                        check_mark += f"{chr(0xFC)}"
                        check_marks.configure(text=check_mark)
                        update_title("Long break")
                        window.after(1000, update_time, started, iteration + 1, CYCLE_END_BREAK, 0, check_mark)
                    else:
                        update_title("Work")
                        check_mark += f"{chr(0xFC)}"
                        check_marks.configure(text=check_mark)
                        window.after(1000, update_time, started, iteration + 1, INTERVAL, 0, check_mark)
                window.after(1000, update_time, False, 0, INTERVAL, 0, check_mark)
        else:
            hrs, mins, secs = str(datetime.timedelta(seconds=interval * 60 - seconds)).split(":")
            canvas.itemconfig(time_text, text=f"{mins}:{secs}")

            if iteration == TOTAL_ITERATIONS:
                window.after(1000, update_time, started, iteration, CYCLE_END_BREAK, seconds + 1, check_mark)
            else:
                window.after(1000, update_time, started, iteration, interval, seconds + 1, check_mark)
    else:
        window.after(1000, update_time, started, iteration, interval, 0, check_mark)


def update_title(title_arg):
    title_text.configure(text=f"{title_arg}")


check_mark_text = f"{chr(0xFC)}"
title = "Work"
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)

title_text = Label(text=title, font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
time_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
check_marks = Label(text=check_mark_text, font=("WINGDINGS", 20, "normal"), bg=YELLOW, fg=GREEN, highlightthickness=0)
title_text.grid(row=0, column=1)
canvas.grid(row=1, column=1)
check_marks.grid(row=2, column=1)
reset_button_var = BooleanVar(name="reset", value=False)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
window.mainloop()
