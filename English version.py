import tkinter as tk
from tkinter import filedialog
import pygame

key_sound_mapping = {}

def select_sound_file(key):
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        key_sound_mapping[key] = file_path
        print(f"Key '{key}'The sound for has been saved")

def play_sound(event):
    key = event.char.upper()
    file_path = key_sound_mapping.get(key)
    if file_path:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

# 키보드 UI 구성
root = tk.Tk()
root.title("UI")
root.geometry("800x400")

def handle_double_click(event):
    key = event.widget["text"]
    select_sound_file(key)

# 키보드 자판 버튼 생성
button_q = tk.Button(root, text="Q")
button_q.place(x=50, y=100, width=50, height=50)
button_q.bind("<Double-Button-1>", handle_double_click)

button_w = tk.Button(root, text="W")
button_w.place(x=100, y=100, width=50, height=50)
button_w.bind("<Double-Button-1>", handle_double_click)

button_e = tk.Button(root, text="E")
button_e.place(x=150, y=100, width=50, height=50)
button_e.bind("<Double-Button-1>", handle_double_click)

button_r = tk.Button(root, text="R")
button_r.place(x=200, y=100, width=50, height=50)
button_r.bind("<Double-Button-1>", handle_double_click)

root.bind("<Key>", play_sound)

root.mainloop()
