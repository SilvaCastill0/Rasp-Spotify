import os
import spotipy
from dotenv import load_dotenv 
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
	client_id=os.getenv("SPOTIFY_CLIENT_ID"),
	client_secret=os.getenv("SPOTOFY_CLIENT_SECRET"),
	redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope="user-read-playback-state"
    )
)

user = sp.current_user()

print("Successfully connected to Spotify!")
print("Logged in as:", user["display_name"])
