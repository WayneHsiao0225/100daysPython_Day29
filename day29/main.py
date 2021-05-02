from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD RANDOM GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter=[random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols=[random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers=[random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list=password_letter+password_symbols+password_numbers
    random.shuffle(password_list)
    password="".join(password_list)
    input_pass.insert(0,password)

#-----------------------------SAVE PASSWORD---------------------------- #
def save():
    WEB=str(input_web.get())
    USERNAME=str(input_emailusername.get())
    PASS=str(input_pass.get())

    if len(WEB)==0 or len(USERNAME)==0 or len(PASS)==0:
        messagebox.showinfo(title="WARNING",message="Please make sure you havenot left any fields empty!")
    else:
        check_ok=messagebox.askokcancel(title="Check",message="Website: "+WEB+"\n"+"E-mail/Username: "+USERNAME+"\n"+"Password: "+PASS+"\n")
        if check_ok:
            file = open("note.txt", "a")
            file.write(WEB+"|"+USERNAME+"|"+PASS+"|"+"\n")
            input_web.delete(0,END)
            input_pass.delete(0,END)

# ---------------------------- UI  ------------------------------- #
## Window and Canvas
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas=Canvas(height=200,width=200)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

##Label
label_web=Label(text="Website:")
label_web.grid(row=1,column=0,sticky="EW")
label_emailusername=Label(text="Email/Username:")
label_emailusername.grid(row=2,column=0,sticky="EW")
label_pass=Label(text="Password:")
label_pass.grid(row=3,column=0,sticky="EW")

##Entry
input_web=Entry()
input_web.focus()
input_web.grid(row=1,column=1,columnspan=2,sticky="EW")
input_emailusername=Entry()
input_emailusername.insert(0,"wayne522048@gmail.com")
input_emailusername.grid(row=2,column=1,columnspan=2,sticky="EW")
input_pass=Entry()
input_pass.grid(row=3,column=1,sticky="EW")

##Button
button_Gen=Button(text="Generated Password",command=password_generator)
button_Gen.grid(row=3,column=2,sticky="EW")
button_Add=Button(text="Add",width=36,command=save)
button_Add.grid(row=4,column=1,columnspan=2,sticky="EW")

window.mainloop()