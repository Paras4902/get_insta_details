from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Get Details @instagram.com")
root.wm_iconbitmap("icon.ico")
img = ImageTk.PhotoImage(Image.open("insta.png"))
root.geometry("500x500")
root.resizable(0, 0)


def get_details():
    import requests
    from bs4 import BeautifulSoup
    from tkinter import messagebox as msgbx

    def parse_data(string):
        dataa = {}
        string = string.split("-")[0]
        string = string.split(" ")
        dataa["Followers"] = string[0]
        dataa["Following"] = string[2]
        dataa["Posts"] = string[4]
        return dataa

    username = username_entry.get()
    r = requests.get(f"https://www.instagram.com/{username}/")
    s = BeautifulSoup(r.text, "html.parser")
    meta = s.find("meta", property="og:description")
    try:
        data = parse_data(meta.attrs["content"])
        followers_entry.delete(0, END)
        followers_entry.insert(END, data["Followers"])
        following_entry.delete(0, END)
        following_entry.insert(END, data["Following"])
        posts_entry.delete(0, END)
        posts_entry.insert(END, data["Posts"])
    except Exception:
        msgbx.showinfo("Invalid Name", "Username does not exist!!")
        followers_entry.delete(0, END)
        following_entry.delete(0, END)
        posts_entry.delete(0, END)


Label(root, image=img).pack(side=LEFT, anchor=N)
Label(root, text="↓@Instagram Handle↓", font="Times 22 bold").place(x=150, y=0)
username_entry = Entry(root, font="Times 22 bold")
username_entry.place(x=150, y=50, width=290)
Button(root, text="Get Details", font="Times 22 bold", bd=5, command=get_details).place(x=200, y=100)
Label(root, text="Followers:", font="Times 35 bold").place(x=10, y=200)
Label(root, text="Following:", font="Times 35 bold").place(x=10, y=280)
Label(root, text="Posts:", font="Times 35 bold").place(x=10, y=360)
Label(root, text="Program@Paras4902", font="Helvetica 25 bold italic").pack(side="bottom", anchor=E)
followers_entry = Entry(root, font="Times 22 bold")
followers_entry.place(x=250, y=210, width=150)
following_entry = Entry(root, font="Times 22 bold")
following_entry.place(x=250, y=290, width=150)
posts_entry = Entry(root, font="Times 22 bold")
posts_entry.place(x=250, y=370, width=150)
root.mainloop()
