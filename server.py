from flask import Flask
from soloist import *

app = Flask(__name__)

@app.route("/pause")
def pause_route():
	pause()
	return "paused"
	
@app.route("/resume")
def resume_route():
	resume()
	return "resume"
	

@app.route("/next")
def next_route():
	next_track()
	return "next song"
	
@app.route("/prev")
def prev_route():
	prev_track()
	return "prev song"
	
	
@app.route("/volume")
def volume_route():
	set_volume("67")
	return "volume set"
	
@app.route("/seek")
def seek_route():
	seek("10000")
	return "found"

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000)
