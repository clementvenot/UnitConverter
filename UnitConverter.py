from TemperatureConverterFunction import Temperature
from CurrencyConverterFunction import Currency
from WeightConverterFunction import Weight
from DistanceConverterFunction import Distance
from tkinter import *

fenetre = Tk()
fenetre.title("tutorial")
fenetre.minsize(width=500, height=300)


# ------------------ DATA ------------------
units = {
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Currency": list(Currency.rates.keys()),
    "Distance": list(Distance().tab.keys()),
    "Weight": list(Weight().tab.keys()),
}


# ------------------ FUNCTIONS ------------------
def update_units(*args):
    selected_category = category_var.get()
    unit_list = units.get(selected_category, [])

    # Update FROM menu
    from_menu["menu"].delete(0, "end")
    for unit in unit_list:
        from_menu["menu"].add_command(
            label=unit,
            command=lambda value=unit: from_unit.set(value)
        )

    # Update TO menu
    to_menu["menu"].delete(0, "end")
    for unit in unit_list:
        to_menu["menu"].add_command(
            label=unit,
            command=lambda value=unit: to_unit.set(value)
        )

    if unit_list:
        from_unit.set(unit_list[0])
        to_unit.set(unit_list[1])

def convert():
    try:
        value = float(input_entry.get())
        category = category_var.get()

        from_u = from_unit.get().lower()
        to_u = to_unit.get().lower()

        if category == "Temperature":
            temp = Temperature(value, from_u)
            result = temp.convert_to(to_u)
        
        elif category == "Currency":
            curr = Currency(value, from_u)
            result = curr.convert_to(to_u)
        
        elif category == "Distance":
            dist = Distance()
            result = dist.convert(from_u, value, to_u)
        
        else:
            result = "Not implemented"

        output_var.set(str(result))

    except Exception:
        output_var.set("Error")

def swap_units():
    #échanger les unités
    from_u = from_unit.get()
    to_u = to_unit.get()

    from_unit.set(to_u)
    to_unit.set(from_u)

    #échanger les valeurs
    input_val = input_entry.get()
    output_val = output_var.get()

    input_entry.delete(0, END)
    input_entry.insert(0, output_val)

    output_var.set(input_val)

# ------------------ TOP (CATEGORY) ------------------
top_frame = Frame(fenetre)
top_frame.pack(pady=10)

label_category = Label(top_frame, text="Category", font=("Arial", 12))
label_category.pack(side=LEFT, padx=5)

category_var = StringVar()
category_var.set("Temperature")

categories = ["Temperature", "Distance", "Weight", "Currency"]

dropdown = OptionMenu(top_frame, category_var, *categories)
dropdown.pack(side=LEFT, padx=5)
category_var.trace("w", update_units)

# ------------------ MAIN (CENTERED) ------------------
main_frame = Frame(fenetre)
main_frame.pack(expand=True)

# 3 colonnes maintenant (gauche / bouton / droite)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=0)
main_frame.columnconfigure(2, weight=1)

# ------------------ INPUT ------------------
input_frame = Frame(main_frame)
input_frame.grid(row=0, column=0, padx=10)

input_entry = Entry(input_frame, width=20)
input_entry.pack()

from_unit = StringVar()
from_menu = OptionMenu(input_frame, from_unit, "")
from_menu.pack(pady=5)

# ------------------ SWAP BUTTON (CENTER) ------------------
swap_button = Button(main_frame, text="⇄", command=swap_units)
swap_button.grid(row=0, column=1, padx=10)

# ------------------ OUTPUT ------------------
output_frame = Frame(main_frame)
output_frame.grid(row=0, column=2, padx=10)

output_var = StringVar()

output_entry = Entry(output_frame, textvariable=output_var, width=20, state="readonly")
output_entry.pack()

to_unit = StringVar()
to_menu = OptionMenu(output_frame, to_unit, "")
to_menu.pack(pady=5)

# ------------------ BUTTON ------------------

convert_button = Button(fenetre, text="Convert", command=convert)
convert_button.pack(pady=10)


update_units()

fenetre.mainloop()