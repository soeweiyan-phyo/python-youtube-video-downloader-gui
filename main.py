import tkinter
import customtkinter
from pytube import YouTube

# Download video from YouTube
def start_download():
  try:
    # Get link from link UI input
    yt_link = link.get()
    # Create YouTube object
    ytObject = YouTube(yt_link, on_progress_callback=on_progress)
    # Get video file from the YouTube object
    video = ytObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # Change title to video title
    title.configure(text=ytObject.title, text_color="black")
    finish_label.configure(text="", text_color="black")
    
    # Download video
    video.download()
    finish_label.configure(text="Download Completed")

  except:
    finish_label.configure(text="Download Error", text_color="red")

# Progress calculation callback function for YouTube object
def on_progress(stream, chunk, bytes_remaining):
  # Calculate completion percentage
  total_size = stream.filesize
  bytes_downloaded = total_size - bytes_remaining
  completion_percent = bytes_downloaded / total_size * 100
  percent = str(int(completion_percent))

  # Update progress percentage UI
  progress_percent.configure(text=percent + "%")
  progress_percent.update() # Update on every interation
  
  # Update progress bar UI
  progress_bar.set(float(completion_percent) / 100)

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10) # Show the UI element

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

# Progress percentage
progress_percent = customtkinter.CTkLabel(app, text="0%")
progress_percent.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

# Run App 
# (Have to loop, otherwise app closes immediately)
app.mainloop()