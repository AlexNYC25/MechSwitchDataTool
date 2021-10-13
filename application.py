import tkinter as tk
from tkinter import ttk
from typing import Container
from mongoLibrary import MechanicalClient

applicationMongoClient = MechanicalClient()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text="Welcome to the application")
        self.label.pack(pady=10, padx=10)

        self.button1 = ttk.Button(self, text="Start",command=lambda: controller.show_frame(NewSwitch))
        self.button1.pack()

## frame for adding a new switch to the database
class NewSwitch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="New Switch")
        self.label.grid(row=0, column=0, columnspan=2)

        self.button1 = ttk.Button(self, text="Back",command=lambda: controller.show_frame(StartPage))
        self.button1.grid(row=0, column=2)

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

        self.main_image = ttk.Label(self, text="Main Image")
        self.main_image.grid(row=12, column=0)
        self.main_image_imput = ttk.Entry(self)
        self.main_image_imput.grid(row=12, column=1)

        self.images = ttk.Label(self, text="Images")
        self.images.grid(row=13, column=0)
        self.images_imput = ttk.Entry(self)
        self.images_imput.grid(row=13, column=1)

        self.manufacturer_description_label = ttk.Label(self, text="Manufacturer Description")
        self.manufacturer_description_label.grid(row=14, column=0)
        self.manufacturer_description = tk.Entry(self)
        self.manufacturer_description.grid(row=14, column=1)

        self.submit_label = ttk.Label(self, text="Submit")
        self.submit_label.grid(row=15, column=0)
        self.submit = ttk.Button(self, text="Submit", command=self.submitHandler)
        self.submit.grid(row=15, column=0)

# need to format data for array values for the monogodb insertion
    def submitHandler(self):
        switch_data = {}

        ## need to format the data for the monogodb insertion
        if self.name_imput.get() != "":
            switch_data["name"] = self.name_imput.get()

        if self.manuf_imput.get() != "":
            switch_data["manufacturer"] = self.manuf_imput.get()

        if self.type.get() != "":
            switch_data["type"] = self.type.get()

        ## split the categories into an array
        if self.category.get() != "":
            switch_data["category"] = self.category.get()

        if self.avg_price.get() != "":
            switch_data["avgCost"] = self.avg_price.get()

        if self.actuation_force.get() != "":
            switch_data["actuationForce"] = self.actuation_force.get()
        
        if self.bottom_force.get() != "":
            switch_data["bottomForce"] = self.bottom_force.get()

        # split the categories into an array
        if self.spring_weights_imput.get() != "":
            switch_data["springWeight"] = self.spring_weights_imput.get().split(",")
        
        if self.actuation_distance.get() != "":
            switch_data["actuationDistance"] = self.actuation_distance.get()

        if self.travel_distance.get() != "":
            switch_data["travelDistance"] = self.travel_distance.get()
        
        if self.main_image_imput.get() != "":
            switch_data["mainImage"] = self.main_image_imput.get()
        
        # split the list of images into an array
        if self.images_imput.get() != "":
            switch_data["images"] = self.images_imput.get().split(",")

        if self.manufacturer_description.get() != "":
            switch_data["manufacturerDescription"] = self.manufacturer_description.get()

        
        ## print(switch_data)

        applicationMongoClient.insertSwitch(switch_data)

        ## reset the fields
        self.name_imput.delete(0, 'end')
        self.manuf_imput.delete(0, 'end')
        self.type.delete(0, 'end')
        self.category.delete(0, 'end')
        self.avg_price.delete(0, 'end')
        self.actuation_force.delete(0, 'end')
        self.bottom_force.delete(0, 'end')
        self.spring_weights_imput.delete(0, 'end')
        self.actuation_distance.delete(0, 'end')
        self.travel_distance.delete(0, 'end')
        self.main_image_imput.delete(0, 'end')
        self.images_imput.delete(0, 'end')
        self.manufacturer_description.delete(0, 'end')


# creates the application window loading the frames
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

