import requests
from tkinter import *

def check():
    get_text = text.get("1.0",END)
    url = "https://plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com/plagiarism"
    payload = {
	"text": get_text,
	"language": "en",
	"includeCitations": False,
	"scrapeSources": False
    }
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "146a316efdmshe042b07c6392d43p1a84b8jsnd7aee4adc615",
	"X-RapidAPI-Host": "plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com"
    }   
    response = requests.post(url, json=payload, headers=headers)
    plagarism = response.json()['percentPlagiarism']
    percent_label.config(text=f"{plagarism}% of plagarism found", font=('Time new Roman', 15, 'bold'))

window = Tk()
window.title("Plagarism checker")
window.geometry("600x400")
window.configure(bg='#ecc0c9')

plagarism_label = Label(window, text="Plagarism checker", font=('Time new Roman', 20, 'bold'), bg='#ecc0c9')
plagarism_label.pack()

enter_label = Label(window, text="Enter your text below", font=('Time new Roman', 15, 'italic'), bg='#ecc0c9')
enter_label.pack(pady=10)


text = Text(window, width=60, height=10)
text.place(x=50, y=80)

check_button = Button(text="Check your plagarism", command=check, font=('Time new Roman', 15, 'italic'))
check_button.place(x=200, y=250)

percent_label = Label(window, text="", font=('Time new Roman', 15, 'bold'), bg='#ecc0c9')
percent_label.place(x=200, y=320)


window.mainloop()