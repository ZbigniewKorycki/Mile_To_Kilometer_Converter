import tkinter


def calculate_miles_to_km():
    km = float(input.get()) * 1.609
    result.config(text=km)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles", font=("Arial", 12))
label_miles.grid(column=2, row=0)

label_result = tkinter.Label(text="Is equal to", font=("Arial", 12))
label_result.grid(column=0, row=1)

result = tkinter.Label(font=("Arial", 24))
result.grid(column=1, row=1)

label_km = tkinter.Label(text="Km", font=("Arial", 12))
label_km.grid(column=2, row=1)

button_calculate = tkinter.Button(text="Calculate", command=calculate_miles_to_km)
button_calculate.grid(column=1, row=2)


window.mainloop()
