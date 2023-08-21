from tkinter import *
from tkinter import messagebox
import base64
#https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
def save_and_encrypt_notes():
    title = title_info.get()
    message = input_info.get('1.0', END)
    master = master_secret.get()

    if len(title) == 0 or len(message) == 0 or len(master) == 0:
        messagebox.showinfo(title="Error", message="Please enter all info.")
    else:
        #encryption
        message_encrypted = encode(master, message)
        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")

        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f"\n{title}\n{message}")

        finally:
            title_info.delete(0, END)
            input_info.delete('1.0', END)
            master_secret.delete(0, END)

def decrypt_notes():
    message_encrypted = input_info.get('1.0', END)
    master_secret_encryped = master_secret.get()

    if(message_encrypted) == 0 or len(master_secret_encryped) == 0:
        messagebox.showinfo(title="Error!", message = "Please enter all info.")
    else:
        try:
            decrypted_message = decode(master_secret_encryped, message_encrypted)
            input_info.delete("1.0", END)
            input_info.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error", message="Please enter encryted text!")



#ui

FONT =("Verdena", 20, "normal")
window = Tk()
window.title("Secret Notes")
window.config(padx=30, pady=30)

photo = PhotoImage(file="img_1.png")
photo_label = Label(image=photo)
photo_label.pack()

'''''
canvas = Canvas(height=200, width=200)
canvas.create_image(100,100, image= photo)
canvas.pack()
'''

title_info_label = Label(text="Enter your title", font=FONT)
title_info_label.pack()

title_info = Entry(width=30)
title_info.pack()

input_info_label = Label(text="Enter your secret", font=FONT)
input_info_label.pack()

input_info = Text(width=40, height=20)
input_info.pack()

master_secret_label = Label(text="Enter master key", font=FONT)
master_secret_label.pack()

master_secret = Entry(width=30)
master_secret.pack()

save_button = Button(text="Save & Encrypt", command=save_and_encrypt_notes)
save_button.pack()

decrypt_button = Button(text="Decrypt", command=decrypt_notes)
decrypt_button.pack()








window.mainloop()
