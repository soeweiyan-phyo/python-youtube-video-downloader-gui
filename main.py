import tkinter
import customtkinter
from pytube import YouTube

# To download video from YouTube
def start_download():
  try:
    yt_link = link.get()
    ytObject = YouTube(yt_link)
    video = ytObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    title.configure(text=ytObject.title, text_color="black")
    finish_label.configure(text="", text_color="black")
    
    video.download()
    finish_label.configure(text="Download Completed")

  except:
    finish_label.configure(text="Download Error", text_color="red")

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

# Run App 
# (Have to loop, otherwise app closes immediately)
app.mainloop()