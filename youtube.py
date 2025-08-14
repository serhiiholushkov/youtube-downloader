from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url: str, save_path: str):
    try:
        yt = YouTube(url)

        # A YouTube progressive stream refers to a method
        # where the entire video file is downloaded from the server and then played by the user's device
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        video = streams.get_highest_resolution()
        video.download(output_path=save_path)
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"An error occurred: {e}")


def open_file_dialog():
    save_path = filedialog.askdirectory()
    if save_path:
        print(f"Selected save path: {save_path}")

    return save_path


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    video_url = input("Enter the YouTube video URL: ")
    save_directory = open_file_dialog()

    if save_directory:
        print("Starting download...")
        download_video(video_url, save_directory)
    else:
        print("No directory selected.")
