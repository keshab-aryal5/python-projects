from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip


def searchinfo():
    website_value = website_entry.get().lower()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
            if website_value in data.keys():
                email_value = data[website_value]["email"]
                password_value = data[website_value]["password"]
                messagebox.showinfo(title=f"{website_value}",message=f"email:{email_value}\npassword:{password_value}\nPassword copied to clipboard.")
                pyperclip.copy(password_value)
            else:
                messagebox.showinfo(title="Oops",message=f"No data found for the website {website_value}")
    except FileNotFoundError:
        messagebox.showwarning(title="Oops",message="No data available")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    password_entry.delete(0,END)
    passkey = []
    passw = ""

    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = [x for x in range(0, 10)]
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '|', '\\', '~', '`', ':', ';',
                          '"',
                          "'", '<', '>', '/', '?', ',', '.']

    for i in range(random.randint(2, 4)):
        passkey.append(random.choice(special_characters))

    for i in range(random.randint(2, 4)):
        passkey.append(random.choice(num))

    for i in range(random.randint(8, 10)):
        passkey.append(random.choice(alpha))

    for i in range(random.choice(num)):
        random.shuffle(passkey)

    passkey = [str(x) for x in passkey]
    passw = "".join(passkey)

    password_entry.insert(0,passw)
    pyperclip.copy(passw)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    code = password_entry.get()
    email = email_entry.get()
    web = website_entry.get().lower()

    if len(code) and len(email) and len(web):
        is_okey = messagebox.askokcancel(title=web,
                                        message=f"These are the details entered:\nEmail: {email}\nPassword: {code}\nIs "
                                                f"it okey to save? ")
        if is_okey:
            new_data = {
                web:{
                    "email":email,
                    "password":code
                }
            }
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json","w")as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                with open("data.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                password_entry.delete(0, END)
                website_entry.delete(0, END)
                email_entry.delete(0,END)
                email_entry.insert(0,"keshabaryal152@gmail.com")

    else:
        messagebox.showerror(title="Oops",message="You cann't have empty entries")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

window.config(padx=50,pady=50,highlightthickness=0)
canvas = Canvas(width=200,height=200)

image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)

canvas.grid(row=0,column=1)

# label
website = Label(text="Website")
website.grid(row=1,column=0)

Email = Label(text="Email/Username")
Email.grid(row=2,column=0)

password = Label(text="Password")
password.grid(row=3,column=0)


# Entry
website_entry = Entry()
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"keshabaryal152@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# Button
generate_password = Button(text="Generate Password",command=generate)
generate_password.grid(row=3,column=2)

add = Button(text="Add",width=35,command=save)
add.grid(row=4,column=1,columnspan=2)

search = Button(text="Search",width=15,command=searchinfo)
search.grid(row=1,column=2)


window.mainloop()
