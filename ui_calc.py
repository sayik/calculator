import tkinter as tk
from tkinter import ttk
from cl_calculator import ui_input

##tasks
# take button input - done!
# take keyboard input - done!
# fix issues with args - done!
# list previous calculation on right - complicated not done!
# refactor buttons - done!
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

        frame.set_history_box(frame_history)


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


    def add_to_list(self, _event=None):
        text = self.entry.get()
        if text:
            self.entry.delete(0, tk.END)

    def clear_list(self):
        self.entry.delete(0, tk.END)

    def button_input(self, input):
        self.entry.insert(tk.END, input)

    def pipeline(self, _=None):
        text = self.entry.get()
        if text:
            result = ui_input(text)
            self.entry.delete(0, tk.END)
            if result is None:
                self.entry.delete(0, tk.END)
            else:
                shared_string.append(f"{text} = {result}")
                self.history_box.inset_text()
                self.entry.insert(tk.END, result)

    def set_history_box(self, history_box):
        """Set the reference to the history box."""
        self.history_box = history_box



class LabelBox(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(
            self, text="History", anchor="center", border=2, relief="groove"
        )
        self.label.grid(row=0, column=3, columnspan=3, sticky="we")

        self.text_list = tk.Listbox(self, border=2, relief="groove")
        self.text_list.grid(row=1, column=3, columnspan=3, sticky="nsew")
        self.text_list.insert(tk.END, shared_string)
    
    def inset_text(self):
        self.text_list.delete(0, tk.END)
        for i in shared_string:
            self.text_list.insert(tk.END, i)


if __name__ == "__main__":
    main()
