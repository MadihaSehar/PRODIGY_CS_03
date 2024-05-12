
########################################  Task-03 ####################################
##################################Password Complexity Checker##########################
import re
import tkinter as tk
from tkinter import messagebox

def password_strength(password):
    length = len(password)
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    numbers = bool(re.search(r'[0-9]', password))
    special_characters = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    strength = 0

    # Length criteria
    if length >= 8:
        strength += 1
    if length >= 12:
        strength += 1

    # Mix of uppercase and lowercase letters
    if uppercase and lowercase:
        strength += 1

    # Presence of numbers and special characters
    if numbers:
        strength += 1
    if special_characters:
        strength += 1

    return strength

def assess_password():
    password = password_entry.get()
    strength = password_strength(password)
    
    if strength <= 1:
        messagebox.showinfo("Password Strength", "Password is weak.")
    elif strength <= 3:
        messagebox.showinfo("Password Strength", "Password is moderate.")
    else:
        messagebox.showinfo("Password Strength", "Password is strong.")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create password entry widget
password_label = tk.Label(root, text="Enter your password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create assess button
assess_button = tk.Button(root, text="Assess Password", command=assess_password)
assess_button.pack()

# Run the main event loop
root.mainloop()
