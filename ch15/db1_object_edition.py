import sqlite3

from sqlite3 import Connection, Cursor


class MusicDB:
    def __init__(self, db_path: str = "music.sqlite"):
        self._conn: Connection = sqlite3.connect(db_path)
        self._cur: Cursor = self._conn.cursor()

    def create_tracks_table(self) -> None:
        self._cur.execute("DROP TABLE IF EXISTS Tracks")
        self._cur.execute("CREATE TABLE Tracks (title TEXT, plays INTEGER)")
        self._conn.commit()

    def insert_track(self, title: str, plays: int) -> None:
        self._cur.execute(
            "INSERT INTO Tracks (title, plays) VALUES (?, ?)", (title, plays)
        )
        self._conn.commit

    def fetch_all_tracks(self) -> list[tuple]:
        return self._cur.execute("SELECT title, plays FROM Tracks").fetchall()

    def remove_less_played(self) -> None:
        self._cur.execute("DELETE FROM Tracks WHERE plays < 100")
        self._conn.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self._conn.commit()
        self._conn.close()


if __name__ == "__main__":
    with MusicDB() as music_db:
        # music_db.create_tracks_table()
        music_db.insert_track("Baile inolvidable", 100)
        music_db.insert_track("Legendarios", 126)
        music_db.insert_track("A Dios le pido", 86)

        for title, plays in music_db.fetch_all_tracks():
            print(title, plays)

        music_db.remove_less_played()

        for title, plays in music_db.fetch_all_tracks():
            print(title, plays)
