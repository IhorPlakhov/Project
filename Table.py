from tkinter import Button, Label, Toplevel, Frame, StringVar

class Table (Toplevel):
    def __init__(self, arr, algo=""):
        super().__init__()
        self.title("Table")
        self.geometry("1600x850")
        self.element_array = arr
        self.iteration = 0
        self.last_iteration = ""
        self.search_history = []

        self.table_frame = Frame(self, bg="#000000",)
        self.table_frame.place(x=0, y=0, relwidth=1, relheight=0.705)

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
            state="disabled",
            command = lambda: self.showing_search_path(False)
        )
        
        self.left_btn.place(
            relx=0.35,
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
            state="disabled",
            command = lambda: self.showing_search_path(True)
        )
        
        self.right_btn.place(
            relx=0.65,
            rely=0.85, 
            anchor="center",
            relwidth=0.1, 
            relheight=0.1
            )

        self.center_label = Label(
            self,
            text="0 / 0",
            fg="#04c7ee",
            font=("Comfortaa", 30),
        )

        self.center_label.place(
            relx=0.5, 
            rely=0.85, 
            anchor="center"
            )
        
        self.info_label = Label(
            self,
            text=f'Search using algorithm "{algo}" on an array of size {len(self.element_array)}',
            fg="#04c7ee",
            font=("Comfortaa", 25),
        )

        self.info_label.place(
            relx=0.5, 
            rely=0.75, 
            anchor="center"
            )

    def build_table(self):
        for cell in self.cells:
            cell.destroy()
        self.cells.clear()
    
        for index, value in enumerate(self.element_array):
            table_row = index // 40
            table_column = index % 40
            
            lbl = Label(
                self.table_frame, 
                text=value, 
                relief="flat", 
                font=("Comfortaa", 10),
                bg="#edc68d",
                fg="#000000",
            )
            lbl.grid(row=table_row, column=table_column, sticky="nsew", padx=1, pady=1)
            self.cells.append(lbl)

    def showing_search_path(self, step_change):
        if step_change:
            new_idx = self.search_history[self.iteration]
            self.iteration+=1
            color = "#deda03"
            if self.iteration == len(self.search_history):
                color = "#15970c"
            self.cells[new_idx].config(bg=color)
        else:
            self.iteration-=1
            new_idx = self.search_history[self.iteration]
            self.cells[new_idx].config(bg="#edc68d")

        self.update_button_status()
        self.center_label.config(text=f"{self.iteration} / {len(self.search_history)}")
        
    def update_button_status(self):
        if not self.search_history:
            self.left_btn.config(state="disabled")
            self.right_btn.config(state="disabled")
        else:
            if self.iteration == 0:
                self.left_btn.config(state="disabled")
            else:
                self.left_btn.config(state="normal")
            
            if self.iteration == len(self.search_history):
                self.right_btn.config(state="disabled")
            else:
                self.right_btn.config(state="normal")

    def table_check(self, new_array, hist_arr, algo):

        if algo:
            self.info_label.config(text=f'Search using algorithm "{algo}" on an array of size {len(new_array)}')

        if self.element_array is new_array:
            for idx in self.search_history:
                self.cells[idx].config(bg="#edc68d")
        
        elif len(self.element_array) != len(new_array):
            self.element_array = new_array
            self.build_table()
        else:
            self.element_array = new_array
            for i, value in enumerate(self.element_array):
                self.cells[i].config(text=value)
                self.cells[i].config(bg="#edc68d")

        self.search_history = hist_arr
        self.iteration = 0
        self.center_label.config(text=f"0 / {len(self.search_history)}")
        self.update_button_status()
    