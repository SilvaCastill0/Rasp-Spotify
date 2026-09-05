from RFID import read_rfid
from database import find_album
from soloist import play, start

def main():
	start()
	uid = read_rfid()
	spotify_id = find_album(uid)
	play(spotify_id)

if __name__ == '__main__':
	main()
