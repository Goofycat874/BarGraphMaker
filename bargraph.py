import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def plot_bar_graph(x, y):
    colors = plt.cm.Paired(np.linspace(0, 1, len(x)))
    plt.figure(figsize=(12, 6))
    bars = plt.bar(x, y, color=colors, edgecolor='black', linewidth=1.2)
    
    plt.title('User Defined Bar Graph', fontsize=16, fontweight='bold', color='darkblue')
    plt.xlabel('Categories', fontsize=14, fontweight='bold', color='green')
    plt.ylabel('Values', fontsize=14, fontweight='bold', color='green')

    plt.grid(axis='y', linestyle='--', alpha=0.7, color='gray')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}', ha='center', va='bottom', fontsize=12, color='black')

    plt.tight_layout()
    plt.show()

def on_plot_button_click():
    x_values = entry_x.get()
    y_values = entry_y.get()

    if not x_values or not y_values:
        messagebox.showerror("Input Error", "Enter both values")
        return
    
    try:
        x = [val.strip() for val in x_values.split(',')]
        y = [float(val.strip()) for val in y_values.split(',')]
        
        if len(x) != len(y):
            messagebox.showerror("Input Error", "x and y need to have the same elements")
            return
        
        plot_bar_graph(x, y)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for Y.")
        
root = tk.Tk()
root.title("Bar Graph Input")

label_x = tk.Label(root, text="Enter categories for the X-axis (comma-separated):")
label_x.grid(row=0, column=0, padx=10, pady=10)

entry_x = tk.Entry(root, width=40)
entry_x.grid(row=0, column=1, padx=10, pady=10)

label_y = tk.Label(root, text="Enter values for the Y-axis (comma-separated):")
label_y.grid(row=1, column=0, padx=10, pady=10)

entry_y = tk.Entry(root, width=40)
entry_y.grid(row=1, column=1, padx=10, pady=10)

plot_button = tk.Button(root, text="Plot Bar Graph", command=on_plot_button_click)
plot_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
