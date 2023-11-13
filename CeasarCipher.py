#for in depth comments go on https://github.com/wobomagondarr/ccipher#readme

import tkinter as tk
import string

def encrypt():
    shift = int(shift_entry.get())
    shift = shift % 26
    chars = string.ascii_lowercase
    key = [chr((ord(c) - ord('a') + shift) % 26 + ord('a')) for c in chars]
    plain_text = input_text.get("1.0", "end-1c")
    cipher_text = ""

    for letter in plain_text:
        if letter in chars:
            index = chars.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter

    result_text.config(fg="dark green")
    result_text.delete("1.0", "end")
    result_text.insert("1.0", cipher_text)

def decrypt():
    shift = int(shift_entry.get())
    shift = shift % 26
    chars = string.ascii_lowercase
    key = [chr((ord(c) - ord('a') - shift) % 26 + ord('a')) for c in chars]
    cipher_text = input_text.get("1.0", "end-1c")
    plain_text = ""

    for letter in cipher_text:
        if letter in key:
            index = key.index(letter)
            plain_text += chars[index]
        else:
            plain_text += letter

    result_text.config(fg="dark green")
    result_text.delete("1.0", "end")
    result_text.insert("1.0", plain_text)

window = tk.Tk()
window.title("Caesar Cipher Encryption/Decryption")
window.geometry("500x700")
window.configure(bg="dark grey")

introduction_label = tk.Label(window, text="Enter a shift value between 1 to infinite and a message, then click Encrypt.", bg="dark grey")
introduction_label.pack()
instructions_label = tk.Label(window, text="Ex: If you encrypt with 251, you decrypt the encrypted message with -251", bg="dark grey")
instructions_label.pack()

shift_label = tk.Label(window, text="Enter the shift value below, make sure to avoid 26 and its multiples:", bg="dark grey")
shift_label.pack()
shift_entry = tk.Entry(window)
shift_entry.pack()

input_label = tk.Label(window, text="Enter a message:", bg="dark grey")
input_label.pack()
input_text = tk.Text(window, width=50, height=15)
input_text.pack()

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)
encrypt_button.pack()
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt)
decrypt_button.pack()

result_text = tk.Text(window, width=50, height=15)
result_text.pack()

introduction_label = tk.Label(window, text="Created by Wobomagondarr", bg="dark grey")
introduction_label.pack()

window.mainloop()
