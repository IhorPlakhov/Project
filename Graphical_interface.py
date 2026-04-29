from tkinter import Tk, Button, Entry, Label
from tkinter.ttk import Combobox

class Window(Tk):

    def __init__(self, controler):
        super().__init__()

        self.controler = controler
        self.title("Search comparison")
        self.geometry("450x650")

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
            rely=0.65, 
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
            rely=0.75, 
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
            rely=0.75, 
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
            rely=0.65, 
            anchor="e",
            relwidth=0.25, 
            relheight=0.07
            )

    def get_size(self):
        return self.entry_size.get()
    
    def get_element(self):
        return self.entry_element.get()
        
    def clicked_on_search(self):
        pass
        #self.controler.filling_array_random_elements(self.get_size)
        #self.controler.search(var, self.)