import tkinter as tk
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """
        self.hi_there = ttk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = ttk.Button(self, text="QUIT")
        self.quit.pack(side="bottom")
        """

        """
        self.id_label = ttk.Label(self, text="ID")
        self.id_label.grid(row=1, column=0)
        self.id_imput = ttk.Entry(self)
        self.id_imput.grid(row=1, column=1)
        """

        self.name_label = ttk.Label(self, text="Name")
        self.name_label.grid(row=2, column=0)
        self.name_imput = ttk.Entry(self)
        self.name_imput.grid(row=2, column=1)

        self.manuf_label = ttk.Label(self, text="Manufacturer")
        self.manuf_label.grid(row=3, column=0)
        self.manuf_imput = ttk.Entry(self)
        self.manuf_imput.grid(row=3, column=1)

        self.type_label = ttk.Label(self, text="Type")
        self.type_label.grid(row=4, column=0)
        self.type = ttk.Combobox(self, values=["Linear", "Tactile", "Clicky"])
        self.type.grid(row=4, column=1)

        self.category_label = ttk.Label(self, text="Categories")
        self.category_label.grid(row=5, column=0)
        self.category = ttk.Entry(self)
        self.category.grid(row=5, column=1)

        self.avg_price_label = ttk.Label(self, text="Average Price")
        self.avg_price_label.grid(row=6, column=0)
        self.avg_price = ttk.Entry(self)
        self.avg_price.grid(row=6, column=1)

        self.actuation_force_label = ttk.Label(self, text="Actuation Force")
        self.actuation_force_label.grid(row=7, column=0)
        self.actuation_force = ttk.Entry(self)
        self.actuation_force.grid(row=7, column=1)

        self.bottom_force_label = ttk.Label(self, text="Bottom Force")
        self.bottom_force_label.grid(row=8, column=0)
        self.bottom_force = ttk.Entry(self)
        self.bottom_force.grid(row=8, column=1)

        self.spring_weights = ttk.Label(self, text="Spring Weights")
        self.spring_weights.grid(row=9, column=0)
        self.spring_weights_imput = ttk.Entry(self)
        self.spring_weights_imput.grid(row=9, column=1)

        self.actuation_distance_label = ttk.Label(self, text="Actuation Distance")
        self.actuation_distance_label.grid(row=10, column=0)
        self.actuation_distance = ttk.Entry(self)
        self.actuation_distance.grid(row=10, column=1)

        self.travel_distance_label = ttk.Label(self, text="Travel Distance")
        self.travel_distance_label.grid(row=11, column=0)
        self.travel_distance = ttk.Entry(self)
        self.travel_distance.grid(row=11, column=1)

        self.mainImage = ttk.Label(self, text="Main Image")
        self.mainImage.grid(row=12, column=0)
        self.mainImage_imput = ttk.Entry(self)
        self.mainImage_imput.grid(row=12, column=1)

        self.images = ttk.Label(self, text="Images")
        self.images.grid(row=13, column=0)
        self.images_imput = ttk.Entry(self)
        self.images_imput.grid(row=13, column=1)

        self.manufacturer_distance_label = ttk.Label(self, text="Manufacturer Distance")
        self.manufacturer_distance_label.grid(row=14, column=0)
        self.manufacturer_distance = ttk.Entry(self)
        self.manufacturer_distance.grid(row=14, column=1)

        self.submit_label = ttk.Label(self, text="Submit")
        self.submit_label.grid(row=15, column=0)
        self.submit = ttk.Button(self, text="Submit", command=self.submitHandler)
        self.submit.grid(row=15, column=0)


    def say_hi(self):
        print("hi there, everyone!")

    def submitHandler(self):
        print("Submit")
        print(self.name_imput.get())



root = tk.Tk()
app = Application(master=root)
app.mainloop()
