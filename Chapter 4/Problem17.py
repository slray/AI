from Tkinter import *

canvas_width    =   512
canvas_height   =   512

colors = {"green":"#476042"}

master = Tk()
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()



points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 90, 110, 60, 100 ]

w.create_polygon(points, outline=colors["green"], 
            fill='yellow', width=3)

mainloop()