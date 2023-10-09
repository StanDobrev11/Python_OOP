from typing import List


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs: List['class Song'] = [] if not args else [song for song in args]

    def add_song(self, song: 'class Song') -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return f"Cannot add songs. Album is published."

        if song in self.songs:
            return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return f"Cannot remove songs. Album is published."

        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return f"Song is not in the album."

        self.songs.remove(song)
        return f"Removed song {song.name} from album {self.name}."

    def publish(self) -> str:
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self) -> str:
        album_data = '\n'.join(f"== {song.get_info()}" for song in self.songs)
        return f"Album {self.name}\n" + album_data
