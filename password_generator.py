# password_generator.py
# A GUI-based Password Generator using Tkinter to create secure passwords with customizable options.

from tkinter import *
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg="light yellow")

        # Variables
        self.length_var = IntVar(value=12)
        self.include_upper = BooleanVar(value=True)
        self.include_lower = BooleanVar(value=True)
        self.include_digits = BooleanVar(value=True)
        self.include_special = BooleanVar(value=True)
        self.password_var = StringVar()

        # GUI Elements
        Label(self.root, text="Password Generator", font=("Arial", 16, "bold"), bg="light yellow").pack(pady=10)

        # Length Entry
        Label(self.root, text="Password Length:", bg="light yellow").pack()
        Entry(self.root, textvariable=self.length_var, width=10, justify="center").pack(pady=5)

        # Checkboxes for character types
        Checkbutton(self.root, text="Include Uppercase Letters", variable=self.include_upper, bg="light yellow").pack(anchor="w", padx=20)
        Checkbutton(self.root, text="Include Lowercase Letters", variable=self.include_lower, bg="light yellow").pack(anchor="w", padx=20)
        Checkbutton(self.root, text="Include Digits", variable=self.include_digits, bg="light yellow").pack(anchor="w", padx=20)
        Checkbutton(self.root, text="Include Special Characters", variable=self.include_special, bg="light yellow").pack(anchor="w", padx=20)

        # Password Display
        Entry(self.root, textvariable=self.password_var, state="readonly", width=30, font=("Arial", 12)).pack(pady=10)

        # Buttons
        button_frame = Frame(self.root, bg="light yellow")
        button_frame.pack(pady=10)
        Button(button_frame, text="Generate Password", command=self.generate_password, bg="blue", fg="white", width=15).pack(side=LEFT, padx=5)
        Button(button_frame, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="green", fg="white", width=15).pack(side=LEFT, padx=5)

    def generate_password(self):
        length = self.length_var.get()
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 characters!")
            return

        chars = ""
        if self.include_upper.get():
            chars += string.ascii_uppercase
        if self.include_lower.get():
            chars += string.ascii_lowercase
        if self.include_digits.get():
            chars += string.digits
        if self.include_special.get():
            chars += string.punctuation

        if not chars:
            messagebox.showerror("Error", "At least one character type must be selected!")
            return

        password = "".join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")

if __name__ == "__main__":
    root = Tk()
    app = PasswordGenerator(root)
    root.mainloop()
