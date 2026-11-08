import re
import requests

TARGET_URL = "https://s1.itcnbd.live/Star.Sports.1.HD/"

def fetch_new_link():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(TARGET_URL, headers=headers)
        match = re.search(r'https?://[^\s<>"]+?index\.m3u8[^\s<>"]*', response.text)
        if match:
            return match.group(0)
    except Exception as e:
        print(f"Error: {e}")
    return None

def update_m3u(stream_link):
    if not stream_link:
        print("Failed to fetch new link.")
        return
    m3u_content = f"""#EXTM3U
#EXTINF:-1 group-title="Sports",Star Sports 1 HD
{stream_link}
"""
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("playlist.m3u updated successfully!")

if __name__ == "__main__":
    new_link = fetch_new_link()
    update_m3u(new_link)