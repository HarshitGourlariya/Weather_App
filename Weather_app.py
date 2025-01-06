import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        latitude = float(lat_field.get())
        longitude = float(lon_field.get())
        
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=longitude, lat=latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        
        # weather
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=1c56c95e7bf3c2aa8b53555c2d16c9ff"
        json_data = requests.get(api).json()
        
        if json_data.get('cod') != 200:
            messagebox.showerror("Weather App", "Invalid Entry")
            return
        
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        
        t.config(text=(temp, "°C"))
        c.config(text=(condition, "|", "FEELS LIKE", temp, "°C"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App", "An error occurred")

# search box
Search_image = PhotoImage(file="D:\\Downloads\\search.png.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

lat_field = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
lat_field.place(x=90, y=40)
lat_field.focus()

lon_field = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
lon_field.place(x=300, y=40)

Search_icon = PhotoImage(file="D:\\Downloads\\Copy of search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=550, y=34)

# logo
logo_image = PhotoImage(file="D:\Downloads\weather.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# bottom_box
Frame_image = PhotoImage(file="D:\\Downloads\\Copy of box (2).png")
Frame = Label(image=Frame_image)
Frame.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("poppins", 20))
clock.place(x=30, y=130)

# label
label1 = Label(root, text="Wind", font=("poppins", 15, "bold"), fg="White", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="Humidity", font=("poppins", 15, "bold"), fg="White", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="Description", font=("poppins", 15, "bold"), fg="White", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="Pressure", font=("poppins", 15, "bold"), fg="White", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("aria", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()