import argparse
from app.location_service import get_coordinates
from app.youtube import fetch_videos
from app.export import export_json, export_md, export_pdf

parser = argparse.ArgumentParser()
parser.add_argument("location")
parser.add_argument("--format", choices=["json", "md", "pdf"], default="json")

args = parser.parse_args()

lat, lon = get_coordinates(args.location)
videos = fetch_videos(lat, lon)

if args.format == "json":
    export_json(videos)
elif args.format == "md":
    export_md(videos)
elif args.format == "pdf":
    export_pdf(videos)

print("Export complete.")
