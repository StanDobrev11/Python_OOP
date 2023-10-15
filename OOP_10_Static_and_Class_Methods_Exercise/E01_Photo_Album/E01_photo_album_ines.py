from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos = self.__initialize_photo_album()
        self.current_page_idx = 0

    def __initialize_photo_album(self) -> List[List]:
        return [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        """ Creates a new instance of PhotoAlbum """
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str) -> str:
        """ Adds the photo in the first possible page and slot """
        try:
            if len(self.photos[self.current_page_idx]) == PhotoAlbum.PHOTOS_PER_PAGE:
                self.current_page_idx += 1
            self.photos[self.current_page_idx].append(label)
            return (f"{label} photo added successfully on page {self.current_page_idx + 1} "
                    f"slot {len(self.photos[self.current_page_idx])}")
        except IndexError:
            return "No more free slots"

    def display(self) -> str:
        """ String representation of each page and the photos in it """
        dashes = '-' * 11
        result = dashes
        for page in self.photos:
            result += '\n' + ' '.join(f"[]" for _ in page)
            result += '\n' + dashes

        return result

#
# album = PhotoAlbum(2)
# print(album.photos)
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
