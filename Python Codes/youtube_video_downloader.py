# Youtube Video Downloader

# This script can download any youtube video in the highest resolution from youtube.
# You have to replace "https://www.youtube.com/watch?v=example" with the url of any video/short from youtube.
# You also have to replace "/path/to/download" with your download distination. 
# If any error occured then it will be print in the terminal.
# If there is any problem in this code, then let me know.
# Enjoy downloading videos of your favourite anime, cartoon, movie, show, etc. in the highest resolution in free!

from pytube import YouTube

def download_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path)
        print(f"Video downloaded successfully: {video_stream.title}")
    except Exception as e:
        print(f"An error occurred: {e}")

download_video("https://youtu.be/Y0NK7I9Krio", r"F:\Personal Files\Naitik\Coding\Projects\Project-1 (Python)\YouTube Downloader")