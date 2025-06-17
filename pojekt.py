from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os
import random

mixer.init()

def pusti(ime_pesme: StringVar, songs_list: Listbox, status: StringVar):
    ime_pesme.set(songs_list.get(ACTIVE))
    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()
    status.set(f"▶️ {songs_list.get(ACTIVE)}")

def zaustavi(status: StringVar):
    mixer.music.stop()
    status.set("⏹️ Zaustavljeno")

def load(listbox):
    directory = filedialog.askdirectory(title='Izaberi folder')
    if directory:
        os.chdir(directory)
        tracks = [track for track in os.listdir() if track.endswith('.mp3')]
        listbox.delete(0, END)
        for track in tracks:
            listbox.insert(END, track)

def pauza(status: StringVar):
    mixer.music.pause()
    status.set("⏸️ Pauzirano")

def resume(status: StringVar):
    mixer.music.unpause()
    status.set("▶️ Nastavljeno")

def preskoci(status: StringVar, songs_list: Listbox):
    sadasnji_indeks = songs_list.curselection()
    if sadasnji_indeks:
        next_index = (sadasnji_indeks[0] + 1) % songs_list.size()
        ime_pesme.set(songs_list.get(next_index))
        mixer.music.load(songs_list.get(next_index))
        mixer.music.play()
        status.set(f"▶️ {songs_list.get(next_index)}")

def prethodna(status: StringVar, songs_list: Listbox):
    sadasnji_indeks = songs_list.curselection()
    if sadasnji_indeks:
        prev_index = (sadasnji_indeks[0] - 1) % songs_list.size()
        ime_pesme.set(songs_list.get(prev_index))
        mixer.music.load(songs_list.get(prev_index))
        mixer.music.play()
        status.set(f"▶️ {songs_list.get(prev_index)}")

def shuffle(ime_pesme: StringVar, songs_list: Listbox, status: StringVar):
    pesme = list(songs_list.get(0, END))
    if pesme:
        random_song = random.choice(pesme)
        ime_pesme.set(random_song)
        mixer.music.load(random_song)
        mixer.music.play()
        status.set(f"🔀 {random_song}")
    else:
        status.set("⚠️ Lista je prazna")

root = Tk()
root.geometry('500x500')
root.title('Mlan plejer')
root.configure(bg='#1e1e1e')
root.resizable(False, False)

ime_pesme = StringVar(root, value='♪ Ništa nije odabrano ♪')
status_pesme = StringVar(root, value='🔈 Spremno')

Label(root, text="🎵 MP3 Player", bg='#1e1e1e', fg='white', font=("Arial", 16, "bold")).pack(pady=10)

playlist = Listbox(root, font=('Courier New', 10), selectbackground='#2ECC71', bg='#2c3e50', fg='white', height=8)
playlist.pack(padx=20, pady=5, fill=X)

Button(root, text='📂 Učitaj folder', bg='#34495e', fg='white', command=lambda: load(playlist)).pack(pady=5)

Label(root, textvariable=ime_pesme, bg='#1e1e1e', fg='#f1c40f', font=("Arial", 10, "italic")).pack(pady=10)

controls_frame = Frame(root, bg='#1e1e1e')
controls_frame.pack(pady=10)

Button(controls_frame, text='⏮️', width=5, command=lambda: prethodna(status_pesme, playlist)).grid(row=0, column=0, padx=3)
Button(controls_frame, text='▶️', width=5, command=lambda: pusti(ime_pesme, playlist, status_pesme)).grid(row=0, column=1, padx=3)
Button(controls_frame, text='⏸️', width=5, command=lambda: pauza(status_pesme)).grid(row=0, column=2, padx=3)
Button(controls_frame, text='⏹️', width=5, command=lambda: zaustavi(status_pesme)).grid(row=0, column=3, padx=3)
Button(controls_frame, text='⏭️', width=5, command=lambda: preskoci(status_pesme, playlist)).grid(row=0, column=4, padx=3)
Button(controls_frame, text='🔀', width=5, command=lambda: shuffle(ime_pesme, playlist, status_pesme)).grid(row=0, column=5, padx=3)
Button(controls_frame, text='🔁', width=5, command=lambda: resume(status_pesme)).grid(row=0, column=6, padx=3)

Label(root, textvariable=status_pesme, bg='#34495e', fg='white', font=('Arial', 9), anchor='w').pack(fill=X, side=BOTTOM)

root.mainloop()
