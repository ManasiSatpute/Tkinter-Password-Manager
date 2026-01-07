from tkinter import *
from generate_password import generate_password
from tkinter import messagebox
# ---------------------------- Generate Paasword ------------------------------- #
def generate_pass():
     password =generate_password()
     password_entry.delete(0 , END)
     password_entry.insert(0 , password)


# ---------------------------- Save Paasword ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if website_entry =="" or password_entry=="":
       messagebox.showinfo(title="OOPS",message="Do not leave any field empty empty")
    
    else:
        is_ok = messagebox.askokcancel(title=website , message=f"These are the details entered: \nEmail :{email}"
                           f"\nPassword: {password}\nIs it ok to save ?")
    
        if is_ok:
          with open("data.txt" ,"a") as data_file:
              data_file.write(f"{website} |{email}|{password}\n")
              website_entry.delete(0 , END)
              password_entry.delete(0 , END)
    

          


   







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.call("tk", "scaling", 1.0)
window.title("Password Manager")
window.configure(padx=50, pady=50, bg="white")

# Logo
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3, pady=(0, 20))

# Labels
website_label = Label(text="Website:", fg="black", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", fg="black", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", fg="black", bg="white")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35, bg="white", fg="black", insertbackground="black")
website_entry.grid(row=1, column=1, columnspan=2)

website_entry.focus()

email_entry = Entry(width=35, bg="white", fg="black", insertbackground="black")

email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"manasi@gmail.com")
password_entry = Entry(width=21, bg="white", fg="black", insertbackground="black")
password_entry.grid(row=3, column=1)

# Buttons
generate_password_btn = Button(text="Generate Password", bg="white", fg="black",command=generate_pass)
generate_password_btn.grid(row=3, column=2, padx=(10, 0), pady=5)

add_button = Button(text="Add", bg="white", fg="black", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=(15, 0))
window.mainloop()
