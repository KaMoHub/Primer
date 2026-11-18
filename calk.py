import tkinter as tk
window = tk.Tk()
window.geometry('300x500')
window.title('Calk')
window.configure(bg='grey')
entry = tk.Entry(window, width=50)
entry.grid(row=0, column=0)




def click(text):
    cur = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, cur+str(text))

def clear():
    entry.delete(0, tk.END)

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0,str(result))

button = tk.Button(window, text=' = ', command=calculate)
button.grid(row=1, column=0)
button = tk.Button(window, text='7', command=lambda: click('7'))
button.grid(row=1, column=1)
button = tk.Button(window, text='8', command=lambda: click('8'))
button.grid(row=1, column=2)
button = tk.Button(window, text='9', command=lambda: click('8'))
button.grid(row=1, column=3)
button = tk.Button(window, text='*', command=lambda: click('8'))
button.grid(row=1, column=4)
button = tk.Button(window, text='C', command=clear)
button.grid(row=2, column=4)



window.mainloop()