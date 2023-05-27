from tkinter import *
from tkinter import font, ttk
from PIL import Image, ImageTk
import requests
import json
import ctypes


ctypes.windll.shcore.SetProcessDpiAwareness(2)
root = Tk()
root.title('Weather')
root.iconbitmap("clipart1294094.ico")

zip_entry = Entry()
location_entry = Entry()
z = 2
table = ttk.Treeview()
city_label = ttk.Label()
zip_image = ImageTk.PhotoImage(Image.open('zip-code.png').resize((50, 50)))
location_image = ImageTk.PhotoImage(Image.open('city.png').resize((50, 50)))
get_image = ImageTk.PhotoImage(Image.open('get.png').resize((50,50)))


def zipcode():
    global zip_entry, btn2, btn1, z, table, city_label, location_image, get_image
    z = 0
    btn1.grid_forget()
    location_entry.grid_forget()
    # Zip code label
    zip_entry = Entry(root, font=font_style, fg=entry_text_color)  # eg code:SW1A 1AA
    zip_entry.grid(row=0, column=0, sticky='ew', padx=20, pady=10, ipadx=50, ipady=10)
    zip_entry.focus()
    btn2.grid_forget()
    btn2 = Button(root, command=location, image=location_image, bd=0)
    btn2.grid(row=0, column=2, sticky='ew', padx=10, pady=10)

    # Submit button
    btn = Button(root, command=submit, image=get_image, bd=0)
    btn.grid(row=0, column=3, sticky='ew', padx=10, pady=10)
    table.grid_forget()
    city_label.grid_forget()
    root.geometry(f"{500 + 20}x{100 + 20}")


def location():
    global location_entry, btn2, btn1, z, table, city_label, zip_image, get_image
    z = 1
    btn2.grid_forget()
    zip_entry.grid_forget()
    # location label
    location_entry = Entry(root, font=font_style, fg=entry_text_color)  # eg code:SW1A 1AA
    location_entry.grid(row=0, column=0, sticky='ew', padx=20, pady=10, ipadx=50, ipady=10)
    location_entry.focus()
    btn1.grid_forget()
    btn1 = Button(root, command=zipcode, image=zip_image, bd=0)
    btn1.grid(row=0, column=2, sticky='ew', padx=10, pady=10)
    # Submit button
    btn = Button(root, command=submit, image=get_image, bd=0)
    btn.grid(row=0, column=3, sticky='ew', padx=10, pady=10)
    table.grid_forget()
    city_label.grid_forget()
    root.geometry(f"{500 + 20}x{100 + 20}")


def submit():
    global table, city_label
    try:
        city_name = location_entry.get()
        if z == 0:
            # api key
            # geocoding
            geocode = requests.get(
                f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_entry.get()},GB&appid=#api key here')
            g_decode = json.loads(geocode.content)
            lat = g_decode['lat']
            lon = g_decode['lon']

            # Reverse geocoding API to get city name
            reverse_geocode = requests.get(
                f'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid=#api key here')
            rg_decode = json.loads(reverse_geocode.content)
            city_name = rg_decode[0]['name']

            # weather
            weather = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=#api key here')
            w_decode = json.loads(weather.content)
            temp = w_decode['main']
        else:
            # weather
            weather = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={location_entry.get()}&appid=#api key here')
            w_decode = json.loads(weather.content)
            temp = w_decode['main']
        # Create table
        table = ttk.Treeview(root, style="Custom.Treeview", show=['headings'],)
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
        table.tag_configure("Values", font=("Helvetica", 16, "bold"), background="#E8F0F7", foreground="#336699")

        # Configure custom style for the table
        table_style = ttk.Style()
        table_style.configure("Custom.Treeview",
                              background="F6F1F1",
                              foreground="#336699",
                              fieldbackground="#E8F0F7",
                              bordercolor="#CCCCCC",
                              highlightthickness=0,
                              font=("Helvetica", 13, "bold"),
                              rowheight=40),
        table_style.configure("Custom.Treeview.Heading", font=("Helvetica", 16, "bold"), foreground="#1D267D")
        # Grid layout for the table
        table.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=(0, 0), padx=(70, 0))
        city_label = ttk.Label(root, text=f"City: {city_name}", style="CityLabel.TLabel")
        city_label.grid(row=1, column=0, columnspan=3, pady=(35, 5), padx=(0, 210))

        # Adjust column weights for responsive resizing
        root.grid_columnconfigure(0, weight=1)

        # Adjust window size based on table content
        root.update()
        root.geometry(f"{500 + 20}x{table.winfo_height() + 20}")

    except Exception as e:
        print(e)


def handle_key(event):
    if event.keysym == "Return":
        submit()


# Set bg
root.configure(bg="#E8F0F7")
root.geometry(f"{500 + 20}x{100 + 20}")
# Set font style
font_style = font.Font(family="Helvetica", size=12, weight="bold", slant="italic")

# Set text colors
label_text_color = "#336699"  # Dark blue
entry_text_color = "#BFEFFF"  # Black
button_text_color = "#FFFFFF"  # White
root.configure(pady=20)

btn1 = Button(root, text='Enter Zip', command=zipcode, font=('Helvetica', '12', 'bold'), bg="#537188", fg=button_text_color)
btn1.grid(row=0, column=0, sticky='ew', padx=70, pady=10, ipadx=30, ipady=10)

btn2 = Button(root, text='Enter City', command=location, font=('Helvetica', '12', 'bold'), bg="#537188", fg=button_text_color)
btn2.grid(row=0, column=1, sticky='ew', padx=5, pady=10, ipadx=25, ipady=10)
root.bind("<Return>", handle_key)


root.mainloop()
