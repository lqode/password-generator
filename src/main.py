from tkinter import *
from tkinter import messagebox
import random
# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    # pyperclip.copy(password)  # to enable copy to clipboard automatically

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = input_website.get()
    email_text = input_email.get()
    password_text = input_password.get()

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # messagebox.showinfo(title="Title", message="Message")
        is_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \nEmail: {email_text} \n"
                                                           f"Password: {password_text} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", 'a') as file:
                file.write(f"{website_text} | {email_text} | {password_text}\n")

            # delete text in website and password
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image_logo = PhotoImage(file="../logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
input_website = Entry(width=38)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()
input_email = Entry(width=38)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "lopa@email.com")
input_password = Entry(width=21)
input_password.grid(row=3, column=1)

# Buttons
button_generate_pw = Button(text="Generate Password", command=generate_password)
button_generate_pw.grid(row=3, column=2)
button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
