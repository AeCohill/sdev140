import tkinter as tk
from tkinter import messagebox

class TaxCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Annual Tax Calculator")

        self.tax_label = tk.Label(root, text="Enter Tax Amount:")
        self.tax_label.pack()

        self.tax_entry = tk.Entry(root)
        self.tax_entry.pack()

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_tax)
        self.calculate_button.pack()

    def calculate_tax(self):
        try:
            tax_amount = float(self.tax_entry.get())
            annual_tax_with_interest = tax_amount * 1.013  # Applying 1.3% interest
            messagebox.showinfo("Result", f"Annual Tax with 1.3% Interest: ${annual_tax_with_interest:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid tax amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaxCalculatorGUI(root)
    root.mainloop()
