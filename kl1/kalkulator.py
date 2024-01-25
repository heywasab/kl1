from tkinter import *

def create_button(text, row, column, columnspan=1, command=None):
    button = Button(text=text, width=5, height=2, command=command)
    button.grid(row=row, column=column, columnspan=columnspan)
    return button

def click(button_text):
    if button_text == 'C':
        entry.delete(0, END)
    elif button_text == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(0, result)
        except:
            entry.delete(0, END)
            entry.insert(0, 'Error')
    else:
        entry.insert(END, button_text)

root = Tk()
root.title('Calculator')

entry = Entry(root, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

create_button('1', 1, 0, command=lambda: click('1'))
create_button('2', 1, 1, command=lambda: click('2'))
create_button('3', 1, 2, command=lambda: click('3'))
create_button('+', 1, 3, command=lambda: click('+'))

create_button('4', 2, 0, command=lambda: click('4'))
create_button('5', 2, 1, command=lambda: click('5'))
create_button('6', 2, 2, command=lambda: click('6'))
create_button('-', 2, 3, command=lambda: click('-'))

create_button('7', 3, 0, command=lambda: click('7'))
create_button('8', 3, 1, command=lambda: click('8'))
create_button('9', 3, 2, command=lambda: click('9'))
create_button('*', 3, 3, command=lambda: click('*'))

create_button('C', 4, 0, command=lambda: click('C'))
create_button('0', 4, 1, command=lambda: click('0'))
create_button('=', 4, 2, columnspan=2, command=lambda: click('='))
create_button('/', 4, 3, command=lambda: click('/'))

root.mainloop()
