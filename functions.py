#Countdowntimer, Function File
#Credit Emil Gungaard/BeHeard - 28. May 2022
#Inspiration from https://stackoverflow.com/questions/53485957/python-gui-countdown-timer-dont-use-classes


import tkinter as tk
from datetime import timedelta
import time
import tkinter.font as tkFont




def main(min, sec, background_color, text_color, text_font,pad_vertical, pad_horison):
    def set_time(minutes:int=0, seconds:int=0):
        end = timedelta(minutes=minutes, seconds=seconds)
        one_second = timedelta(seconds=1)
        result = end - one_second
        new_time = seconds_to_hms(result.seconds)
        if result.seconds == 0:
            minutes, seconds = new_time.get('minutes'), new_time.get('seconds')
            time.set(str(minutes).zfill(2)+':'+str(seconds).zfill(2))
            root.update()
            return
            
            
        else:
            minutes, seconds = new_time.get('minutes'), new_time.get('seconds')
            time.set(str(minutes).zfill(2)+':'+str(seconds).zfill(2))
            root.update()
            root.after(1000, lambda : set_time(minutes, seconds))

    def seconds_to_hms(seconds:int) -> dict:
        minutes, seconds = 0, seconds
        if seconds >= 60:
            minutes = seconds//60
            seconds = seconds - minutes*60
        result = {'minutes': minutes, 'seconds': seconds}
        return result

    def quit(*args):
        root.destroy()

    root = tk.Tk()
    root.title(string='Timer')
    time = tk.StringVar()
    root.configure(background= background_color)
    # logo = tk.PhotoImage(file='Logo.png')
    #lbl_logo = tk.Label(root, image=logo, bg='black').pack(side='right')
    #lbl_timer = tk.Label(root, padx=10, text="Timer", fg='white', bg='black', font='Times 24', anchor='center').pack()
    lbl_time = tk.Label(root, pady = pad_vertical, padx = pad_horison , textvariable=time, font= text_font, fg=text_color , bg=background_color ,anchor='center').pack() #changed text to textvariable
    #btn_start = tk.Button(root, text='start', bg='gray', fg='black', command=lambda :set_time(0,0,3700)).pack()
    root.bind('x', quit)
    root.after(1000, lambda : set_time(min,sec))
    root.mainloop()

if __name__ == '__main__':
    main()
