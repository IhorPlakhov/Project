from tkinter import Tk, Button, Entry, Label
from tkinter.ttk import Combobox

class Window(Tk):

    def __init__(self, controler):
        super().__init__()

        self.controler = controler
        self.title("Search comparison")
        self.geometry("450x650")
        self.type_of_search = ["SequentialSearch","FibonacciSearch","InterpolationSearch","HashFunctionSearch"]

        self.btn = Button(
            self, 
            text="START", 
            font =("Comfortaa", 20), 
            fg="#edc68d", 
            bg="#303938",
            activebackground="#edc68d",
            activeforeground="#303938",
            relief="flat",
            command=self.clicked_on_search()
            )
        
        self.btn.place(
            relx=0.5, 
            rely=0.9, 
            anchor="center",
            relwidth=0.25, 
            relheight=0.07
            )
        
        self.lable_1 = Label(
            self,
            text="Size of array",
            fg="#04c7ee",
            font =("Comfortaa", 20),
        )

        self.lable_1.place(
            relx=0.15, 
            rely=0.55, 
            anchor="w",
            relwidth=0.4, 
            relheight=0.07
            )
        
        self.lable_2 = Label(
            self,
            text="Target element",
            fg="#04c7ee",
            font =("Comfortaa", 20),
        )

        self.lable_2.place(
            relx=0.12, 
            rely=0.65, 
            anchor="w",
            relwidth=0.4, 
            relheight=0.07
            )
        
        self.entry_size = Entry(
            self,
            font =("Comfortaa", 20)
        )

        self.entry_size.place(
            relx=0.8, 
            rely=0.65, 
            anchor="e",
            relwidth=0.25, 
            relheight=0.07
            )

        self.entry_element = Entry(
                self,
                font =("Comfortaa", 20)
            )

        self.entry_element.place(
            relx=0.8, 
            rely=0.55, 
            anchor="e",
            relwidth=0.25, 
            relheight=0.08
            )
        
        self.cd = Combobox(self,state="readonly")
        self.cd.configure(
            font =("Comfortaa", 20),
            values=self.type_of_search,
        

            )
        self.cd.set("Choose an algorithm")
        selected_algorithm = self.cd.get()
        self.cd.bind("<<ComboboxSelected>>", self.on_algorithm_select)
        self.current_choice = None

    def clicked_on_search(self):
        pass
        #self.controler.filling_array_random_elements(self.entry_size.get())
        #self.controler.search(self.cd.get(), self.entry_element.get())