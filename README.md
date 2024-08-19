# youtube_page_downloader

This extracts video links and video names from multiple youtube channel's video page.

## Installation

```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
clear
python videos.py
```
# 1) Extract Page

## Command

```
python youtube_extractor.py <YouTube_Channel_URL>
```


Also increase this number based on your internet speed. 1 should be enough for most people but if you see the page not completely scrolling to the bottom change it to 2.
```
internet_speed = 2
```

You can keep your terminal open on the side to see how much time is remaining for the scroll as the scroll time is dependent on the number of videos on that youtube channel.


A new file will be created when the links are extracted. You can copy paste it directly in database or excel and it will retain it's structure since it has a tab character in between then.

# 2) Download Videos

Based on the extracted information from the YouTube page, the script will download and store the MP4 files in the ./videos directory.

## Command

```
python download_videos.py 
```
