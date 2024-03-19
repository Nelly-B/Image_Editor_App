from tkinter import ttk, Tk, PhotoImage


root = Tk()

ttk.Label(root, text='this is a text label').pack()

ttk.Label(root, text='this is my second label').pack()

def triggered_func():
    print('I was clicked')

ttk.Button(root, text='Click me', command=triggered_func).pack()

logo = PhotoImage(file='python-logo-notext.svg.png').subsample(20,20)
ttk.Label(root, image=logo).pack()

root.mainloop()