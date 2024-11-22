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
        self.entry_btn3 = ttk.Button(
            self, text="1", command=lambda: self.button_input(1)
        )
        self.entry_btn3.grid(row=2, column=0)

        self.entry_btn4 = ttk.Button(
            self, text="2", command=lambda: self.button_input(2)
        )
        self.entry_btn4.grid(row=2, column=1)

        self.entry_btn5 = ttk.Button(
            self, text="3", command=lambda: self.button_input(3)
        )
        self.entry_btn5.grid(row=2, column=2)

        self.entry_btn6 = ttk.Button(
            self, text="4", command=lambda: self.button_input(4)
        )
        self.entry_btn6.grid(row=3, column=0)

        self.entry_btn7 = ttk.Button(
            self, text="5", command=lambda: self.button_input(5)
        )
        self.entry_btn7.grid(row=3, column=1)

        self.entry_btn8 = ttk.Button(
            self, text="6", command=lambda: self.button_input(6)
        )
        self.entry_btn8.grid(row=3, column=2)

        self.entry_btn9 = ttk.Button(
            self, text="7", command=lambda: self.button_input(7)
        )
        self.entry_btn9.grid(row=4, column=0)

        self.entry_btn10 = ttk.Button(
            self, text="8", command=lambda: self.button_input(8)
        )
        self.entry_btn10.grid(row=4, column=1)

        self.entry_btn11 = ttk.Button(
            self, text="9", command=lambda: self.button_input(9)
        )
        self.entry_btn11.grid(row=4, column=2)

        self.entry_btn12 = ttk.Button(
            self, text="-", command=lambda: self.button_input("-")
        )
        self.entry_btn12.grid(row=5, column=0)

        self.entry_btn13 = ttk.Button(
            self, text="0", command=lambda: self.button_input(0)
        )
        self.entry_btn13.grid(row=5, column=1)

        self.entry_btn14 = ttk.Button(
            self, text="+", command=lambda: self.button_input("+")
        )
        self.entry_btn14.grid(row=5, column=2)

        self.entry_btn15 = ttk.Button(
            self, text="*", command=lambda: self.button_input("*")
        )
        self.entry_btn15.grid(row=6, column=0)

        self.entry_btn16 = ttk.Button(
            self, text="/", command=lambda: self.button_input("/")
        )
        self.entry_btn16.grid(row=6, column=1)

        self.entry_btn17 = ttk.Button(
            self, text="%", command=lambda: self.button_input("%")
        )
        self.entry_btn17.grid(row=6, column=2)

        for i in range(0, 3):
            self.entry_btn17 = ttk.Button(
                self, text="%", command=lambda: self.button_input("%")
            )
        self.entry_btn17.grid(row=6, column=2)

    def add_to_list(self, _event=None):
        text = self.entry.get()
        if text:
            # self.entry.insert(tk.END, text)
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
