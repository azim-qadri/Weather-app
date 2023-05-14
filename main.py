from tkinter import *
from tkinter import font,ttk
import requests
import json

root = Tk()
root.title('Weather')
root.iconbitmap("clipart1294094.ico")
root.resizable(False, False)

def submit():
    try:
        # api key
        # 69279444320403e83591dac64cdf5746
        # geocoding
        geocode = requests.get(
            f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_entry.get()},GB&appid=69279444320403e83591dac64cdf5746')
        g_decode = json.loads(geocode.content)
        lat = g_decode['lat']
        lon = g_decode['lon']

        # Reverse geocoding API to get city name
        reverse_geocode = requests.get(
            f'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid=69279444320403e83591dac64cdf5746')
        rg_decode = json.loads(reverse_geocode.content)
        city_name = rg_decode[0]['name']

        # weather
        weather = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=69279444320403e83591dac64cdf5746')
        w_decode = json.loads(weather.content)
        temp = w_decode['main']

        # Create table
        table = ttk.Treeview(root, style="Custom.Treeview", show=['headings'])
        table["columns"] = ("Parameter", "Value")
        table.column("Parameter", width=200, anchor="center",)
        table.column("Value", width=200, anchor="center")
        table.heading("Parameter", text="Parameter", anchor="center")
        table.heading("Value", text="Value", anchor="center")

        # Insert weather information into the table
        for key, value in temp.items():
            key = key.capitalize()
            table.insert("", "end", values=(key, value))

        # Set font style for table values
        table.tag_configure("Values", font=("Arial", 12), background="#E8F0F7", foreground="#336699")

        # Configure custom style for the table
        table_style = ttk.Style()
        table_style.configure("Custom.Treeview",
                              background="#E8F0F7",
                              foreground="#336699",
                              fieldbackground="#E8F0F7",
                              bordercolor="#CCCCCC",
                              highlightthickness=0,
                              font=("Helvetica", 13, "bold")),

        # Grid layout for the table
        table.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=(0, 0))
        city_label = ttk.Label(root, text=f"City: {city_name}", style="CityLabel.TLabel")
        city_label.grid(row=1, column=0, columnspan=3, pady=(0, 1))

        # Adjust column weights for responsive resizing
        root.grid_columnconfigure(0, weight=1)

        # Adjust window size based on table content
        root.update()
        root.geometry(f"{table.winfo_width() + 20}x{table.winfo_height() + 20}")

    except Exception as e:
        print(e)


# Set bg
root.configure(bg="#E8F0F7")

# Set font style
font_style = font.Font(family="Helvetica", size=20, weight="bold", slant="italic")

# Set text colors
label_text_color = "#336699"  # Dark blue
entry_text_color = "#BFEFFF"  # Black
button_text_color = "#FFFFFF"  # White

# Zip code label
zip_label = Label(root, text='Enter zip code', font=font_style, bg="#E8F0F7", fg=label_text_color)
zip_label.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

# Zip code entry
zip_entry = Entry(root, font=font_style, fg=entry_text_color)  # eg code:SW1A 1AA
zip_entry.grid(row=0, column=1, sticky='ew', padx=10, pady=10)

# Submit button
btn = Button(root, text='Get', command=submit, font=font_style, bg="#C0C0C0", fg=button_text_color)
btn.grid(row=0, column=2, sticky='ew', padx=10, pady=10)

root.mainloop()
