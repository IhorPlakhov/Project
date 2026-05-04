from tkinter import Tk, Button, Entry, Label, messagebox, StringVar
from tkinter.ttk import Combobox
from Table import Table
from File import *

class Window(Tk):

    def __init__(self, controller):
        super().__init__()

        self.controler = controller
        self.title("Search comparison")
        self.geometry("450x300")
        self.type_of_search = ["Sequential Search","Fibonacci Search","Interpolation Search","Hash Function Search"]
        self.enter_lenght = 5
        self.size_var = StringVar()
        self.element_var = StringVar()
        self.algorithm_var = StringVar()
        self.history_list = []
        self.handling_focus_out = False

        self.table_window = None

        self.btn_start_search = Button(
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
        
        self.btn_start_search.place(
            relx=0.5,
            rely=0.9, 
            anchor="center",
            relwidth=0.25, 
            relheight=0.12
            )
        
        self.btn_save_file = Button(
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
        
        self.btn_save_file.place(
            relx=0.65, 
            rely=0.9, 
            anchor="w",
            relwidth=0.25, 
            relheight=0.12
            )
        
        self.btn_show_table = Button(
            self, 
            text="TABLE", 
            font =("Comfortaa", 20), 
            fg="#edc68d", 
            bg="#303938",
            activebackground="#edc68d",
            activeforeground="#303938",
            relief="flat",
            command=self.create_table_view,
            state="disabled"
            )
        
        self.btn_show_table.place(
            relx=0.35, 
            rely=0.9, 
            anchor="e",
            relwidth=0.25, 
            relheight=0.12
            )
        
        self.btn_clear = Button(
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
        
        self.btn_clear.place(
            relx=0.85, 
            rely=0.2, 
            anchor="e",
            relwidth=0.08, 
            relheight=0.25
            )
        
        self.label_size = Label(
            self,
            text="Size of array",
            fg="#04c7ee",
            font =("Comfortaa", 20),
        )

        self.label_size.place(
            relx=0.15, 
            rely=0.1, 
            anchor="w",
            relwidth=0.4, 
            relheight=0.1
            )
        
        self.label_element = Label(
            self,
            text="Target element",
            fg="#04c7ee",
            font =("Comfortaa", 20),
        )

        self.label_element.place(
            relx=0.12, 
            rely=0.3, 
            anchor="w",
            relwidth=0.4, 
            relheight=0.1
            )
        
        self.label_difficulty = Label(
            self,
            text="Practical difficulty:",
            fg="#04c7ee",
            font =("Comfortaa", 20),
        )

        self.label_difficulty.place(
            relx=0.42, 
            rely=0.73,
            anchor="center",
            relwidth=0.75, 
            relheight=0.1
            )
        
        
        self.label_difficulty_value = Label(
            self,
            text="",
            fg="#04c7ee",
            font =("Comfortaa", 20),
            anchor="w"
        )

        self.label_difficulty_value.place(
            relx=0.84, 
            rely=0.73,
            anchor="center",
            relwidth=0.35, 
            relheight=0.12
            )
        
        self.label_status = Label(
            self,
            font =("Comfortaa", 18),
            anchor="s"
        )

        self.label_status.place(
            relx=0.5, 
            rely=0.625,
            anchor="center",
            relwidth=0.5, 
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
        
        self.combo_algorithms = Combobox(self,state="readonly")
        self.combo_algorithms.configure(
            font =("Comfortaa", 20),
            values=self.type_of_search,
            textvariable=self.algorithm_var
            )

        self.combo_algorithms.set("Choose algorithm")

        self.combo_algorithms.place(
            relx=0.5, 
            rely=0.5, 
            anchor="center",
            relwidth=0.67, 
            relheight=0.12
        )
        
        self.size_var.trace_add("write", self.reset_search_state)
        self.element_var.trace_add("write", self.reset_search_state)
        self.algorithm_var.trace_add("write", self.reset_search_state)

        self.entry_size.bind("<FocusOut>", self.on_size_focus_out)
        self.entry_size.bind("<Return>", self.on_size_focus_out)

        self.combo_algorithms.bind("<<ComboboxSelected>>", self.changing_algorithm)
    
    def changing_algorithm(self, event=None):
        choice = self.algorithm_var.get()
        array_changed = False

        if choice == "Fibonacci Search" or choice == "Interpolation Search":
            if self.controler.array is not None and not self.controler.is_sorted:
                self.controler.sort_array()
                array_changed = True

        elif choice == "Sequential Search":
            if self.controler.is_sorted:
                create_new = messagebox.askokcancel(
                    "Confirmation",
                    "Array is sorted so search results for sequential search may not be accurate!\n"
                    "Do you want generate a new unsorted array?\n"
                    "OK - Create new unsorted array\n"
                    "Cancel - Continue using this sorted array"
                )
                if create_new:
                    self.controler.filling_array_random_elements(len(self.controler.array))
                    self.history_list.clear()
                    array_changed = True

        if (array_changed or not self.history_list) and self.table_window is not None and self.table_window.winfo_exists():
            self.table_window.update_table_status(self.controler.array, self.history_list, choice)
            
        self.check_fields()

    def reset_search_state(self, *args):
        current_text = self.label_difficulty_value.cget("text")
        
        if current_text != "":
            self.label_difficulty_value.config(text="")
            self.label_status.config(text="")
            self.history_list.clear()
            
            if self.table_window is not None and self.table_window.winfo_exists():
                choice = self.algorithm_var.get()
                self.table_window.update_table_status(self.controler.array, self.history_list, choice)
                
        self.check_fields()

    def clean_interface(self):
        self.size_var.set("")
        self.element_var.set("")
        self.combo_algorithms.set("Choose algorithm")

        self.label_difficulty_value.config(text="")
        self.label_status.config(text="")

        self.controler.reset_data()
        self.history_list.clear()
        
        if self.table_window is not None and self.table_window.winfo_exists():
            self.table_window.destroy()

        self.check_fields()  

    def on_size_focus_out(self, event):
        if self.handling_focus_out:
            return
        if not self.entry_size.get().isdigit():
            return
        
        if self.table_window is not None and self.table_window.winfo_exists():
            self.handling_focus_out = True
            self.create_table_view()
            self.handling_focus_out = False
        
    def table_close(self):
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
        choice = self.combo_algorithms.get()
        
        is_found, self.history_list, counter = self.controler.searching(choice, element)

        if is_found:
            self.label_status.config(text="Element is found",fg="#51ea3d")
            self.label_difficulty_value.config(text = str(counter))
        else:
            self.label_status.config(text="Element is not found",fg="#f1392b")
            self.label_difficulty_value.config(text="")
            self.history_list.clear()

        if self.table_window is not None and self.table_window.winfo_exists():
            self.table_window.update_table_status(self.controler.array, self.history_list, choice)

        self.btn_save_file.config(state="normal")
        self.check_fields()
    
    def create_table_view(self):
        if not self.entry_size.get().isdigit():
            return
        
        array_size = int(self.entry_size.get())

        if self.controler.array is None or len(self.controler.array) != array_size:
            if array_size <= 1000 and array_size >= 100:
                self.controler.filling_array_random_elements(array_size)
            else:
                messagebox.showerror("Error",f"Size of your array: {array_size}, but must be in range (100, 1000)")
                self.size_var.set("")
                return

        choice = self.combo_algorithms.get()
        if choice == "Fibonacci Search" or choice == "Interpolation Search":
            self.controler.sort_array()

        if self.table_window is None or not self.table_window.winfo_exists():
            self.table_window = Table(self.controler.array, choice)
            self.table_window.protocol("WM_DELETE_WINDOW", self.table_close)
        
        self.table_window.update_table_status(self.controler.array, self.history_list, choice)
        self.check_fields()

    def check_fields(self, *args):
        size_entered = bool(self.size_var.get())
        element_entered = bool(self.element_var.get())
        algorithm_chosen = self.algorithm_var.get() != "Choose algorithm"

        has_results = False
        if hasattr(self, 'label_difficulty_value'):
            current_text = self.label_difficulty_value.cget("text")
            has_results = bool(current_text)

        table_exists = self.table_window is not None and self.table_window.winfo_exists()

        can_clear = size_entered or element_entered or algorithm_chosen
        can_start_search = size_entered and element_entered and algorithm_chosen
        can_show_table = size_entered and not table_exists
        can_save_file = size_entered and has_results

        self.btn_clear.config(state="normal" if can_clear else "disabled")
        self.btn_start_search.config(state="normal" if can_start_search else "disabled")
        self.btn_show_table.config(state="normal" if can_show_table else "disabled")
        self.btn_save_file.config(state="normal" if can_save_file else "disabled")
    
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
