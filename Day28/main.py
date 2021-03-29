from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repititions = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title_label = "Timer
    timerLabel.config(text="Timer")
    #reset marks
    checkLabel.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repititions
    repititions += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's 1st/3rd/5th/7th rep:
    if repititions % 8 == 0:
        # if it's the 8th rep
        count_down(long_break_sec)
        timerLabel.config(text="Pauze", fg=RED)
    # if it the 2nd/4th/6th rep
    if repititions % 2 == 0:
        count_down(short_break_sec)
        timerLabel.config(text="Pauze", fg=PINK)
    else:
        count_down(work_sec)
        timerLabel.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(repititions / 2)
        for _ in range(work_sessions):
            mark += "✔"
        checkLabel.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
foto = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=foto)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=2, row=2)

startButton = Button(text="Start", highlightthickness=0, command=start_timer)
startButton.grid(column=1, row=3)

timerLabel = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timerLabel.grid(column=2, row=1)
checkLabel = Label(bg=YELLOW, highlightthickness=0, fg=GREEN)
checkLabel.grid(column=2, row=4)
resetButton = Button(text="Reset", highlightthickness=0,command=reset_timer)
resetButton.grid(column=3, row=3)
window.mainloop()
