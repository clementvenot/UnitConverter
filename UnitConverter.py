from TemperatureConverterFunction import Temperature
from tkinter import *

fenetre = Tk()
fenetre.title("tutorial")
fenetre.minsize(width=500, height=300)


# ------------------ DATA ------------------



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

formulaire = Canvas(fenetre)
formulaire.pack()

fenetre.mainloop()