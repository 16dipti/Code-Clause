import tkinter as tk
import requests
from tkinter import messagebox

api_key = "146a316efdmshe042b07c6392d43p1a84b8jsnd7aee4adc615"
api_host = "url-shortener23.p.rapidapi.com"
url = "https://url-shortener23.p.rapidapi.com/shorten"

def shorten_url():
    window.clipboard_clear()
    url_input = entry_url.get()
    
    
    data = {"url": url_input}
    headers = {"X-RapidAPI-Key": api_key, "X-RapidAPI-Host": api_host}
    
    try:
        response = requests.post(url, json=data, headers=headers)
        short_url = response.json()["short_url"]
        label_result.config(text=f"Shortened URL: {short_url}")
        window.clipboard_append(short_url)
        messagebox.showinfo(message="Copied to Clipboard")
    except Exception as e:
        label_result.config(text=f"An error occurred: {str(e)}")

# GUI Setup
window = tk.Tk()
window.title("URL Shortener")
window.geometry("500x300")
window.configure(bg='#bddbed')

label_title = tk.Label(window, text="URL SHORTNER", font=('Times New Roman', 30, 'bold'), highlightthickness=0, bd=0, bg='#bddbed')
label_title.pack(pady=10)

label_url = tk.Label(window, text="Enter URL:" ,font=('Times New Roman', 13, 'bold'), bg='#bddbed')
label_url.pack(pady=10)

entry_url = tk.Entry(window, width=40)
entry_url.pack(pady=10)

btn_shorten = tk.Button(window, text="Shorten URL",font=('Times New Roman', 13, 'bold'), command=shorten_url)
btn_shorten.pack(pady=10)

label_result = tk.Label(window, text="", font=('Times New Roman', 13, 'bold'),  bg='#bddbed')
label_result.pack(pady=10)

window.mainloop()
