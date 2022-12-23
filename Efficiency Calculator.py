from tkinter import *
from math import*
from tkinter import messagebox

window =Tk()
window.title("Efficiency calculator")
window.geometry("1210x700")
label1=Label(window)


def Show():
    Rp= float(Primary_Resistance_ent.get())
    Xp= float(Primary_Resistance_ent.get())
    Rs= float(Secondary_Resistance_ent.get())
    Rc= float(core_resistance_ent.get())
    Xm= float(Magnetising_Reactance_ent.get())
    Xs= float(Secondary_Reactance_ent.get())
    K = float(Turns_Ratio_ent.get())
    Io = float(open_circuit_current_ent.get())


    P_load=float(Load_Ratings_ent.get())
    R_load= float(Load_Resistance_ent.get())
    X_load= float(Load_Reactance_ent.get())


    a = (R_load**2)+(X_load**2)
    b= float(sqrt (a))
    Power_factor= (R_load/b)
    c = (P_load/b)
    I2 = float(sqrt (c))
    V2 = float(I2*b)
    Ip = Io + (K*I2)
    Copper_Loss = ((Ip**2)*Rp) + ((I2**2)*Rs) 
    d = float((Rc*Xm)/(Rc+Xm))
    Core_loss = (Io**2)*d
    p = V2*I2*Power_factor
    effi = p/(p+Core_loss+Copper_Loss)


    label1.configure(text=''+f"{effi}",font=" Calibri(Body) 10 bold",fg="Forestgreen")
    label1.grid(row=13,column=3)


    if (effi)<1:
        messagebox.showwarning("Warning","Change inputs of Load Parameters so that efficiency of the transformer can be increased")



Label(window,text="Transformer Equivalent Parameters",font=" Calibri(Body) 15 bold").grid(row=0,column=2,pady=10)
Primary_Resistance =Label(window,text="Rp(ohms)",font=" Calibri(Body) 10 bold")
Primary_Reactance =Label(window,text="Xp(ohms)  ",font=" Calibri(Body) 10 bold")
Secondary_Resistance =Label(window,text="Rs(ohms)",font=" Calibri(Body) 10 bold")
core_resistance  = Label(window,text="Rc(ohms)",font=" Calibri(Body) 10 bold")
Magnetising_Reactance = Label(window,text="Xm(ohms)  ",font=" Calibri(Body) 10 bold")
Secondary_Reactance  = Label(window,text="Xs(ohms)  ",font=" Calibri(Body) 10 bold")
Turns_Ratio  = Label(window,text="K (Ns/Np)",font=" Calibri(Body) 10 bold")
open_circuit_current  = Label(window,text="Io(Amp)  ",font=" Calibri(Body) 10 bold")


Label(window,text="Load Parameters",font=" Calibri(Body) 15 bold").grid(row=5,column=2,pady=10)
Load_Ratings = Label(window,text="P(load) in KVA",font=" Calibri(Body) 10 bold")
Load_Resistance  = Label(window,text="RL(ohms)",font=" Calibri(Body) 10 bold")
Load_Reactance  = Label(window,text="XL(ohms)",font=" Calibri(Body) 10 bold")


Primary_Resistance.grid(row=1,column=1)
Primary_Reactance.grid(row=1,column=3)
Secondary_Resistance.grid(row=2,column=1)
Secondary_Reactance.grid(row=2,column=3)
core_resistance.grid(row=3,column=1)
Magnetising_Reactance.grid(row=3,column=3)
Turns_Ratio.grid(row=4,column=1)
open_circuit_current.grid(row=4,column=3)


Load_Ratings.grid(row=6,column=1)
Load_Resistance.grid(row=6,column=3)
Load_Reactance.grid(row=7,column=1)


Primary_Resistance_val = DoubleVar()
Primary_Reactance_val = DoubleVar()
Secondary_Resistance_val = DoubleVar()
core_resistance_val = DoubleVar()
Magnetising_Reactance_val = DoubleVar()
Secondary_Reactance_val = DoubleVar()
Turns_Ratio_val = DoubleVar()
open_circuit_current_val = DoubleVar()


Load_Ratings_val = DoubleVar()
Load_Resistance_val = DoubleVar()
Load_Reactance_val = DoubleVar()


Primary_Resistance_ent =Entry(window,textvariable=Primary_Resistance_val,borderwidth=7,font="Calibri(Body) 10 bold",relief=SUNKEN)
Primary_Reactance_ent =Entry(window,textvariable=Primary_Reactance_val,borderwidth=7,font="Calibri(Body) 10 bold",relief=SUNKEN)
Secondary_Resistance_ent =Entry(window,textvariable=Secondary_Resistance_val,borderwidth=7,font="Calibri(Body) 10 bold",relief=SUNKEN)
core_resistance_ent =Entry(window,textvariable=core_resistance_val,borderwidth=7,font="Calibri(Body) 10 bold",relief=SUNKEN)
Magnetising_Reactance_ent =Entry(window,textvariable=Magnetising_Reactance_val,borderwidth=7,font="Calibri(Body) 10 bold",relief=SUNKEN)
Secondary_Reactance_ent =Entry(window,textvariable=Secondary_Reactance_val,borderwidth=7,font="Calibri(Body) 10 bold",relief=SUNKEN)
Turns_Ratio_ent =Entry(window,textvariable=Turns_Ratio_val,borderwidth=7,font="Calibri(Body) 10 bold",relief=SUNKEN)
open_circuit_current_ent =Entry(window,textvariable=open_circuit_current_val,borderwidth=7,font="Calibri(Body) 10 bold",relief=SUNKEN)


Load_Ratings_ent =Entry(window,textvariable=Load_Ratings_val,borderwidth=7,font="Calibri(Body) 10 bold",relief=SUNKEN)
Load_Resistance_ent =Entry(window,textvariable=Load_Resistance_val,borderwidth=7,font="Calibri(Body) 10 bold",relief=SUNKEN)
Load_Reactance_ent =Entry(window,textvariable=Load_Reactance_val,borderwidth=7,font="Calibri(Body) 10 bold",relief=SUNKEN)


Primary_Resistance_ent.grid(row=1,column=2,pady=4)
Primary_Reactance_ent.grid(row=1,column=4,pady=4)
Secondary_Resistance_ent.grid(row=2,column=2,pady=4)
Secondary_Reactance_ent.grid(row=2,column=4,pady=4)
core_resistance_ent.grid(row=3,column=2,pady=4)
Magnetising_Reactance_ent.grid(row=3,column=4,pady=4)
Turns_Ratio_ent.grid(row=4,column=2,pady=4)
open_circuit_current_ent.grid(row=4,column=4,pady=4)


Load_Ratings_ent.grid(row=6,column=2,pady=4)
Load_Resistance_ent.grid(row=6,column=4,pady=4)
Load_Reactance_ent.grid(row=7,column=2,pady=4)


# R_load= float(Load_Resistance_ent.get())
# X_load= float(Load_Reactance_ent.get())



button =Button(window,text="Output",command=Show,font=" Calibri(Body) 10 bold",width=15,height=1,fg="white",bg="Black")
button.grid(row=8,column=2,padx=10,pady=10)


efficiency= Label(window,text="Efficiency of the transformer is  :-",font=" Calibri(Body) 15 bold",fg="Forestgreen")
efficiency.grid(row=13,column=1)

photo = PhotoImage(file="Image.png")
Equivalent_Label = Label(image=photo)
Equivalent_Label.grid(row=16,column=4)


name=Label(window,text="By :- Divyansh garg",font=" Calibri(Body) 10 bold",fg="red")
name.grid(row=16,column=2)

window.mainloop()