import os
import spotipy
import subprocess
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from collections import Counter

# Load environment variables from .env file
load_dotenv()

# Set up authentication
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# Fetch recently played tracks
results = sp.current_user_recently_played(limit=50)

# Process the data
song_counts = Counter()
genres = Counter()

for item in results['items']:
    track = item['track']
    song_name = track['name']
    artist_name = track['artists'][0]['name']
    
    song_counts[f"{song_name} - {artist_name}"] += 1

    # Get genres
    artist_id = track['artists'][0]['id']
    artist_info = sp.artist(artist_id)
    for genre in artist_info['genres']:
        genres[genre] += 1

# Most played song
most_played = song_counts.most_common(1)[0] if song_counts else ("None", 0)

# Most common genre
most_common_genre = genres.most_common(1)[0] if genres else ("Unknown", 0)

# Create summary text
summary = f"""
Weekly Spotify Summary:

🎵 Most Played Song: {most_played[0]} ({most_played[1]} times)
🎧 Total Songs Played: {sum(song_counts.values())}
🎼 Main Genre: {most_common_genre[0]}

📊 All Songs Played:
""" + "\n".join([f"{song} - {count} times" for song, count in song_counts.items()])

print(summary)
subprocess.run(["python3", "send_email.py"])
