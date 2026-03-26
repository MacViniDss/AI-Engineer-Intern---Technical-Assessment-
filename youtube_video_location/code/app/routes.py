# app/routes.py
from flask import Blueprint, request, jsonify
from app.location_service import get_coordinates
from app.youtube import fetch_videos

bp = Blueprint("main", __name__)

@bp.route("/search", methods=["GET"])
def search():
    location = request.args.get("location")

    lat, lon = get_coordinates(location)
    videos = fetch_videos(lat, lon)

    return jsonify(videos)