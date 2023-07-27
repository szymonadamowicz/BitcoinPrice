import requests
from tkinter import *
from datetime import datetime


def track_bitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    return response


def window(response):
    canvas = Tk()
    canvas.geometry("400x500")
    canvas.title("Bitcoin tracker")
    canvas.config(bg="black")
    label = Label(canvas, text="Bitcoin Price", font=("Papyrus", 24, "bold"), bg="black", fg="white")
    label.pack(pady=20)
    LabelPrice = Label(canvas, font=("Papyrus", 20, "bold"), bg="black", fg="white")
    LabelPrice.pack(pady=20)
    LabelTime = Label(canvas, font=("Papyrus", 20, "bold"), bg="black", fg="white")
    LabelTime.pack(pady=20)

    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    LabelPrice.config(text=str(price) + " $")
    LabelTime.config(text="Updated at: " + time)
    canvas.mainloop()

window(track_bitcoin())