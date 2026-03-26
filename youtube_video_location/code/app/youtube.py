import requests
from config import YOUTUBE_API_KEY

BASE_URL = "https://www.googleapis.com/youtube/v3/search"

def fetch_videos(lat, lon, radius="10km", max_results=10):
    params = {
        "key": YOUTUBE_API_KEY,
        "type": "video",
        "part": "snippet",
        "location": f"{lat},{lon}",
        "locationRadius": radius,
        "maxResults": max_results
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    videos = []
    for item in data.get("items", []):
        videos.append({
            "title": item["snippet"]["title"],
            "video_id": item["id"]["videoId"],
            "url": f"https://youtube.com/watch?v={item['id']['videoId']}"
        })

    return videos
