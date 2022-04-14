import tkinter as tk

def setTextInput(text):
    symbol = ["+", "-", "*", "/"]
    lastChar = TextBox.get("end-2c", "end-1c")


    if lastChar in symbol:
        if text in symbol:
            TextBox.delete("end-2c", "end")
            TextBox.insert(tk.END, text)
        else:
            TextBox.insert(tk.END, text)
    else:
        TextBox.insert(tk.END, text)

def result():
    command = TextBox.get(1.0, tk.END)
    TextBox.delete("1.0", "end")
    TextBox.insert(tk.END, str(eval(command)))

def BackSpace():
    TextBox.delete("end-2c", "end")

def clear():
    TextBox.delete("1.0", "end")

root = tk.Tk()
root.resizable(False, False)
root.title("Test Calculator")
FrameText = tk.Frame(root)
FrameGrid = tk.Frame(root)
FrameGrid.pack(side=tk.BOTTOM)
FrameText.pack(side=tk.TOP)

Label = tk.Label(FrameText, text="Calculator")
TextBox = tk.Text(FrameText, height=1, width=30)

Button0 = tk.Button(FrameGrid, text="0", height=2, width=3, command=lambda: setTextInput("0"))
Button1 = tk.Button(FrameGrid, text="1", height=2, width=3, command=lambda: setTextInput("1"))
Button2 = tk.Button(FrameGrid, text="2", height=2, width=3, command=lambda: setTextInput("2"))
Button3 = tk.Button(FrameGrid, text="3", height=2, width=3, command=lambda: setTextInput("3"))
Button4 = tk.Button(FrameGrid, text="4", height=2, width=3, command=lambda: setTextInput("4"))
Button5 = tk.Button(FrameGrid, text="5", height=2, width=3, command=lambda: setTextInput("5"))
Button6 = tk.Button(FrameGrid, text="6", height=2, width=3, command=lambda: setTextInput("6"))
Button7 = tk.Button(FrameGrid, text="7", height=2, width=3, command=lambda: setTextInput("7"))
Button8 = tk.Button(FrameGrid, text="8", height=2, width=3, command=lambda: setTextInput("8"))
Button9 = tk.Button(FrameGrid, text="9", height=2, width=3, command=lambda: setTextInput("9"))
ButtonAdd = tk.Button(FrameGrid, text="+", height=2, width=3, command=lambda: setTextInput("+"))
ButtonSub = tk.Button(FrameGrid, text="-", height=2, width=3, command=lambda: setTextInput("-"))
ButtonMul = tk.Button(FrameGrid, text="*", height=2, width=3, command=lambda: setTextInput("*"))
ButtonDiv = tk.Button(FrameGrid, text="/", height=2, width=3, command=lambda: setTextInput("/"))
ButtonDot = tk.Button(FrameGrid, text=".", height=2, width=10, command=lambda: setTextInput("."))
ButtonBackspace = tk.Button(FrameGrid, text="C", height=2, width=3, command=lambda: BackSpace())
ButtonClear = tk.Button(FrameGrid, text="CA", height=8, width=3, command=lambda: clear())
ButtonEqual = tk.Button(FrameGrid, text="=", height=2, width=31, command=lambda: result())

Label.pack()
TextBox.pack()

Button0.grid(row=4, column=1)
Button1.grid(row=1, column=1)
Button2.grid(row=1, column=2)
Button3.grid(row=1, column=3)
Button4.grid(row=2, column=1)
Button5.grid(row=2, column=2)
Button6.grid(row=2, column=3)
Button7.grid(row=3, column=1)
Button8.grid(row=3, column=2)
Button9.grid(row=3, column=3)
ButtonAdd.grid(row=1, column=4)
ButtonSub.grid(row=2, column=4)
ButtonMul.grid(row=3, column=4)
ButtonDiv.grid(row=4, column=4)
ButtonDot.grid(row=4, column=2, columnspan=2)
ButtonEqual.grid(row=5, column=1, columnspan=5)
ButtonBackspace.grid(row=1, column=5)
ButtonClear.grid(row=2, column=5, rowspan=3)

root.mainloop()
