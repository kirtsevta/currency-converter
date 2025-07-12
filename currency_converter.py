from tkinter import *
from tkinter import ttk

converter = Tk()
converter.geometry("500x350")
converter.title("Currency Converter")
# converter.wm_iconbitmap("cc.ico")  # Uncomment if valid icon is there

OPTIONS = {
    "Australian Dollar": 49.10,
    "Brazilian Real": 17.30,
    "British Pound": 90.92,
    "Bulgarian Lev": 39.80,
    "Chinese Yuan": 10.29,
    "Euro": 77.85,
    "HongKong Dollar": 8.83,
    "Indonesian Rupiah": 0.004864,
    "Japanese Yen": 0.628,
    "Pakistani Rupee": 0.49,
    "SriLankan Rupee": 0.39,
    "Swiss Franc": 69.62,
    "US Dollar": 69.32
}

appName = Label(converter, text="Currency", font=("Arial", 20, "bold"), fg="dark red")
appName.grid(row=0, column=0, padx=10)

# photo = PhotoImage(file="cc.png")
# logo = Label(converter, image=photo)
# logo.grid(row=0, column=1)
logo = Label(converter, text="💱", font=("Arial", 18))
logo.grid(row=0, column=1)

appName2 = Label(converter, text="Converter", font=("Arial", 20, "bold"), fg="dark red")
appName2.grid(row=0, column=2, padx=10)

result = Text(converter, height=5, width=60, font=("Arial", 10, "bold"), bd=5)
result.grid(row=1, columnspan=10, padx=3, pady=5)

# Conversion type label
conversion_type = Label(converter, text="Choose Conversion Type", font=("Arial", 10, "bold"), fg="red")
conversion_type.grid(row=2, column=0, pady=5)

type_var = StringVar()
type_var.set("INR to Other")  # Default

# Conversion type options
type_menu = OptionMenu(converter, type_var, "INR to Other", "Other to INR")
type_menu.grid(row=2, column=1, sticky=W+E)

# Amount Entry
amount_label = Label(converter, text="Enter Amount", font=("Arial", 10, "bold"), fg="red")
amount_label.grid(row=3, column=0)
amount_entry = Entry(converter, font=("calibri", 10))
amount_entry.grid(row=3, column=1)

# Country selection
choice = Label(converter, text="Select Country", font=("Arial", 10, "bold"), fg="red")
choice.grid(row=4, column=0)
Variable = StringVar(converter)
Variable.set("Select")
optin = OptionMenu(converter, Variable, *OPTIONS.keys())
optin.grid(row=4, column=1, sticky=W+E)

# Convert Button Function
def convert():
    amount = amount_entry.get()
    country = Variable.get()
    direction = type_var.get()
    
    if amount.replace(".", "").isdigit() and country in OPTIONS:
        value = float(amount)
        rate = OPTIONS[country]
        
        result.delete(1.0, END)
        
        if direction == "INR to Other":
            ans = round(value / rate, 2)
            result.insert(END, f"{value} INR = {ans} {country}")
        else:  # Other to INR
            ans = round(value * rate, 2)
            result.insert(END, f"{value} {country} = {ans} INR")
    else:
        result.delete(1.0, END)
        result.insert(END, "❌ Please enter valid amount and select country.")

# Convert Button
button = Button(converter, text="Convert", fg="green", font=("calibri", 20), bg="powder blue", command=convert)
button.grid(row=5, column=1, pady=10)

mainloop()