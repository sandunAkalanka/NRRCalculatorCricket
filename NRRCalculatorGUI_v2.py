import tkinter as tk
from tkinter import ttk
import sv_ttk
from decimal import Decimal , getcontext

root = tk.Tk()

root.title("NRR Calculator App")
root.geometry('300x400')
root.resizable(0 , 0)

lbl1 = ttk.Label(root , text = "Welcome to NRR Calculator!")
lbl2 = ttk.Label(root , text = "Total runs scored: ")
lbl3 = ttk.Label(root , text = "Total overs faced: ")
lbl4 = ttk.Label(root , text = "Total runs conceded: ")
lbl5 = ttk.Label(root , text = "Total overs bowled: ")
lbl6 = ttk.Label(root , text = "")

ent1 = ttk.Entry(root , width = 10)
ent2 = ttk.Entry(root , width = 10)
ent3 = ttk.Entry(root , width = 10)
ent4 = ttk.Entry(root , width = 10)

def calculateNRR():
    runs_for = ent1.get()
    overs_for = ent2.get()
    runs_against = ent3.get()
    overs_against = ent4.get()

    getcontext().prec = 4

    nrr_for = Decimal(runs_for) / Decimal(overs_for)
    nrr_against = Decimal(runs_against) / Decimal(overs_against)
    nrr = nrr_for - nrr_against
    nrr_text = "NRR is " + str(nrr)

    lbl6.configure(text = nrr_text)

btn1 = ttk.Button(root , text = "Calculate NRR" , command = calculateNRR)

lbl1.pack()
lbl2.pack()
ent1.pack()
lbl3.pack()
ent2.pack()
lbl4.pack()
ent3.pack()
lbl5.pack()
ent4.pack()
btn1.pack()
lbl6.pack()

sv_ttk.set_theme("dark")

root.mainloop()