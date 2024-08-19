import time
import sys
from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm

if len(sys.argv) != 2:
    print("Usage: python script_name.py <YouTube_Channel_URL>")
    sys.exit(1)

channel = sys.argv[1]
internet_speed = 2

video_info = []

def convert_video_count(count_str):
    if 'K' in count_str:
        return int(float(count_str.replace('K', '')) * 1000)
    elif 'M' in count_str:
        return int(float(count_str.replace('M', '')) * 1000000)
    else:
        return int(count_str.replace(',', ''))

driver = webdriver.Chrome()

driver.get(channel)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

total_videos_element = soup.find('span', {'dir': 'auto', 'class': 'style-scope yt-formatted-string'})

total_videos_count = convert_video_count(total_videos_element.text)
scroll_duration = internet_speed * total_videos_count / 5
print(total_videos_count, " : ", scroll_duration)

driver.execute_script('''
    var scroll = setInterval(function(){
        window.scrollBy(0, 1000);
    }, 1000);
''')

with tqdm(total=scroll_duration, unit="s", desc="Scrolling") as pbar:
    for _ in range(int(scroll_duration)):
        time.sleep(1)
        pbar.update(1)

updated_page_source = driver.page_source
soup = BeautifulSoup(updated_page_source, 'html.parser')

video_tags = soup.find_all('a', {'id': 'video-title-link', 'class': 'yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media'})

for video_tag in video_tags:
    video_title = video_tag.get('title', 'N/A')
    video_url = 'https://www.youtube.com' + video_tag.get('href', 'N/A')
    video_info.append(f"{video_title}: {video_url}")

with open('video_info.txt', 'w', encoding='utf-8') as output_file:
    for entry in video_info:
        output_file.write(entry + '\n')

print("Video information has been saved to video_info.txt")
print(f"Total videos found: {len(video_info)}")

print("Press Ctrl+C to exit")
while True:
    time.sleep(1)
