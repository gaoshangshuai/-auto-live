import time
from datetime import datetime

def generate_url():
    t = int(time.time()) + 3 * 60 * 60
    url = f"https://tv.pull.hebtv.com/jishi/weishipindao.m3u8?t={t}&k=7ce65bcf054b7b595ab624c5aa1a8a6b"
    return url

def update_m3u():
    url = generate_url()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"""#EXTM3U
#EXTINF:-1 tvg-name="河北卫视" group-title="卫视",更新时间：{now}
{url}
"""
    with open("channels.m3u", "w", encoding="utf-8") as f:
        f.write(content)

update_m3u()
