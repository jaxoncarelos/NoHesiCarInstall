import os
import requests
import re
import tkinter as tk
from tkinter import filedialog

carText = input("Enter the prompt ACM gave you for cars you need: ")

car_list = re.findall(r'“(.*?)”', carText)

root = tk.Tk()
root.withdraw()

cars_dir = filedialog.askdirectory(title="Select the cars folder")


for car in car_list:
    url = f"https://cdn.nohesi.gg/cars/{car}.7z"
    r = requests.get(url, allow_redirects=True)

    file_path = os.path.join(cars_dir, f"{car}.7z")
  
    with open(file_path, 'wb') as file:
        file.write(r.content)

    print(file_path)