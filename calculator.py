from tkinter import Tk, Entry, Button, StringVar, Frame


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(master, width=17, bg="#fff", font=("Arial Bold", 28),
              textvariable=self.equation).place(x=0, y=0)

        # Define buttons with explicit color for each, including 'white' where no specific color is needed
        buttons = [
            ('(', 0, 50, 'white'), (')', 90, 50, 'white'), ('%', 180, 50, 'white'),
            ('1', 0, 125, 'white'), ('2', 90, 125,
                                     'white'), ('3', 180, 125, 'white'),
            ('4', 0, 200, 'white'), ('5', 90, 200,
                                     'white'), ('6', 180, 200, 'white'),
            ('7', 0, 275, 'white'), ('8', 90, 275,
                                     'white'), ('9', 180, 275, 'white'),
            ('0', 90, 350, 'white'), ('.', 180, 350,
                                      'white'), ('+', 270, 275, 'white'),
            ('-', 270, 200, 'white'), ('/', 270,
                                       50, 'white'), ('*', 270, 125, 'white'),
            ('=', 270, 350, 'lightblue'), ('C', 0, 350, 'white')
        ]

        for text, x, y, bg in buttons:
            Button(master, width=11, height=4, text=text, relief="flat", bg=bg,
                   command=lambda txt=text: self.show(txt) if txt not in "=C" else (self.solve() if txt == "=" else self.clear())).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception as e:
            self.equation.set("Error")
            self.entry_value = ""


root = Tk()
calculator = Calculator(root)
root.mainloop()
