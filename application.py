import tkinter as tk
from tkinter import ttk
from typing import Container


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text="Welcome to the application")
        self.label.grid(row=0, column=1, columnspan=5, pady=10, padx=10)

        self.button1 = ttk.Button(self, text="Start",command=lambda: controller.show_frame(NewSwitch))
        self.button1.grid(row=1, column=1,pady=10, padx=10)

class NewSwitch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="New Switch")
        self.label.grid(row=0, column=0, columnspan=2)

        self.button1 = ttk.Button(self, text="Back",command=lambda: controller.show_frame(StartPage))
        self.button1.grid(row=0, column=2)

        self.id_label = ttk.Label(self, text="ID")
        self.id_label.grid(row=1, column=0)
        self.id_imput = ttk.Entry(self)
        self.id_imput.grid(row=1, column=1)

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

    def submitHandler(self):
        print("Submit")
        print(self.name_imput.get())
        self.name_imput.delete(0, 'end')


class Application(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, NewSwitch):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


    

app = Application()
app.mainloop()

