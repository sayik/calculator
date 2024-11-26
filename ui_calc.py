import tkinter as tk
from tkinter import ttk
from cl_calculator import ui_input

##tasks
# take button input - done!
# take keyboard input - done!
# fix issues with args - done!
# list previous calculation on right - complicated not done!
# fix scaling
# use threading to make it work seamlessly

shared_string: list[str] = []


def main():
    app = Application()
    app.mainloop()


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, weight=3)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(0, weight=6)

        frame = InputForm(self)
        frame.grid(row=0, column=0, padx=5, pady=5)

        frame_history = LabelBox(self)
        frame_history.grid(row=0, column=1, padx=5, pady=5)


class InputForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)

        self.entry = ttk.Entry(self, justify="right")
        self.entry.grid(
            row=0,
            column=0,
            columnspan=2,
            rowspan=2,
            sticky="ewns",
            ipady=10,
        )
        self.entry.focus()
        self.entry.bind("<Return>", self.pipeline)

        self.entry_btn = ttk.Button(self, text="=", command=self.pipeline)
        self.entry_btn.grid(row=0, column=2)

        self.entry_btn2 = ttk.Button(self, text="AC", command=self.clear_list)
        self.entry_btn2.grid(row=1, column=2)

        # NUM PAD

        elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, "-", 0, "+", "*", "**", "/"]

        start_index = 0
        number_rows = 5

        for j in range(number_rows):
            for i in range(start_index, start_index + 3):
                self.entry_btn = ttk.Button(
                    self,
                    text=elements[i],
                    command=lambda val=elements[i]: self.button_input(val),
                )
                self.entry_btn.grid(row=j + 2, column=i - start_index)
            start_index += 3

            """Note on lambda function here - Why It Appears to Only Return the val:
Each time you call a lambda, it just returns the default argument value (val), 
which was set when the lambda was created. Since each lambda has its own 
local val (the value of x at the time the lambda was defined), calling the lambdas will 
give you a list of values from 0 to 4. Also remember the concept of late binding"""

    def add_to_list(self, _event=None):
        text = self.entry.get()
        if text:
            # self.entry.insert(tk.END, text)
            self.entry.delete(0, tk.END)

    def clear_list(self):
        self.entry.delete(0, tk.END)

    def button_input(self, input):
        # print(input)
        self.entry.insert(tk.END, input)

    def pipeline(self, _=None):
        text = self.entry.get()
        if text:
            result = ui_input(text)
            self.entry.delete(0, tk.END)
            if result is None:
                self.entry.delete(0, tk.END)
            else:
                shared_string.append(f"{result} = {text}")
                self.entry.insert(tk.END, result)


class LabelBox(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(
            self, text="History", anchor="center", border=2, relief="groove"
        )
        self.label.grid(row=0, column=3, columnspan=3, sticky="we")

        self.text_list = tk.Listbox(self, border=2, relief="groove")
        self.text_list.grid(row=1, column=3, columnspan=3, sticky="nsew")

    def inset_text(self):
        for i in shared_string:
            self.text_list.insert(tk.END, i)


if __name__ == "__main__":
    main()
