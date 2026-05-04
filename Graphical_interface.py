from tkinter import Tk, Button, Entry, Label, messagebox, StringVar
from tkinter.ttk import Combobox
from Table import Table
from File import *

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
            command=self.save_result,
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
        
        self.delete_btn = Button(
            self, 
            text="X", 
            font =("Comfortaa", 20), 
            fg="#edc68d", 
            bg="#303938",
            activebackground="#edc68d",
            activeforeground="#303938",
            relief="flat",
            command=self.clean_interface,
            state="disabled"
            )
        
        self.delete_btn.place(
            relx=0.85, 
            rely=0.2, 
            anchor="e",
            relwidth=0.08, 
            relheight=0.25
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
            relx=0.74, 
            rely=0.1, 
            anchor="e",
            relwidth=0.2, 
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
            relx=0.74, 
            rely=0.3, 
            anchor="e",
            relwidth=0.2, 
            relheight=0.1
            )
        
        self.cd = Combobox(self,state="readonly")
        self.cd.configure(
            font =("Comfortaa", 20),
            values=self.type_of_search,
            textvariable=self.algorithm_var

            )

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
        
        self.size_var.trace_add("write", self.reset_search_state)
        self.element_var.trace_add("write", self.reset_search_state)
        self.algorithm_var.trace_add("write", self.reset_search_state)

        self.entry_size.bind("<FocusOut>", self.on_size_focus_out)
        self.entry_size.bind("<Return>", self.on_size_focus_out)

        self.cd.set("Choose algorithm")
        self.cd.bind("<<ComboboxSelected>>", self.changing_algoritm)
    
    def changing_algoritm(self, event=None):
        choice = self.algorithm_var.get()

        if choice == "Fibonacci Search" or choice == "Interpolation Search":
            if not self.controler.is_sorted:
                self.controler.sort_array()

        elif choice == "Sequential Search":
            if self.controler.is_sorted:
                create_new = messagebox.askokcancel(
                    "Confirmation",
                    "Array is sorted so search results for sequential search may not be accurate!\n"
                    "Do you want generate a new unsorted array?\n"
                    "Yes - Create new unsorted array\n"
                    "No - Continue using this sorted array"
                )
                self.controler.filling_array_random_elements(len(self.controler.array))
                if create_new:
                    self.controler.filling_array_random_elements(len(self.controler.array))

        if len(self.history_list) == 0:
            if self.table_window is not None and self.table_window.winfo_exists():
                self.table_window.table_check(self.controler.array, self.history_list, choice)
                
        self.check_fields()

    def reset_search_state(self, *args):
        current_text = self.lable_4.cget("text")
        
        if current_text != "":
            self.lable_4.config(text="")
            self.lable_5.config(text="")
            self.history_list = []
            
            if self.table_window is not None and self.table_window.winfo_exists():
                choice = self.algorithm_var.get()
                self.table_window.table_check(self.controler.array, self.history_list, choice)
                
        self.check_fields()

    def clean_interface(self):
        self.size_var.set("")
        self.element_var.set("")
        
        self.cd.set("Choose algorithm")

        self.lable_4.config(text="")
        self.lable_5.config(text="")

        self.controler.reset_data()
        self.history_list = []
        
        if self.table_window is not None and self.table_window.winfo_exists():
            self.table_window.destroy()

        self.check_fields()  

    def on_size_focus_out(self, event):
        if not self.entry_size.get().isdigit():
            return
        
        if self.table_window is not None and self.table_window.winfo_exists():
            self.creation_table()
        
    def closing_window(self):
        self.table_window.destroy()
        self.check_fields()

    def clicked_on_search(self):
        if self.controler.array is None:
            messagebox.showwarning("Attention","First create a table, to do this click on TABLE")
            return
        
        array_size = int(self.entry_size.get())

        if len(self.controler.array) != array_size:
            messagebox.showwarning("Attention", "You changed the size of the array, click 'TABLE' to generate new data.")
            return
        
        element = int(self.entry_element.get())
        choice = self.cd.get()
        
        is_found, self.history_list, counter = self.controler.searching(choice, element)

        if is_found:
            self.lable_5.config(text="Element is found",fg="#51ea3d")
            self.lable_4.config(text=counter)
        else:
            self.lable_5.config(text="Element is not found",fg="#f1392b")
            self.lable_4.config(text="")
            self.history_list = []

        if self.table_window is not None and self.table_window.winfo_exists():
            self.table_window.table_check(self.controler.array, self.history_list, choice)

        self.btn_2.config(state="normal")
        self.check_fields()
    
    def creation_table(self):
        if not self.entry_size.get().isdigit():
            return
        
        array_size = int(self.entry_size.get())

        if self.controler.array is None or len(self.controler.array) != array_size:
            if array_size <= 1000 and array_size >= 100:
                if self.controler.array is None or len(self.controler.array) != array_size:
                    self.controler.filling_array_random_elements(array_size)
            else:
                messagebox.showerror("Error",f"Size of your array: {array_size}, but must be in range (100, 1000)")
                self.size_var.set("")
                return

        choice = self.cd.get()
        if choice == "Fibonacci Search" or choice == "Interpolation Search":
            self.controler.sort_array()

        if self.table_window is None or not self.table_window.winfo_exists():
            self.table_window = Table(self.controler.array, choice)
            self.table_window.protocol("WM_DELETE_WINDOW", self.closing_window)
            self.table_window.table_check(self.controler.array, self.history_list, choice)
        else:
            self.table_window.table_check(self.controler.array, self.history_list, choice)
        self.check_fields()

    def check_fields(self, *args):
        size = self.size_var.get()
        element = self.element_var.get()
        choice = self.algorithm_var.get()

        if hasattr(self, 'lable_4'):
            current_text = self.lable_4.cget("text")

        if size != "" or element != "" or choice != "Choose algorithm":
            self.delete_btn.config(state="normal")
        else:
            self.delete_btn.config(state="disabled")

        if size != "":
            if element != "" and choice != "Choose algorithm":
                self.btn_1.config(state="normal")
            else:
                self.btn_1.config(state="disabled")

            if self.table_window is None or not self.table_window.winfo_exists():
                self.btn_3.config(state="normal")
            else:
                self.btn_3.config(state="disabled")
        else:
            self.btn_1.config(state="disabled")
            self.btn_3.config(state="disabled")
            self.btn_2.config(state="disabled")

        if hasattr(self, 'lable_4'):
            current_text = self.lable_4.cget("text")
            if not current_text or current_text == "":
                 self.btn_2.config(state="disabled")
            else:
                 self.btn_2.config(state="normal")
        else:
            self.btn_2.config(state="disabled")
    
    def validate_char(self, text):
        return text == "" or text.isdigit() and len(text) <= self.enter_lenght
    
    def save_result(self):
        user_solution = messagebox.askokcancel(
            "Confirmation",
            "Do you want to save the search results to a file?"
        )

        if user_solution:
            file = File()
            file.write_file(40, self.controler.array, self.entry_element.get())
