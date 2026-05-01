from tkinter import Button, Label, Toplevel, Frame

class Table (Toplevel):
    def __init__(self, arr):
        super().__init__()
        self.title("Table")
        self.geometry("1440x850")
        self.element_array = arr
        self.iteration = self.StringVar()
        self.iteration.set("0")
        self.last_iteration = ""
        self.search_history = []

        self.table_frame = Frame(self)
        self.table_frame.place(x=0, y=0, relwidth=1, height=750)

        self.cells = []
        for i in range(40): self.table_frame.columnconfigure(i, weight=1)
        for j in range(25): self.table_frame.rowconfigure(j, weight=1)

        self.build_table()

        self.left_btn = Button(
        self, 
        text="<", 
        font =("Comfortaa", 30), 
        fg="#edc68d", 
        bg="#303938",
        activebackground="#edc68d",
        activeforeground="#303938",
        relief="flat",
        state="disabled"
        )
        
        self.left_btn.place(
            relx=0.4,
            rely=0.85, 
            anchor="center",
            relwidth=0.1, 
            relheight=0.1
            )
        
        self.right_btn = Button(
        self, 
        text=">", 
        font =("Comfortaa", 30), 
        fg="#edc68d", 
        bg="#303938",
        activebackground="#edc68d",
        activeforeground="#303938",
        relief="flat",
        state="disabled"
        )
        
        self.right_btn.place(
            relx=0.6,
            rely=0.85, 
            anchor="center",
            relwidth=0.1, 
            relheight=0.1
            )
        
        self.center_lable = Label(
            self,
            text="99",
            fg="#04c7ee",
            font =("Comfortaa", 20),
            textvariable = self.iteration
        )

        self.center_lable.place(
            relx=0.5, 
            rely=0.85,
            anchor="center",
            relwidth=0.1, 
            relheight=0.1
            )

    def build_table(self):
        for cell in self.cells:
            cell.destroy()
        self.cells.clear()
    
        for index, value in enumerate(self.element_array):
            table_row = index // 40
            table_column = index % 40
            
            lbl = Label(
                self, 
                text=value, 
                relief="flat", 
                font=("Comfortaa", 10),
                bg="#edc68d",
                fg="#000000",
            )
            lbl.grid(row=table_row, column=table_column, sticky="nsew", padx=1, pady=1)
            self.cells.append(lbl)

    def showing_search_path(self):
        pass



    def table_check(self, new_array, hist_arr):
        if self.element_array is new_array:
            return
        
        if len(self.element_array) != len(new_array):
            self.element_array = new_array
            self.build_table()
        else:
            self.element_array = new_array
            for i, value in enumerate(self.element_array):
                self.cells[i].config(text=value)

        if len(self.history_list) > 0:
            self.search_history = hist_arr
    