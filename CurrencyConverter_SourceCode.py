import tkinter as tk
from tkinter import *
import tkinter.messagebox
import requests

# Creating the main window
root = tk.Tk()
root.title("Currency Conversion using Python")
root.configure(background='#e6e5e5')
root.geometry("700x400")

# Add Header
Tops = Frame(root, bg='#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)
headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='      PythonGeeks   :    Currency Converter', bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

# Dropdown Variables
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
variable1.set("currency")
variable2.set("currency")

# API Request Function
def RealTimeCurrencyConversion():
    api_key = "your_api_key_here"  # Replace with your actual API key
    base_url = "https://api.exchangerate-api.com/v4/latest/"
    
    from_currency = variable1.get()
    to_currency = variable2.get()
    
    if Amount1_field.get() == "":
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please enter a valid amount.")
        return

    if from_currency == "currency" or to_currency == "currency":
        tkinter.messagebox.showinfo("Error !!", "Currency Not Selected.\n Please select FROM and TO Currency from menu.")
        return

    try:
        # Fetch rates
        response = requests.get(f"{base_url}{from_currency}")
        data = response.json()
        
        if response.status_code != 200 or "rates" not in data:
            raise Exception("Invalid API Response")

        # Convert amount
        rate = data["rates"][to_currency]
        amount = float(Amount1_field.get())
        converted_amount = round(amount * rate, 4)

        # Display result
        Amount2_field.delete(0, tk.END)
        Amount2_field.insert(0, str(converted_amount))
    
    except Exception as e:
        tkinter.messagebox.showinfo("Error !!", f"Failed to fetch conversion rate: {e}")

# Clear Input Fields
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)

# Currency Codes
CurrenyCode_list = ["USD", "INR", "EUR", "GBP", "CAD", "AUD"]

# UI Design
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)

FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

ConvertButton = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="light blue", fg="white", command=RealTimeCurrencyConversion)
ConvertButton.grid(row=6, column=0)

ClearButton = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="light blue", fg="white", command=clear_all)
ClearButton.grid(row=10, column=0)

root.mainloop()
