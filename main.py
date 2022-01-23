
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_symbols = randint(2, 4)
nr_numbers = randint(2, 4)


def generate_password():
    pass_entry.delete(0, "end")
    password_list = []

    password_list += [choice(letters) for letter in range(nr_letters)]
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    password_list += [choice(symbols) for symbol in range(nr_symbols)]
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_list += [choice(numbers) for number in range(nr_numbers)]
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")

    pass_entry.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    if website == "" or user == "" or password == "":
        messagebox.askretrycancel(message="Complete all the fields, please", title="Oops")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUser/Email: {user}\n"
                                                              f"Password: {password}\nIs it ok to save?")
        if is_ok:

            f = open("data.txt", "a")
            f.write(f"\n{website} | {user} | {password}\n")
            website_entry.delete(0, "end")
            user_entry.delete(0, "end")
            pass_entry.delete(0, "end")
            f.close()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# label website
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
# label email/username
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
# label password
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# entry Website
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
# entry username
user_entry = Entry(width=38)
user_entry.grid(column=1, row=2, columnspan=2)
# user_entry.insert(0,"Type your username or email here")
# entry password
pass_entry = Entry(width=29)
pass_entry.grid(column=1, row=3)

# button Generate Password
generate_button = Button(text="Generate", highlightthickness=0, command=generate_password )
generate_button.grid(column=2, row=3)
# button Add
add_button = Button(width= 30, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()