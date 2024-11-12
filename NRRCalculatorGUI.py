import tkinter as tk
from decimal import Decimal , getcontext

root = tk.Tk()

root.title("NRR Calculator App")
root.geometry('300x400')

lbl1 = tk.Label(root , text = "Welcome to NRR Calculator!")
lbl2 = tk.Label(root , text = "Total runs scored: ")
lbl3 = tk.Label(root , text = "Total overs faced: ")
lbl4 = tk.Label(root , text = "Total runs conceded: ")
lbl5 = tk.Label(root , text = "Total overs bowled: ")
lbl6 = tk.Label(root , text = "")

ent1 = tk.Entry(root , width = 10)
ent2 = tk.Entry(root , width = 10)
ent3 = tk.Entry(root , width = 10)
ent4 = tk.Entry(root , width = 10)

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


btn = tk.Button(root , text = "Calculate NRR" , command = calculateNRR)

lbl1.pack()
lbl2.pack()
ent1.pack()
lbl3.pack()
ent2.pack()
lbl4.pack()
ent3.pack()
lbl5.pack()
ent4.pack()
btn.pack()
lbl6.pack()

root.mainloop()