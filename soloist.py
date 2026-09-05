import os
import subprocess
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
