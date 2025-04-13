import tkinter as tk
def key_press(event):
    print(event.keysym)
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    if event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    if event.keysym == 'Left':
        canvas.move(oval, -10, 0)
    if event.keysym == 'Right':
        canvas.move(oval, 10, 0)



win = tk.Tk()
canvas = tk.Canvas(win, bg='#fff', height=600, width=600)
line = canvas.create_line((0, 300), (300,300), fill='red')
line = canvas.create_line((300, 0), (300,300), fill='red')
line = canvas.create_line((600, 0), (300,300), fill='red')
line = canvas.create_line((0, 0), (300,300), fill='red')
line = canvas.create_line((0, 600), (300,300), fill='red')
line = canvas.create_line((600, 600), (300,300), fill='red')
line = canvas.create_line((300, 300), (300,600), fill='red')
line = canvas.create_line((300, 300), (600,300), fill='red')









oval = canvas.create_oval((175,175), (425,425), fill='red')
canvas.pack()
win.bind("<KeyPress>", key_press)
tk.mainloop()
















