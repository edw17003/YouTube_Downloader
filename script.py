import pytube
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# 'root' is the name by which I will refer to the window
root = tk.Tk()

# setting properties of the window
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Downloader")
root.config(background="#03001c")

# 'videoLink' will later hold the URL that the user enters
videoLink = StringVar()
downloadPath = StringVar()

# holds the application interface
def UI():
    # tkinter element for plain text
    label = tk.Label(
        root, 
        text="YouTube Downloader", 
        font=('Arial', 18),
        bg="#03001c",
        fg="#ffffff")
    # pack is used for positioning elements on the screen
    label.pack(
        padx=10, 
        pady=10)
    
    # Defines a new frame that we can use for positioning elements relative to each other
    URLFrame = Frame(
        root, 
        bg="#03001c")
    URLFrame.pack(side=TOP)
    
    label = tk.Label(
        URLFrame, 
        text="URL: ", 
        font=('Arial', 14),
        bg="#03001c",
        fg="#6E85B2",)
    label.pack(
        side=LEFT,
        fill=X)
    
    # tkinter element for single line text inputs
    textbox = tk.Entry(
        URLFrame, 
        font=('Arial', 14), 
        textvariable=videoLink, # assigns the users input to our 'videoLink' variable
        width=37,
        bg="#ffffff",
        fg="black")
    textbox.pack(pady=20, side=LEFT)
    
    browseFrame = Frame(
        root, 
        bg="#03001c")
    browseFrame.pack(side=TOP)
    
    label = tk.Label(
        browseFrame, 
        text="Location: ", 
        font=('Arial', 14),
        bg="#03001c",
        fg="#6E85B2",)
    label.pack(
        side=LEFT)
    
    textbox = tk.Entry(
        browseFrame, 
        font=('Arial', 14), 
        textvariable=downloadPath,
        width=26,
        bg="#060036",
        fg="#ffffff")
    textbox.pack(pady=20, side=LEFT)
    
    button = tk.Button(
        browseFrame, 
        text="Browse", 
        font=('Arial', 10), 
        command=Browse,)
    button.pack(
        padx=10, 
        pady=10,
        side=LEFT)
    
    button = tk.Button(
        root, 
        text="Video", 
        font=('Arial', 16), 
        command=DownloadVideo, # runs the DownloadVideo function when button is clicked
        bg="#5C527F",
        fg="#ffffff",
        pady=7,
        padx=40)
    button.pack(
        side=LEFT, 
        expand=TRUE, 
        )
    
    button = tk.Button(
        root, 
        text="Audio", 
        font=('Arial', 16),
        command=DownloadAudio,
        bg="#5C527F",
        fg="#ffffff",
        pady=7,
        padx=40,)
    button.pack(
        side=LEFT, 
        expand=TRUE, 
        )

def Browse():
    downloadDirectory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video"
    )
    downloadPath.set(downloadDirectory)

def DownloadVideo():
    location = downloadPath.get()
    URL = videoLink.get()
    yt = pytube.YouTube(URL)
    yt.streams.get_highest_resolution().download(location)
    messagebox.showinfo("Success!", URL)
    
def DownloadAudio():
    location = downloadPath.get()
    URL = videoLink.get()
    yt = pytube.YouTube(URL)
    yt.streams.get_audio_only().download(location)
    messagebox.showinfo("Success!", URL)
    
UI() 
root.mainloop() # Necessary to keep the application running each frame