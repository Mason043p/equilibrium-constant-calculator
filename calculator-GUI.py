GUIfrom tkinter import *

root = Tk()

def mkLabel(labelName, text):
    labelName = Label(root, text = text)
    labelName.pack(side=TOP)


mkLabel("a_label", "Input the starting value of a")
a_entry = Entry(root, width=50)
a_entry.pack(side=TOP)


mkLabel("b_label", "Input the starting value of b")

b_entry = Entry(root, width=50)
b_entry.pack(side=TOP)

mkLabel("forward_rate_label", "Input the value of the forward rate constant as a decimal")

forward_rate_entry = Entry(root, width=50)
forward_rate_entry.pack(side=TOP)


mkLabel("reverse_rate_label", "Input the value of the forward rate constant as a decimal")

reverse_rate_entry = Entry(root, width=50)
reverse_rate_entry.pack(side=TOP)

number_of_calculations_label = Label(root, text = "Input the amount of calculations you wish to run")
number_of_calculations_label.pack()

number_of_calculations_entry = Entry(root, width=50)
number_of_calculations_entry.pack(side=TOP)

def formula():
    a = float(a_entry.get())
    b = float(b_entry.get())
    forward_rate_constant = float(forward_rate_entry.get())
    reverse_rate_constant = float(reverse_rate_entry.get())
    for i in range(int(number_of_calculations_entry.get())):
        a = a - a * forward_rate_constant  
        a = a + b * reverse_rate_constant
        b = b * reverse_rate_constant + a * forward_rate_constant
        q = b / a
        output_label = Label(root, text = f"a = {a} | b = {b} | q = {q}")
        output_label.pack()
    
  
    

formButton = Button(root, text="Click to run calculations", command=formula)
formButton.pack()

root.mainloop()



