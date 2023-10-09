from tkinter import *
import math
from PIL import ImageTk,Image

WORK_MIN=25
S_BREAK=5
L_BREAK=20
counter=0
timer=None

def start_timer():
    start_button['state']= 'disabled'
    global counter
    counter+=1
    
    work_sec=WORK_MIN*60
    s_break_sec=S_BREAK*60
    l_break_sec=L_BREAK*60
    
    if counter % 8==0:
        count_down(l_break_sec)
        title.config(text='')
        title_label.config(text='Long Break',fg="#34280c")
        
    elif counter % 2 ==0:
        count_down(s_break_sec)
        title.config(text='')
        title_label.config(text='Short Break',fg="#34280c")
        
    else:
        count_down(work_sec)
        title.config(text='')
        title_label.config(text='Work',fg="#34280c")
        
def count_down(count):
    count_min,count_sec=divmod(count,60)
    canvas.itemconfig(timer_text,text=f"{count_min:02d}:{count_sec:02d}")
    
    if count>0:
        global timer
        timer=root.after(1000,count_down,count-1)
        
    else:
        start_timer()
        ticks=''
        sessions=math.floor(counter/2)
        for i in range(sessions):
            ticks+='✓'
        check_marks.config(text=ticks)    
        

def reset_timer():
    start_button['state']='normal'
    root.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title.config(text="Pomodoro",fg="#34280c")
    title_label.config(text="    Timer    ",fg="#34280c")
    
    check_marks.config(text='')
    
    global counter
    counter=0
    
    
    

root = Tk()
root.title("Pomodoro Timer Application")
root.config(padx=100, pady=50, bg="#977423")

title=Label(text="Pomodoro", fg='#34280c', bg="#977423", font=("Arial", 50))
title.grid(column=1,row=0)
title_label = Label(text=" Timer  ", fg='#34280c', bg="#977423", font=("Arial", 50))
title_label.grid(column=1, row=1,padx=20,pady=20)

canvas = Canvas(width=200, height=200,highlightthickness=0,bg="#977423")
pomodoro_image = ImageTk.PhotoImage(Image.open("pomodoro.png").resize((175,175)))
canvas.create_image(100, 112,image=pomodoro_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 35, "bold"))
canvas.grid(column=1, row=2,padx=20,pady=20)

start_button = Button(text="Start", command=start_timer, bg="#2e230a",fg='white', font=("arial", 15, "bold"))
start_button.grid(column=0, row=3,padx=20,pady=20)

reset_button = Button(text="Reset", command = reset_timer, bg="#2e230a", fg='white',font=("arial", 15, "bold"))
reset_button.grid(column=2, row=3,padx=20,pady=20)

check_marks = Label(text="", fg='#34280c', bg="#977423", font=("arial", 25, "bold"))
check_marks.grid(column=1, row=4)

root.mainloop()
