from tkinter import Tk, Button, Entry, Label, messagebox, StringVar, Toplevel
from tkinter.ttk import Combobox
from Table import Table

class Window(Tk):

    def __init__(self, controler):
        super().__init__()

        self.controler = controler
        self.title("Search comparison")
        self.geometry("450x300")
        self.type_of_search = ["Sequential Search","Fibonacci Search","Interpolation Search","Hash Function Search"]
        self.enter_lenght = 5
        self.size_var = StringVar()
        self.element_var = StringVar()
        self.algorithm_var = StringVar()
        self.history_list = []

        self.size_var.trace_add("write", self.check_fields)
        self.element_var.trace_add("write", self.check_fields)
        self.algorithm_var.trace_add("write", self.check_fields)

        self.table_window = None

        self.btn_1 = Button(
            self, 
            text="START", 
            font =("Comfortaa", 20), 
            fg="#edc68d",
            bg="#303938",
            activebackground="#edc68d",
            activeforeground="#303938",
            relief="flat",
            command=self.clicked_on_search,
            state="disabled"
            )
        
        self.btn_1.place(
            relx=0.5,
            rely=0.9, 
            anchor="center",
            relwidth=0.25, 
            relheight=0.12
            )
        
        self.btn_2 = Button(
            self, 
            text="FILE", 
            font =("Comfortaa", 20), 
            fg="#edc68d", 
            bg="#303938",
            activebackground="#edc68d",
            activeforeground="#303938",
            relief="flat",
            command=self.clicked_on_search,
            state="disabled"
            )
        
        self.btn_2.place(
            relx=0.65, 
            rely=0.9, 
            anchor="w",
            relwidth=0.25, 
            relheight=0.12
            )
        
        self.btn_3 = Button(
            self, 
            text="TABLE", 
            font =("Comfortaa", 20), 
            fg="#edc68d", 
            bg="#303938",
            activebackground="#edc68d",
            activeforeground="#303938",
            relief="flat",
            command=self.creation_table,
            state="disabled"
            )
        
        self.btn_3.place(
            relx=0.35, 
            rely=0.9, 
            anchor="e",
            relwidth=0.25, 
            relheight=0.12
            )
        
        self.lable_1 = Label(
            self,
            text="Size of array",
            fg="#04c7ee",
            font =("Comfortaa", 20),
        )

        self.lable_1.place(
            relx=0.15, 
            rely=0.1, 
            anchor="w",
            relwidth=0.4, 
            relheight=0.1
            )
        
        self.lable_2 = Label(
            self,
            text="Target element",
            fg="#04c7ee",
            font =("Comfortaa", 20),
        )

        self.lable_2.place(
            relx=0.12, 
            rely=0.3, 
            anchor="w",
            relwidth=0.4, 
            relheight=0.1
            )
        
        self.entry_size = Entry(
            self,
            font =("Comfortaa", 20),
            validate = "key",
            validatecommand = (self.register(self.validate_char), '%P'),
            textvariable=self.size_var
        )

        self.entry_size.place(
            relx=0.8, 
            rely=0.1, 
            anchor="e",
            relwidth=0.25, 
            relheight=0.1
            )

        self.entry_element = Entry(
                self,
                font = ("Comfortaa", 20),
                validate = "key",
                validatecommand = (self.register(self.validate_char), '%P'),
                textvariable=self.element_var
            )

        self.entry_element.place(
            relx=0.8, 
            rely=0.3, 
            anchor="e",
            relwidth=0.25, 
            relheight=0.1
            )
        
        self.cd = Combobox(self,state="readonly")
        self.cd.configure(
            font =("Comfortaa", 20),
            values=self.type_of_search,
            textvariable=self.algorithm_var

            )
        self.cd.set("Choose algorithm")
        self.cd.bind("<<ComboboxSelected>>", self.check_fields)

        self.cd.place(
            relx=0.5, 
            rely=0.5, 
            anchor="center",
            relwidth=0.67, 
            relheight=0.12
        )

        self.lable_3 = Label(
            self,
            text="Practical difficulty:",
            fg="#04c7ee",
            font =("Comfortaa", 20),
        )

        self.lable_3.place(
            relx=0.42, 
            rely=0.73,
            anchor="center",
            relwidth=0.75, 
            relheight=0.1
            )
        
        self.lable_4 = Label(
            self,
            text="",
            fg="#04c7ee",
            font =("Comfortaa", 20),
            anchor="w"
        )

        self.lable_4.place(
            relx=0.84, 
            rely=0.73,
            anchor="center",
            relwidth=0.35, 
            relheight=0.12
            )
        
        self.lable_5 = Label(
            self,
            font =("Comfortaa", 18),
            anchor="s"
        )

        self.lable_5.place(
            relx=0.5, 
            rely=0.625,
            anchor="center",
            relwidth=0.5, 
            relheight=0.1
            )

    def clicked_on_search(self):
        array_size = self.entry_size.get()
        array_size = int(array_size)
        if array_size <= 1000 and array_size >= 100:
            element = self.entry_element.get()
            choice = self.cd.get()
            self.controler.filling_array_random_elements(array_size)
            is_found, self.history_list, counter = self.controler.searching(choice, element)
            if is_found:
                self.lable_5.config(text="Element is found",fg="#51ea3d")
                self.lable_4.config(text=counter)
            else:
                self.lable_5.config(text="Element is not found",fg="#f1392b")
                self.history_list = []
        else:
            messagebox.showerror("Error",f"Size of your array: {array_size}, but must be in range (100, 1000)")
    
    def creation_table(self):
        if (self.controler.array == None):
            array_size = int(self.entry_size.get())
            if array_size <= 1000 and array_size >= 100:
                self.controler.filling_array_random_elements(array_size)
            else:
                messagebox.showerror("Error",f"Size of your array: {array_size}, but must be in range (100, 1000)")
                return

        if self.table_window is None or not self.table_window.winfo_exists():
            self.table_window = Table(self.controler.array)
        else:
            self.table_window.table_check(self.controler.array, self.history_list)



    def check_fields(self, *args):
        size = self.size_var.get()
        element = self.element_var.get()
        choice = self.algorithm_var.get()

        if size != "":
            self.btn_3.config(state="normal")
            if element != "" and choice != "Choose algorithm":
                self.btn_1.config(state="normal")
                if self.lable_4.cget("text") != "":
                    self.btn_2.config(state="normal")
                else:
                    self.btn_2.config(state="disabled")
            else:
                self.btn_1.config(state="disabled")
        else:
            self.btn_3.config(state="disabled")
    

    def validate_char(self, text):
        return text == "" or text.isdigit() and len(text) <= self.enter_lenght
