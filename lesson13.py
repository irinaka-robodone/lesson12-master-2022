from email.errors import MessageError
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# def get_filepth():
#     filetype_list=[("all file","*")]
#     filepath=filedialog.askopenfilename(initialdir="/",filetypes=filetype_list)
#     print(filepath)
#     # message["text"]=filepath

# root = tk.Tk()
# root.title("あああ")
# root.geometry("698x435")

# bt=tk.Button(text="boakjvoibdigjm,v.sgjubfhc",command=get_filepth)
# bt.pack()

def msg_warning():
    ret=label["text"]=str(messagebox.showinfo("info"," インフォメーションです"))
    print(ret)
    
def msg_info():
    ret=label["text"]=str(messagebox.showinfo("info","インフォメーションです"))
    print(ret)
def msg_warning():
    ret=labil["text"]=str(messagebox.showwarning("warning","警告！"))
def msg_error():
    ret=label["text"]=str(messagebox.showerror("error","エラーです！"))
    print(ret)
def msg_puestion():
    ret=label["text"]=ser(messagebox.askpuestion("puestion","質問です！"))
    print(ret)
def msg_yesno():
    ret=messagebox.askyesno("yesno","はい？いいえ？どちらですか")
    print(ret)
    if ret==True:
        label["text"]="yes"
    else:
        label["text"]="no"
def msg_okcancel():
    ret=messagebox.askokcancel("okcancel","OK？Cancel")
    print(ret)
    if ret==True:
        label["text"]="OK"
    else:
        label["text"]="cancel"
root = tk.Tk()
root.title("タイトルです")
root.geometry("300x500")

labe1=tk.Label(text="message")
bt1=tk.Button(text="info",command=msg_info)
bt2=tk.Button(text="warning",command=msg_warning)
bt1.pack()
bt2.pack()

root.mainloop();;;;;