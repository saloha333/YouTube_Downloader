
import tkinter as tk
from tkinter import ttk
import yt_dlp
import os
import subprocess
import platform

def download_video(quality):
    try:
        link = entry.get()

        # Set options for downloading based on the quality chosen
        if quality == 'high':
            ydl_opts = {
                'format': 'best',  # Best combined video and audio format
                'outtmpl': '%(title)s.%(ext)s',  # Save with video title as the filename
            }
        elif quality == 'low':
            ydl_opts = {
                'format': 'worstvideo+worstaudio/best',  # Worst available video and audio, fallback to best if not available
                'outtmpl': '%(title)s.%(ext)s',
            }
        elif quality == 'audio':
            ydl_opts = {
                'format': 'bestaudio/best',  # Only download the best audio
                'outtmpl': '%(title)s.%(ext)s',
            }
        else:
            status_label.config(text="Invalid quality option", fg="red")
            return

        # Create a yt-dlp object and download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        status_label.config(text="Download completed! You can find your file in C:\\Users\\mahdy.", fg="green")

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")


# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("600x500")  # Set window size
root.config(bg="#2c3e50")  # Background color

# Title label
title_label = tk.Label(root, text="YouTube Downloader", font=("Helvetica", 16, "bold"), fg="white", bg="#2c3e50")
title_label.pack(pady=20)

# Input frame
input_frame = tk.Frame(root, bg="#2c3e50")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Paste Link Here:", font=("Helvetica", 12), fg="white", bg="#2c3e50").pack()

entry = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
entry.pack(pady=5)

# Buttons frame
buttons_frame = tk.Frame(root, bg="#2c3e50")
buttons_frame.pack(pady=20)

tk.Button(buttons_frame, text="High Quality", command=lambda: download_video('high'), font=("Helvetica", 12), fg="white", bg="#3498db", width=15, height=2).pack(pady=5)
tk.Button(buttons_frame, text="Low Quality", command=lambda: download_video('low'), font=("Helvetica", 12), fg="white", bg="#e74c3c", width=15, height=2).pack(pady=5)
tk.Button(buttons_frame, text="Only Audio", command=lambda: download_video('audio'), font=("Helvetica", 12), fg="white", bg="#2ecc71", width=15, height=2).pack(pady=5)

# Exit button
tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 12), fg="white", bg="#34495e", width=15, height=2).pack(pady=20)

# Status label
status_label = tk.Label(root, text="", font=("Helvetica", 12), fg="white", bg="#2c3e50")
status_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
