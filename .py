import tkinter as tk
from tkinter import messagebox

def calculate_iron_condor():
    try:
        # Retrieve user inputs
        account_size = float(account_size_entry.get())
        short_put_strike = float(short_put_entry.get())
        long_put_strike = float(long_put_entry.get())
        short_call_strike = float(short_call_entry.get())
        long_call_strike = float(long_call_entry.get())
        credit_put = float(credit_put_entry.get())
        debit_put = float(debit_put_entry.get())
        credit_call = float(credit_call_entry.get())
        debit_call = float(debit_call_entry.get())
        contracts = int(contracts_entry.get())
        
        # Calculate max profit and max loss
        total_credit = (credit_put - debit_put + credit_call - debit_call) * contracts
        max_loss_put = (short_put_strike - long_put_strike - (credit_put - debit_put)) * contracts
        max_loss_call = (long_call_strike - short_call_strike - (credit_call - debit_call)) * contracts
        max_loss = max(max_loss_put, max_loss_call)
        max_profit = total_credit
        percent_risk = (max_loss / account_size) * 100

        # Display results
        result_text.set(f"Max Profit: £{max_profit:.2f}\n"
                        f"Max Loss: £{max_loss:.2f}\n"
                        f"Risk (% of Account): {percent_risk:.2f}%")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for all fields.")

# Initialize GUI
root = tk.Tk()
root.title("Iron Condor Calculator")

# Input Fields
tk.Label(root, text="Account Size (£):").grid(row=0, column=0, sticky="e")
account_size_entry = tk.Entry(root)
account_size_entry.grid(row=0, column=1)

tk.Label(root, text="Short Put Strike:").grid(row=1, column=0, sticky="e")
short_put_entry = tk.Entry(root)
short_put_entry.grid(row=1, column=1)

tk.Label(root, text="Long Put Strike:").grid(row=2, column=0, sticky="e")
long_put_entry = tk.Entry(root)
long_put_entry.grid(row=2, column=1)

tk.Label(root, text="Short Call Strike:").grid(row=3, column=0, sticky="e")
short_call_entry = tk.Entry(root)
short_call_entry.grid(row=3, column=1)

tk.Label(root, text="Long Call Strike:").grid(row=4, column=0, sticky="e")
long_call_entry = tk.Entry(root)
long_call_entry.grid(row=4, column=1)

tk.Label(root, text="Credit for Short Put (£):").grid(row=5, column=0, sticky="e")
credit_put_entry = tk.Entry(root)
credit_put_entry.grid(row=5, column=1)

tk.Label(root, text="Debit for Long Put (£):").grid(row=6, column=0, sticky="e")
debit_put_entry = tk.Entry(root)
debit_put_entry.grid(row=6, column=1)

tk.Label(root, text="Credit for Short Call (£):").grid(row=7, column=0, sticky="e")
credit_call_entry = tk.Entry(root)
credit_call_entry.grid(row=7, column=1)

tk.Label(root, text="Debit for Long Call (£):").grid(row=8, column=0, sticky="e")
debit_call_entry = tk.Entry(root)
debit_call_entry.grid(row=8, column=1)

tk.Label(root, text="Number of Contracts:").grid(row=9, column=0, sticky="e")
contracts_entry = tk.Entry(root)
contracts_entry.grid(row=9, column=1)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_iron_condor)
calculate_button.grid(row=10, column=0, columnspan=2)

# Result Display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), fg="blue", justify="left")
result_label.grid(row=11, column=0, columnspan=2)

# Run the application
root.mainloop()
