import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import Menu

# Global variables for conversion rates
us_to_cad_rate = 1.36  # Default rate
cad_to_us_rate = 1 / us_to_cad_rate

def update_rates(new_us_to_cad=None, new_cad_to_us=None):
    global us_to_cad_rate, cad_to_us_rate
    if new_us_to_cad is not None:
        us_to_cad_rate = new_us_to_cad
        cad_to_us_rate = 1 / new_us_to_cad
    elif new_cad_to_us is not None:
        cad_to_us_rate = new_cad_to_us
        us_to_cad_rate = 1 / new_cad_to_us

def clear_fields():
    amount_entry.delete(0, tk.END)
    result_label.config(text="Result:")

def exit_program():
    """Exit the program."""
    root.destroy()

def set_us_to_cad_rate():
        try:
        new_rate = float(simpledialog.askstring("Set US to Canadian Rate", "Enter new US to Canadian rate:"))
        update_rates(new_us_to_cad=new_rate)
        messagebox.showinfo("Rate Updated", f"New rate: 1 USD = {us_to_cad_rate:.2f} CAD")
    except (TypeError, ValueError):
        messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

def set_cad_to_us_rate():
    """Prompt the user to set a new Canadian to US rate."""
    try:
        new_rate = float(simpledialog.askstring("Set Canadian to US Rate", "Enter new Canadian to US rate:"))
        update_rates(new_cad_to_us=new_rate)
        messagebox.showinfo("Rate Updated", f"New rate: 1 CAD = {cad_to_us_rate:.2f} USD")
    except (TypeError, ValueError):
        messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

def show_about():
    """Display the About window."""
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("300x200")
    
    tk.Label(about_window, text="Currency Converter", font=("Arial", 14)).pack(pady=10)
    tk.Label(about_window, text="Created by: Wada Tafesse", font=("Arial", 12)).pack()
    tk.Label(about_window, text="Date: January 21 2025", font=("Arial", 12)).pack()

    img = tk.PhotoImage(file="me.jng")
    tk.Label(about_window, image=img).pack(pady=10)
    about_window.mainloop()

def convert_currency():
    """Convert the input amount based on the selected conversion direction."""
    try:
        amount = float(amount_entry.get())
        if conversion_var.get() == "us_to_cad":
            result = amount * us_to_cad_rate
            result_label.config(text=f"Result: {amount} USD = {result:.2f} CAD")
        elif conversion_var.get() == "cad_to_us":
            result = amount * cad_to_us_rate
            result_label.config(text=f"Result: {amount} CAD = {result:.2f} USD")
        else:
            messagebox.showerror("Error", "Please select a conversion direction.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

# Main Window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Menu
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear", command=clear_fields)
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)

rate_menu = Menu(menu_bar, tearoff=0)
rate_menu.add_command(label="US to Canadian", command=set_us_to_cad_rate)
rate_menu.add_command(label="Canadian to US", command=set_cad_to_us_rate)
menu_bar.add_cascade(label="Rates", menu=rate_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Widgets
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

conversion_var = tk.StringVar(value="us_to_cad")
tk.Radiobutton(root, text="US to Canadian", variable=conversion_var, value="us_to_cad").grid(row=1, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Canadian to US", variable=conversion_var, value="cad_to_us").grid(row=1, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=2, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="Result:", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
