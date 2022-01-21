


from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
# window.geometry('220x220')
window.config(padx=35, pady=35)

#canvas
canvas = Canvas(width=200, height=200, bg="white" )
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
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
# entry username

# entry password

# button Generate Password

# button Add
add_button = Button(width= 36, text="Add", highlightthickness=0, )
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()