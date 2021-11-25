from tkinter import *
import time
import datetime
from threading import *

# Clock Timer
from pygame import mixer

app_window = Tk()
app_window.title("Set Timer")
app_window.geometry("520x650")
app_window.resizable(1, 3)

text_font = ("Boulder", 68, 'bold')
background = "#6096AA"
foreground = "#363529"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width, pady=30, padx=45)
label.pack()


def digital_clock():
    time_live = time.strftime('%H:%M %p')
    label.config(text=time_live)
    label.after(200, digital_clock)
    return time_live


digital_clock()


def threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    while True:

        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            print("Time to Wake up")

            mixer.init()
            mixer.music.load("Alarm-ringtone.mp3")
            mixer.music.play()

            Label(app_window, text="Stop by Playing a game", font="Boulder 12 bold").pack()

            Button(app_window, bg='#6096AA', text="stop", font="Boulder 15 bold", command=mixer.music.stop).pack()
            Button(app_window, bg='#6096AA', text="Math", font="Boulder 15 bold").pack(side=LEFT, expand=True)
            Button(app_window, bg='#6096AA', text="f?", font="Boulder 15 bold", activebackground='yellow').pack(
                side=LEFT, expand=True)


Label(app_window, text="", font="Boulder 15 bold", fg="red").pack(pady=10)
Label(app_window, text="Set Time", font="Boulder 15 bold").pack(pady=10)
Label(app_window, text="Hour   Min   Sec", font="Boulder 14 bold").pack()

frame = Frame(app_window)
frame.pack()

hour = StringVar(app_window)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(app_window)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(app_window)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(app_window, text="Set Alarm", font="Boulder 15 bold", command=threading).pack(pady=20)
# Label(app_window, text="Snooze by Playing a game", font="Boulder 12 bold").pack()
# Button(app_window,bg='#6096AA', text="Math", font="Boulder 15 bold").pack(side=LEFT, expand=True)
# Button(app_window,bg='#6096AA', text="f?", font="Boulder 15 bold",activebackground='yellow').pack(side=LEFT,  expand=True)

app_window.mainloop()
