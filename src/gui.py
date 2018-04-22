from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import fnmatch
import funcs, data

class start_window:
    def __init__(self):
        top = Tk()

        file_frame = Frame(top)
        Label(file_frame, text="Gene file").pack(side=LEFT)
        Button(file_frame, text="Browse", command = self.file_browse).pack(side=RIGHT)
        self.file_entry = Entry(file_frame, textvariable=StringVar, width=100)
        self.file_entry.pack(side=LEFT)
        self.file_entry.insert(0, "No file selected")
        file_frame.pack(side=TOP, fill=X)

        mass_frame = Frame(top)
        Label(mass_frame, text = "Mass min. (Dalton)").grid(row = 1, column = 0)
        self.entry_input_lower_mass = Entry(mass_frame)
        self.entry_input_lower_mass.grid(row = 1, column = 1)
        Label(mass_frame, text = "Mass max. (Dalton)").grid(row = 2, column = 0)
        self.entry_input_upper_mass = Entry(mass_frame)
        self.entry_input_upper_mass.grid(row = 2, column = 1)
        # TODO move panel to left side
        mass_frame.pack()

        result_frame = Frame(top)
        self.scrollbar = Scrollbar(result_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.result_window = Text(result_frame, yscrollcommand=self.scrollbar.set)
        self.result_window.pack(fill=BOTH)
        self.result_window.insert(INSERT, "")
        self.scrollbar.config(command=self.result_window.yview())
        result_frame.pack(fill=BOTH)

        button_frame=Frame(top)
        self.search_button = Button(button_frame, text="Search", command = self.data_search)
        self.search_button.pack(side=LEFT)
        self.clear_result = Button(button_frame, text="Clear", command=self.clear_results)
        self.clear_result.pack(side=LEFT)
        button_frame.pack()

        top.mainloop()

    def file_browse(self):
        dir = os.getcwd()
        self.filename = filedialog.askopenfilename(initialdir=dir, title="Select file")
        self.file_entry.delete(0, END)
        self.file_entry.insert(0, self.filename)


    def data_search(self):
        try:
            file = self.filename
        except:
            self.no_file_callback()
            raise

        if os.path.isfile(file) and fnmatch.fnmatch(file, '*.gb'):
            pass
        else:
            self.no_file_callback()
            return False

        try:
            mass_low = int(self.entry_input_lower_mass.get())
        except ValueError:
            self.wrong_entry_callback()
            raise

        try:
            mass_high = int(self.entry_input_upper_mass.get())
        except ValueError:
            self.wrong_entry_callback()
            raise
        self.result_window.delete(1.0, END)
        found_data = funcs.gene_find_func(file, mass_low, mass_high)
        result_string = funcs.write_results(found_data)
        self.result_window.insert(INSERT, result_string)

    def clear_results(self):
        self.result_window.delete(1.0, END)

    def wrong_entry_callback(self):
        msg = messagebox.showinfo("Invalid entry", "Please enter an integer")


    def no_file_callback(self):
        msg = messagebox.showinfo("No file found", "Please use existing '*gb'-file")