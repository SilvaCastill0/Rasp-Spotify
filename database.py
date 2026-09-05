import sqlite3

def find_album(uid):
	connection = sqlite3.connect("spotify.db")
	cursor = connection.cursor()

	cursor.execute("""
		SELECT albums.album, albums.artist, albums.api_ID
		FROM tags
		JOIN albums ON tags.album_id = albums.id
		WHERE tags.uid = ?
	""", (uid,))

	result = cursor.fetchone()
	if result:
		album, artist, spotify_id = result
		return spotify_id
	else:
		print("Tag not found.")

	connection.close()
