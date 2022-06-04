import tkinter as tk

app = tk.Tk()

app.geometry('300x300')
app.resizable(0, 0)

backFrame = tk.Frame(master=app,
                    width=200,
                    height=200,
                    bg='blue').pack()

button1 = tk.Button(master=backFrame, 
                    text='Button 1', 
                    bg='blue', 
                    fg='red').pack()
button2 = tk.Button(master=backFrame, 
                    text='Button 2', 
                    bg='blue', 
                    fg='green').pack()
button3 = tk.Label(master=backFrame, 
                   text='Button 3', 
                   bg='red',
                   fg='blue').pack()

app.mainloop()