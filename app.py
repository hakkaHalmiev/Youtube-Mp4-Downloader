from pytubefix import YouTube
from pytubefix.cli import on_progress

# Add New Libraries to operate virtual program

import os
import tkinter as tk
from tkinter import filedialog,messagebox


#url = input("Enter YouTube URL: ")
#yt = YouTube (url, on_progress_callback=on_progress)
#print(yt.title)

#ys = yt.streams.get_highest_resolution()
#print("Wait.......")
#ys.download()
#('Completed')

# Add virtual settings

## Create a window

root = tk.Tk()
root.title("Youtube MP4 Downloader")
root.geometry("600x200")

label = tk.Label(root, text="MP4 Downloader", font=("Arial", 20))
label.pack()

# Adding function to download Video
def download():
    url = input("Enter URL: ")
    yt = YouTube(url, on_progress_callback=on_progress)

    ys = yt.streams.get_highest_resolution()
    ys.download()

### Creating Button
button = tk.Button(root, text="Download", command=download)
button.pack()






root.mainloop()