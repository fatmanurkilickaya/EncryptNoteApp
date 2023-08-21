import tkinter
from tkinter import END

#from PIL import ImageTk, Image

window = tkinter.Tk()
window.title("Secret Note")
window.config(padx =30, pady=30)

def saveEncryptNote():
    title_input_get = title_input.get()
    secret_input_get = secret_input.get('1.0', END)
    with open("myNote.txt", "w") as my_file:
        my_file.write(title_input.get())
        my_file.write(secret_input.get('1.0', END))

    title_input.delete(0, 'end')
    secret_input.delete('1.0', END)


#ui

image1 = Image.open("venv/Fig/PngItem_4746699.png")
resized_image= image1.resize((100,100), Image.Resampling.LANCZOS)
show = ImageTk.PhotoImage(resized_image)
image_input = tkinter.Label(image=show)
image_input.pack()

title_input_label = tkinter.Label(text="Enter your title")
title_input_label.pack()

title_input = tkinter.Entry(width=20)
title_input.pack()

secret_input_label = tkinter.Label(text="Enter your Secret")
secret_input_label.pack()

secret_input = tkinter.Text(width=30, height=10)
secret_input.pack()

master_key_input_label = tkinter.Label(text="Enter master key")
master_key_input_label.pack()

master_key_input = tkinter.Entry(width=20)
master_key_input.pack()

encrypt_button = tkinter.Button(text="Save & Encrypt", command=saveEncryptNote)
encrypt_button.pack()

decrypt_button = tkinter.Button(text="Decrypt")
decrypt_button.pack()

window.mainloop()
