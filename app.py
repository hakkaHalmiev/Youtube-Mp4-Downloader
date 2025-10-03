from pytubefix import YouTube
from pytubefix.cli import on_progress

# Add New Libraries to operate virtual program

import os
import tkinter as tk
from tkinter import filedialog,messagebox
#-----------------------------------------------------------------------------------------------------------------------

#url = input("Enter YouTube URL: ")
#yt = YouTube (url, on_progress_callback=on_progress)
#print(yt.title)

#ys = yt.streams.get_highest_resolution()
#print("Wait.......")
#ys.download()
#('Completed')
#-----------------------------------------------------------------------------------------------------------------------
# Add virtual settings
#-----------------------------------------------------------------------------------------------------------------------
### Create a window

root = tk.Tk()
root.title("Youtube MP4 Downloader")
root.geometry("600x300")
root.resizable(False,False)

label = tk.Label(root, text="MP4 Downloader", font=("Arial", 20))
label.pack()

folder_path = tk.StringVar() # For path variables
#-----------------------------------------------------------------------------------------------------------------------
### Adding function to download Video
def download():
    url = url_entr.get()
    folder = folder_path.get()

    if not url or not folder:
        messagebox.showerror("Error", "Please enter valid URL or Folder")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=folder)
        messagebox.showinfo("Success", f"Downloaded:\n{yt.title}\nSaved to: {folder}")

    except Exception as e:
        messagebox.showwarning("Error", "Something went wrong.\n{str(e)}")



#-----------------------------------------------------------------------------------------------------------------------
### Function Browse Folder

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)



#-----------------------------------------------------------------------------------------------------------------------
### Label Creation

tk.Label(root, text="Youtube video url:", font=("Arial", 12)).pack(pady=10)
url_entr=tk.Entry(root,width=60)
url_entr.pack(pady=10)


tk.Label(root, text="Select Download Folder:", font=("Arial", 12)).pack(pady=10)
folder_frame=tk.Frame(root)
folder_frame.pack(pady=10)

tk.Entry(folder_frame,textvariable= folder_path, width=40,).pack(side="left", padx=5) # We can write on the program
tk.Button(folder_frame, text="Browse", command=browse_folder).pack(side="left")

#-----------------------------------------------------------------------------------------------------------------------
### Creating Button
button = tk.Button(root, text="Download", command=download)
button.pack()

root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------