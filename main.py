import tkinter as tk
import ttkbootstrap as ttk

# Functionality


def convert():
    try:
        miles_to_convert = input_value.get()
        converted_to_km = float(miles_to_convert) * 1.61
        output_value.set(f"{str(converted_to_km)} Kilometer(s)")
    except:
        output_value.set("No input.")


# Main window
app = ttk.Window(themename='solar')
app.title("Converter")
app.geometry("300x150")

# Title
title = ttk.Label(
    master=app,
    text="Miles to Kilometers",
    font="Calibri 24"
)
title.pack()


# Window Icon
icon = tk.PhotoImage(file='./assets/scale.png')
app.iconphoto(False, icon)

# Inputs
input_frame = ttk.Frame(master=app)

input_value = tk.StringVar()
input_field = ttk.Entry(
    master=input_frame,
    textvariable=input_value
)


# Conversion
convert_button = ttk.Button(
    master=input_frame,
    text="Convert",
    command=convert
)


# Packing and Arrangement
input_field.pack(side='left', padx=20)
convert_button.pack(side='left')
input_frame.pack(pady=20)


# Outputs
output_value = tk.IntVar()
output_field = ttk.Label(
    master=app,
    text="[OUTPUT]",
    font="Calibri",
    textvariable=output_value
)

output_field.pack()


# Run
if __name__ == "__main__":
    app.mainloop()
