from tkinter import filedialog
from tkinter import *
import pygame
import os

window = Tk()
window.title("Music player")
window.geometry("500x300")

pygame.mixer.init()

songs = []
current_song = ""
paused = False


menu = Menu(window)
window.config(menu=menu)

def load_file():
    global current_song
    window.__dir__ = filedialog.askdirectory()
    for song in os.listdir(window.__dir__):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)
    for song in songs:
        songlist.insert("end", song)
    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]
    
def play_music():
    global current_song, paused
    if not paused:
        pygame.mixer.music.load(os.path.join(window.__dir__, current_song)) 
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song, paused
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global current_song, paused
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


organize_menu = Menu(menu, tearoff=False)
organize_menu.add_command(label='Select Folder', command=load_file)
menu.add_cascade(label='Organise', menu=organize_menu)

songlist = Listbox(window, bg="black", fg="white", width=100, height=15)
songlist.pack()

play_btn_image = PhotoImage(file="images/play-button.png")
back_btn_image = PhotoImage(file="images/back.png")
next_btn_image = PhotoImage(file="images/next.png")
pause_btn_image = PhotoImage(file="images/pause.png")

control_frame = Frame(window)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_music)
back_btn = Button(control_frame, image=back_btn_image, borderwidth=0, command=prev_music)
next_btn= Button(control_frame, image=next_btn_image, borderwidth=0, command=next_music)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
back_btn.grid(row=0, column=0, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)

window.mainloop()

