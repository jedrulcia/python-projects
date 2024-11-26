import tkinter

window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(200,100)
window.config(padx=10,pady=10)

def convert_to_km():
    miles = int(input.get())
    km = miles * 1.60
    label_3.config(text=km)

input = tkinter.Entry()
input.grid(row=0,column=1)

label_1 = tkinter.Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = tkinter.Label(text="is equal to")
label_2.grid(row=1, column=0)

label_3 = tkinter.Label(text="0")
label_3.grid(row=1, column=1)

label_4 = tkinter.Label(text="Km")
label_4.grid(row=1, column=2)

button = tkinter.Button(text="Convert", command=convert_to_km)
button.grid(row=2, column=1)



window.mainloop()