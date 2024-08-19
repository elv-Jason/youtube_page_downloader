import os
import yt_dlp
import re

def sanitize_title(title):
    return re.sub(r'[\\/:"*?<>|]+', '_', title)

text_file_path = './video_info.txt'
destination_folder = './videos'

os.makedirs(destination_folder, exist_ok=True)

with open(text_file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    if ' | Movieclips: ' in line:
        title, url = line.split(' | Movieclips: ')
        url = url.strip()
        title = sanitize_title(title.strip())
        
        ydl_opts = {
            'outtmpl': os.path.join(destination_folder, f'{title}.%(ext)s'),
            'format': 'best',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

print("Download completed.")



