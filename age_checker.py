import tkinter as tk
from tkinter import messagebox

# Function to check age
def check_age():
    try:
        # Get the input from the textbox
        age = int(age_entry.get())

        # Validate age and display result with colors
        if age < 0:
            messagebox.showerror("Error", "Age cannot be negative!")
        elif age < 18:
            result_label.config(text="You are a Minor.", fg="blue", bg="#ADD8E6")
        else:
            result_label.config(text="You are an Adult.", fg="green", bg="#90EE90")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Create the main application window
app = tk.Tk()
app.title("Colorful Age Checker")
app.geometry("350x250")  # Set the size of the window
app.configure(bg="#FFE4B5")  # Set the background color of the app

# Instruction Label
instruction_label = tk.Label(
    app,
    text="Enter your age and click Check:",
    font=("Arial", 14),
    bg="#FFE4B5",  # Matching background
    fg="#8B4513",  # Brown text color
)
instruction_label.pack(pady=10)

# Entry box for age input
age_entry = tk.Entry(app, width=15, font=("Arial", 14), bg="#FFFFE0", fg="#000000")
age_entry.pack(pady=5)

# Button to check age
check_button = tk.Button(
    app,
    text="Check",
    command=check_age,
    font=("Arial", 12, "bold"),
    bg="#FFD700",  # Golden background
    fg="#000000",  # Black text
    activebackground="#FFA500",  # Orange when clicked
    activeforeground="#FFFFFF",  # White text when clicked
)
check_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(
    app,
    text="",
    font=("Arial", 16, "bold"),
    bg="#FFE4B5",  # Background matching the app
)
result_label.pack(pady=10)

# Run the Tkinter event loop
app.mainloop()
