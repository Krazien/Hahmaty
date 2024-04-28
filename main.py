import tkinter as tk
size = 400
amount = 8
diametr = size/amount
win = tk.Tk()
canvans = tk.Canvas(win, width=size, height=size)
for i in range(0, size, size//amount):
    canvans.create_line((i, 0),(i, size))
    canvans.create_line((0, i), (size, i))
for y in range(3):
    for x in range(4):
        x_real = (x*2 +(y%2)) * diametr
        y_real = y *diametr
        canvans.create_oval((x_real, y_real), (x_real + diametr, y_real + diametr), fill='lightgreen')
for y in range (5, amount):
    for x in range (4):
        x_real = (x * 2 + (y % 2)) * diametr
        y_real = y * diametr
        canvans.create_oval((x_real, y_real), (x_real + diametr, y_real + diametr), fill='lightblue')
canvans.pack()
win.mainloop()