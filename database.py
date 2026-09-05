import sqlite3

connection = sqlite3.connect("spotify.db")
cursor = connection.cursor()

def get_data(uid):
	cursor.execute("""
		SELECT albums.album, albums.artist, albums.api_ID
		FROM tags
		JOIN albums ON tags.album_id = albums.id
		WHERE tags.uid = ?
	""", (uid,))

	result = cursor.fetchone()
