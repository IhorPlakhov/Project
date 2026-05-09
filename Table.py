from tkinter import Button, Label, Toplevel, Frame
from Constans import UIConfig

class Table (Toplevel):
    def __init__(self, arr, algo=""):
        super().__init__()
        self.title("Table")
        self.state('zoomed')
        self.geometry(UIConfig.TABLE_SIZE)
        self.element_array = arr
        self.iteration = 0
        self.search_history = []

        self.table_frame = Frame(self, bg=UIConfig.TABLE_BACKGROUND,)
        self.table_frame.place(x=0, y=0, relwidth=1, relheight=0.705)

        self.cells = []
        for i in range(UIConfig.TABLE_COLUMNS):
            self.table_frame.columnconfigure(i, weight=1)
        for j in range(UIConfig.TABLE_ROWS):
            self.table_frame.rowconfigure(j, weight=1)

        self.build_table()

        self.btn_prev_step = Button(
            self,
            text="<", 
            font =UIConfig.TABLE_COUNTER, 
            fg=UIConfig.BUTTONS_TEXT, 
            bg=UIConfig.BUTTONS_BACKGROUND,
            activebackground=UIConfig.BUTTONS_TEXT,
            activeforeground=UIConfig.BUTTONS_BACKGROUND,
            relief="flat",
            state="disabled",
            command = lambda: self.showing_search_path(False)
        )
        
        self.btn_prev_step.place(
            relx=0.35,
            rely=0.85, 
            anchor="center",
            relwidth=0.1, 
            relheight=0.1
            )
        
        self.btn_next_step = Button(
            self, 
            text=">", 
            font =UIConfig.TABLE_COUNTER, 
            fg=UIConfig.BUTTONS_TEXT, 
            bg=UIConfig.BUTTONS_BACKGROUND,
            activebackground=UIConfig.BUTTONS_TEXT,
            activeforeground=UIConfig.BUTTONS_BACKGROUND,
            relief="flat",
            state="disabled",
            command = lambda: self.showing_search_path(True)
        )
        
        self.btn_next_step.place(
            relx=0.65,
            rely=0.85, 
            anchor="center",
            relwidth=0.1, 
            relheight=0.1
            )

        self.center_label = Label(
            self,
            text="0 / 0",
            fg=UIConfig.TEXT_COLOR,
            font=UIConfig.TABLE_COUNTER,
        )

        self.center_label.place(
            relx=0.5, 
            rely=0.85, 
            anchor="center"
            )
        
        self.info_label = Label(
            self,
            text=f'Search using algorithm "{algo}" on an array of size {len(self.element_array)}',
            fg=UIConfig.TEXT_COLOR,
            font=UIConfig.TABLE_INFO,
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
            table_row = index // UIConfig.TABLE_COLUMNS
            table_column = index % UIConfig.TABLE_COLUMNS
            
            lbl = Label(
                self.table_frame, 
                text=value, 
                relief="flat", 
                font=UIConfig.TABLE_CELL,
                bg=UIConfig.CELL_DEFAULT,
                fg=UIConfig.CELL_TEXT,
            )
            lbl.grid(row=table_row, column=table_column, sticky="nsew", padx=1, pady=1)
            self.cells.append(lbl)

    def showing_search_path(self, is_next):
        if is_next:
            new_idx = self.search_history[self.iteration]
            self.iteration+=1
            color = UIConfig.CELL_VISITED
            if self.iteration == len(self.search_history):
                color = UIConfig.CELL_FOUND
            self.cells[new_idx].config(bg=color)
        else:
            self.iteration-=1
            new_idx = self.search_history[self.iteration]
            self.cells[new_idx].config(bg=UIConfig.CELL_DEFAULT)

        self.update_button_status()
        self.center_label.config(text=f"{self.iteration} / {len(self.search_history)}")

    def reset_highlights(self):
        for idx in self.search_history:
            self.cells[idx].config(bg=UIConfig.CELL_DEFAULT)
        self.search_history = []
        self.iteration = 0
        self.center_label.config(text="0 / 0")
        self.update_button_status()
        
    def update_button_status(self):
        has_history = bool(self.search_history)
        
        self.btn_prev_step.config(state="normal" if has_history and self.iteration > 0 else "disabled")
        self.btn_next_step.config(state="normal" if has_history and self.iteration < len(self.search_history) else "disabled")

    def update_table_status(self, new_array, hist_arr, algo):

        if algo == UIConfig.COMBO_PLACEHOLDER:
            self.info_label.config(text=f"You haven't chosen the algorithm. Array size: {len(new_array)}")
        else:
            self.info_label.config(text=f'Search using algorithm "{algo}" on array of size {len(new_array)}')

        if self.element_array is new_array:
            for idx in self.search_history:
                self.cells[idx].config(bg=UIConfig.CELL_DEFAULT)
        
        elif len(self.element_array) != len(new_array):
            self.element_array = new_array
            self.build_table()
        else:
            self.element_array = new_array
            for i, value in enumerate(self.element_array):
                self.cells[i].config(text=value, bg=UIConfig.CELL_DEFAULT)

        self.search_history = hist_arr
        self.iteration = 0
        self.center_label.config(text=f"0 / {len(self.search_history)}")
        self.update_button_status()
    