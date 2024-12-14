# import tkinter as tk
# import yt_dlp

# def download_video(quality):
#     try:
#         link = entry.get()

#         # Set options for downloading based on the quality chosen
#         ydl_opts = {
#             'format': 'bestvideo+bestaudio/best' if quality == 'high' else
#                       'worstvideo+worstaudio/worst' if quality == 'low' else
#                       'bestaudio/best',
#             'outtmpl': '%(title)s.%(ext)s',  # Saves the file in the current directory with video title as filename
#         }

#         # Create a yt-dlp object and download the video
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([link])

#         status_label.config(text="Download completed!", fg="green")

#     except Exception as e:
#         status_label.config(text=f"Error: {str(e)}", fg="red")


# # Create the main window
# root = tk.Tk()
# root.title("YouTube Downloader")

# # Create the input field for the link
# tk.Label(root, text="Paste Link Here:").pack()

# entry = tk.Entry(root, width=50)
# entry.pack(pady=10)

# # Create buttons for downloading
# tk.Button(root, text="High Quality", command=lambda: download_video('high')).pack(pady=5)
# tk.Button(root, text="Low Quality", command=lambda: download_video('low')).pack(pady=5)
# tk.Button(root, text="Only Audio", command=lambda: download_video('audio')).pack(pady=5)
# tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

# # Status label
# status_label = tk.Label(root, text="")
# status_label.pack(pady=10)

# # Run the GUI loop
# root.mainloop()







#-------------------------------"   Version 1.2   cm open after file downloaded   "-----------------------------------------






# import tkinter as tk
# import yt_dlp
# import os
# import subprocess
# import platform

# def download_video(quality):
#     try:
#         link = entry.get()

#         # Set options for downloading based on the quality chosen
#         if quality == 'high':
#             ydl_opts = {
#                 'format': 'best',  # Best combined video and audio format
#                 'outtmpl': '%(title)s.%(ext)s',  # Save with video title as the filename
#             }
#         elif quality == 'low':
#             ydl_opts = {
#                 'format': 'worstvideo+worstaudio/best',  # Worst available video and audio, fallback to best if not available
#                 'outtmpl': '%(title)s.%(ext)s',
#             }
#         elif quality == 'audio':
#             ydl_opts = {
#                 'format': 'bestaudio/best',  # Only download the best audio
#                 'outtmpl': '%(title)s.%(ext)s',
#             }
#         else:
#             status_label.config(text="Invalid quality option", fg="red")
#             return

#         # Create a yt-dlp object and download the video
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([link])

#         status_label.config(text="Download completed!", fg="green")

#         # Open the downloaded file automatically after the download
#         open_downloaded_file()

#     except Exception as e:
#         status_label.config(text=f"Error: {str(e)}", fg="red")


# def open_downloaded_file():
#     # Get the file name of the downloaded file
#     downloaded_file = f"{yt_dlp.YoutubeDL().prepare_filename(yt_dlp.YoutubeDL().extract_info(entry.get(), download=False))}"

#     # Get the file extension (audio/video)
#     file_extension = downloaded_file.split('.')[-1]

#     # Open the file after download, depending on the operating system
#     if platform.system() == 'Windows':
#         subprocess.run(['start', downloaded_file], shell=True)
#     elif platform.system() == 'Darwin':  # macOS
#         subprocess.run(['open', downloaded_file])
#     else:  # Linux or other OS
#         subprocess.run(['xdg-open', downloaded_file])


# # Create the main window
# root = tk.Tk()
# root.title("YouTube Downloader")

# # Create the input field for the link
# tk.Label(root, text="Paste Link Here:").pack()

# entry = tk.Entry(root, width=50)
# entry.pack(pady=10)

# # Create buttons for downloading
# tk.Button(root, text="High Quality", command=lambda: download_video('high')).pack(pady=5)
# tk.Button(root, text="Low Quality", command=lambda: download_video('low')).pack(pady=5)
# tk.Button(root, text="Only Audio", command=lambda: download_video('audio')).pack(pady=5)
# tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

# # Status label
# status_label = tk.Label(root, text="")
# status_label.pack(pady=10)

# # Run the GUI loop
# root.mainloop()




#--------------------------------------------------"   version 1.3 final good version   "---------------------------


# #link to test :         https://www.youtube.com/shorts/eA7s5cvibrk

# import tkinter as tk
# import yt_dlp
# import os
# import subprocess
# import platform

# def download_video(quality):
#     try:
#         link = entry.get()

#         # Set options for downloading based on the quality chosen
#         if quality == 'high':
#             ydl_opts = {
#                 'format': 'best',  # Best combined video and audio format
#                 'outtmpl': '%(title)s.%(ext)s',  # Save with video title as the filename
#             }
#         elif quality == 'low':
#             ydl_opts = {
#                 'format': 'worstvideo+worstaudio/best',  # Worst available video and audio, fallback to best if not available
#                 'outtmpl': '%(title)s.%(ext)s',
#             }
#         elif quality == 'audio':
#             ydl_opts = {
#                 'format': 'bestaudio/best',  # Only download the best audio
#                 'outtmpl': '%(title)s.%(ext)s',
#             }
#         else:
#             status_label.config(text="Invalid quality option", fg="red")
#             return

#         # Create a yt-dlp object and download the video
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([link])

#         status_label.config(text="Download completed! you can find your file in C:\\Users\\mahdy", fg="green")

#         # Open the downloaded file automatically after the download
#         # open_downloaded_file()

#     except Exception as e:
#         status_label.config(text=f"Error: {str(e)}", fg="red")


# # def open_downloaded_file():
# #     # Get the file name of the downloaded file
# #     downloaded_file = f"{yt_dlp.YoutubeDL().prepare_filename(yt_dlp.YoutubeDL().extract_info(entry.get(), download=False))}"

# #     # Check the system and open the file with the appropriate default application
# #     if platform.system() == 'Windows':
# #         # Open the file using the default application for the file type (no command prompt)
# #         os.startfile(downloaded_file)  # This should launch the file with its default program
# #     elif platform.system() == 'Darwin':  # macOS
# #         subprocess.run(['open', downloaded_file])
# #     else:  # Linux or other OS
# #         subprocess.run(['xdg-open', downloaded_file])


# # Create the main window
# root = tk.Tk()
# root.title("YouTube Downloader")

# # Create the input field for the link
# tk.Label(root, text="Paste Link Here:").pack()

# entry = tk.Entry(root, width=50)
# entry.pack(pady=10)

# # Create buttons for downloading
# tk.Button(root, text="High Quality", command=lambda: download_video('high')).pack(pady=5)
# tk.Button(root, text="Low Quality", command=lambda: download_video('low')).pack(pady=5)
# tk.Button(root, text="Only Audio", command=lambda: download_video('audio')).pack(pady=5)
# tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

# # Status label
# status_label = tk.Label(root, text="")
# status_label.pack(pady=10)

# # Run the GUI loop
# root.mainloop()



#-----------------------------------------------------------------



# import tkinter as tk
# import yt_dlp
# import os
# import subprocess
# import platform

# def download_video(quality):
#     try:
#         link = entry.get()

#         # Set options for downloading based on the quality chosen
#         if quality == 'high':
#             ydl_opts = {
#                 'format': 'best',  # Best combined video and audio format
#                 'outtmpl': '%(title)s-%(id)s.%(ext)s',  # Add the video ID to the filename for uniqueness
#             }
#         elif quality == 'low':
#             ydl_opts = {
#                 'format': 'worstvideo+worstaudio/best',  # Worst available video and audio, fallback to best if not available
#                 'outtmpl': '%(title)s-%(id)s.%(ext)s',
#             }
#         elif quality == 'audio':
#             ydl_opts = {
#                 'format': 'bestaudio/best',  # Only download the best audio
#                 'outtmpl': '%(title)s-%(id)s.%(ext)s',
#             }
#         else:
#             status_label.config(text="Invalid quality option", fg="red")
#             return

#         # Create a yt-dlp object and download the video
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([link])

#         status_label.config(text="Download completed!", fg="green")

#         # Open the downloaded file automatically after the download
#         open_downloaded_file()

#     except Exception as e:
#         status_label.config(text=f"Error: {str(e)}", fg="red")


# def open_downloaded_file():
#     # Get the file name of the downloaded file
#     downloaded_file = f"{yt_dlp.YoutubeDL().prepare_filename(yt_dlp.YoutubeDL().extract_info(entry.get(), download=False))}"

#     # Check the system and open the file with the appropriate default application
#     if platform.system() == 'Windows':
#         # Open the file using the default application for the file type (no command prompt)
#         os.startfile(downloaded_file)  # This should launch the file with its default program
#     elif platform.system() == 'Darwin':  # macOS
#         subprocess.run(['open', downloaded_file])
#     else:  # Linux or other OS
#         subprocess.run(['xdg-open', downloaded_file])


# # Create the main window
# root = tk.Tk()
# root.title("YouTube Downloader")

# # Create the input field for the link
# tk.Label(root, text="Paste Link Here:").pack()

# entry = tk.Entry(root, width=50)
# entry.pack(pady=10)

# # Create buttons for downloading
# tk.Button(root, text="High Quality", command=lambda: download_video('high')).pack(pady=5)
# tk.Button(root, text="Low Quality", command=lambda: download_video('low')).pack(pady=5)
# tk.Button(root, text="Only Audio", command=lambda: download_video('audio')).pack(pady=5)
# tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

# # Status label
# status_label = tk.Label(root, text="")
# status_label.pack(pady=10)

# # Run the GUI loop
# root.mainloop()














#---------------------------"   version 1.4 final good version   "---------------------------

# #link to test :         https://www.youtube.com/shorts/eA7s5cvibrk


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
title_label = tk.Label(root, text="YouTube Downloader POWERD BY @MahdyDaoud", font=("Helvetica", 16, "bold"), fg="white", bg="#2c3e50")
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
