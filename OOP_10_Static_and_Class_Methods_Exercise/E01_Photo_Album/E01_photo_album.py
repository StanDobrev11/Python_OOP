from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        """ Creates a new instance of PhotoAlbum """
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def is_album_full(self) -> bool:
        try:
            self.photos[self.pages - 1][PhotoAlbum.PHOTOS_PER_PAGE - 1]
            return True
        except IndexError:
            return False

    def last_filled_photo(self, label):
        for row in range(len(self.photos)):
            for col in range(len(self.photos[row])):
                if self.photos[row][col] == label:
                    return row, col

    def add_photo(self, label: str) -> str:
        """ Adds the photo in the first possible page and slot """
        if self.is_album_full():
            return "No more free slots"

        for row in self.photos:
            if len(row) == PhotoAlbum.PHOTOS_PER_PAGE:
                continue

            row.append(label)
            r, c = self.last_filled_photo(label)
            return f"{label} photo added successfully on page {r + 1} slot {c + 1}"

    def display(self) -> str:
        """ String representation of each page and the photos in it """
        result = '-----------'
        for r in self.photos:
            result += '\n' + ('[] ' * len(r)).strip()
            result += '\n-----------'

        return result

# album = PhotoAlbum(2)
# print(album.photos)
# print(album.is_album_full())
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
# print(album.display())
# album = PhotoAlbum(1)
# album.add_photo("baby")
# album.add_photo("first grade")
# album.add_photo("eight grade")
# album.add_photo("party with friends")
# print(album.display())
# album = PhotoAlbum(3)
# for _ in range(8):
#     album.add_photo("asdf")
# print(album.display())
# # result = album.display().strip()
