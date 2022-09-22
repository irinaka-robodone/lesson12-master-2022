from secrets import choice
import tkinter as tk
import random
import time
def te():
    te=random.choice(["グー", "チョキ", "パー"])
    time.sleep(0.3)
    print(te)
#te()


root= tk.Tk()
root.title("じゃんげーむぅぅぅぅぅう（暇つぶし）")
root.geometry("250x250")

button=tk.Button(text="じゃんけん？！", command=te)
button.place(x=90,y=90)


root.mainloop()