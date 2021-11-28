from tkinter import *
from PIL import Image, ImageTk
import random
import time
from pygame import mixer
import datetime
from threading import *
from tkinter import ttk
from eye_detection import all_functions
from cam_trail import generate_gesture

root = Tk()
# root.iconbitmap('icon.ico')

root.title('MyPal')

root.geometry("1300x600")


def open_alarm():
    global rand1, rand2, entry, top2
    top2 = Toplevel()
    top2.title('Math game')
    # top2.iconbitmap('icon.ico')
    math1 = Label(top2, text='Solve To Stop:   ' + str(rand1) + '+' + str(rand2), fg='#0D7377',
                  font=("Boulder", 20, "bold"))
    math1.grid(row=0, column=0, padx=30, pady=60)
    entry = Entry(top2, text="Answer Here      ")
    entry.grid(row=1, column=0)
    b2 = Button(top2, text="Check The Answer", command=checker, padx=82, fg='white', bg='#0D7377',
                font=("Boulder", 12, "normal"))
    b2.grid(row=2, column=0, pady=30)
    mixer.init()
    mixer.music.load('Alarm-ringtone.mp3')
    mixer.music.set_volume(0,1)
    mixer.music.play()


def checker():
    if str(rand1 + rand2) == entry.get():
        math2 = Label(top2, text='Well Done! Now We Know You Are Awake', fg='#4BB543',
                      font=("Boulder", 15, "normal"))
        math2.grid(row=3, column=0, padx=30, pady=60)
        entry.delete(0, END)
        b2 = Button(top2, text="Check The Answer", command=checker, padx=82, fg='white', bg='#2F86A6', state=DISABLED,
                    font=("Boulder", 12, "normal"))
        b2.grid(row=2, column=0, pady=30)
        mixer.music.stop()

    else:
        math2 = Label(top2, text='Try Again! You Are Still Sleepy', fg='#FF0000',
                      font=("Boulder", 15, "normal"))
        math2.grid(row=3, column=0, padx=30, pady=60)
        entry.delete(0, END)


def clock():
    # global app_window
    app_window = Toplevel()
    app_window.geometry("775x610")
    app_window['bg'] = '#f5f5f5'

    def threading():
        t1 = Thread(target=alarm)
        t1.start()

    Label(app_window, text="", font="Boulder 15 bold", bg='WhiteSmoke').grid(row=3, column=1)
    Label(app_window, text="Set Time", font="Boulder 15 bold", bg='WhiteSmoke').grid(row=4, column=1)
    Label(app_window, text="", font="Boulder 15 bold", fg="red", bg='WhiteSmoke').grid(row=5, column=1)
    Label(app_window, text="Hour   Min   Sec", font="Boulder 13 normal", bg='WhiteSmoke').grid(row=6, column=1)
    Label(app_window, text="Note: enter the time in 24 format", fg='#FF0000', font="Boulder 10 italic",
          bg='WhiteSmoke').grid(row=9, column=1)

    frame = Frame(app_window, height=25, width=740)
    frame.grid(row=7, column=1)

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

    mins = ttk.OptionMenu(frame, minute, *minutes)
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
    app_window.title('Set Alarm')
    # app_window.iconbitmap('C:/Users/Abd/PycharmProjects/3339052_business tools_passing_time_alarm_schedule_icon.ico')
    # label = Label(app_window, pady=30, padx=45)
    # label.grid(row=0,column=0)
    text_font = ("Boulder", 68, 'bold')
    # background = "#6096AA"
    # background = '#a3ccbe'
    background='#26AB95'
    foreground = "#212121"
    border_width = 25
    label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width, pady=30, padx=45)
    label.grid(row=0, column=1)

    def digital_clock():
        time_live = time.strftime('%H:%M:%S %p')
        label.config(text=time_live)
        label.after(200, digital_clock)
        return time_live

    digital_clock()
    Label(app_window, text="", font="Boulder 15 bold", bg='WhiteSmoke').grid(row=10, column=1)
    Button(app_window, text="Set Alarm",padx=40, font="Boulder 12 bold",fg='white' ,command=threading, background='#0D7377',
           ).grid(row=11, column=1)

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
                Label(app_window, text="", font="Boulder 12 bold", bg='WhiteSmoke').grid(
                    row=15, column=1)
                Label(app_window, text="Stop by Playing a game", font="Boulder 12 bold", bg='WhiteSmoke').grid(
                    row=16, column=1)
                Label(app_window, text="", font="Boulder 12 bold", bg='WhiteSmoke').grid(
                    row=17, column=1)
                Label(app_window, text="OR", bg='WhiteSmoke', font="Boulder 12 bold").grid(row=19, column=1)
                Button(app_window, padx=40, background='#0D7377', text="Solve The Equation", font="Boulder 13 normal",
                       fg='white',command=open_alarm).grid(row=18, column=1)
                Button(app_window, padx=65, text="Hand Gesture", font="Boulder 13 normal", fg='white',
                       background='#0D7377', command=open_hand_gesture).grid(row=20, column=1)


def open_sleep():
    all_functions()
    # top.iconbitmap('C:/Users/Abd/PycharmProjects/3339052_business tools_passing_time_alarm_schedule_icon.ico')


def open_hand_gesture():
    generate_gesture()


rand1 = random.randrange(1, 50)
rand2 = random.randrange(1, 50)
root['bg'] = '#f5f5f5'

blank_label1 = Label(root, text="Welcome to MyPal", fg='#0D7377', background='#f5f5f5', font=("Boulder", 22, "bold"))
blank_label1.grid(row=0, column=1, padx=30, pady=50)
frame_left = LabelFrame(root, text="Alarm", padx=30, pady=30, fg='#0D7377', background='#f5f5f5',
                        font=("Boulder", 12, "normal"))
frame_left.grid(row=3, column=0, padx=100)
frame_right = LabelFrame(root, text="Sleep Detector", padx=30, pady=30, fg='#0D7377', background='#f5f5f5',
                         font=("Boulder", 12, "normal"))
frame_right.grid(row=3, column=2, padx=0)

img1 = Image.open('alarm.jpg')
resize_image = img1.resize((250, 250))
img11 = ImageTk.PhotoImage(resize_image)
label1 = Label(frame_left, image=img11)
label1.grid(row=0, column=0)

img2 = Image.open('home.jpg')
resize_image = img2.resize((250, 250))
img22 = ImageTk.PhotoImage(resize_image)
label1 = Label(frame_right, image=img22)
label1.grid(row=0, column=0)

b1 = Button(root, text="Set Alarm", command=clock, padx=115, fg='white', bg='#0D7377', font=("Boulder", 12, "bold"))
b2 = Button(root, text="Start Sleep Detector", command=open_sleep, padx=65, fg='white', bg='#0D7377',
            font=("Boulder", 12, "bold"))
b1.grid(row=4, column=0, pady=50)
b2.grid(row=4, column=2, pady=30)

root.mainloop()
