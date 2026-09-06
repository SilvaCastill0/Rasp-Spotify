import os
import subprocess
import json
from dotenv import load_dotenv

load_dotenv()
secret = os.getenv("SPOTIFY_API_KEY")

def start():
	subprocess.Popen([
		"soloist",
		"-n", "Rasp-Spotify",
    		"-k", secret,
   		 "--ws", "127.0.0.1:9090"
	])

def play(id):
	uri = f"spotify:album:{id}"

	subprocess.run([
		"soloist",
		"ctl",
		"play",
		uri
	])
	
def pause():
	subprocess.run([
		"soloist",
		"ctl",
		"pause"
	])

def resume():
	subprocess.run([
		"soloist",
		"ctl",
		"play"
	])
	
def next_track():
	subprocess.run([
		"soloist",
		"ctl",
		"next"
	])
	
def prev_track():
	subprocess.run([
		"soloist",
		"ctl",
		"prev"
	])
	
def set_volume(db):
	subprocess.run([
		"soloist",
		"ctl",
		"volume",
		db
	])
	
def seek(ms):
	subprocess.run([
		"soloist",
		"ctl",
		"seek",
		ms
	])

def now_playing():
	result =  subprocess.run([
                "soloist",
                "ctl",
                "now",
		"--json"],
		capture_output=True,
		text=True
	 )
	data = json.loads(result.stdout)

	artist = data["item"]["decorations"]["creators"][0]["entity"]["decorations"]["identity"]["name"]
	state = data["status"]
	track = data["item"]["decorations"]["identity"]["name"]
	album = data["item"]["decorations"]["parent"]["entity"]["decorations"]["identity"]["name"]
	cover = data["item"]["decorations"]["visual_identity"]["cover"][2]
	position = data["position"]["position_ms"]
	duration = data["item"]["decorations"]["playback"]["duration_ms"]

	return {
		"artist": artist,
		"state": state,
		"track": track,
		"album": album,
		"cover": cover,
		"position": position,
		"duration": duration
	}

