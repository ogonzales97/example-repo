"""
This module defines the `Album` class, which encapsulates
the details of a music album.


Classes:
    Album: Represents a music album with its name, number of songs, and artist.


    Methods:
        __str__(): Returns a string representation of the album details.
the details of a music album."""


class Album:
    """
    This class represents a music album with its name,
    number of songs, and artist.

    Attributes:
        album_name (str): The name of the album.
        number_of_songs (int): The number of songs in the album.
        album_artist (str): The artist of the album.
    Returns:
        str: A string representation of the album details.
    """

    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return (f"Album Name: {self.album_name}, "
                f"Number of Songs: {self.number_of_songs}, "
                f"Album Artist: {self.album_artist}")


albums1 = [Album("Thriller", 9, "Michael Jackson"),
           Album("Back in Black", 10, "AC/DC"),
           Album("The Dark Side of the Moon", 10, "Pink Floyd"),
           Album("The Bodyguard", 12, "Whitney Houston"),
           Album("Rumours", 11, "Fleetwood Mac")]
for album in albums1:
    print(album)
print("\nSorted by number of songs:")
# Sorting songs by number of songs in album
albums1.sort(key=lambda album: album.number_of_songs)
for album in albums1:
    print(album)
# Swapping first and second albums
print("\nAfter replacing first album with second:")
albums1[0], albums1[1] = albums1[1], albums1[0]
for album in albums1:
    print(album)


albums2 = [Album("21", 11, "Adele"),
           Album("1989", 13, "Taylor Swift"),
           Album("Abbey Road", 17, "The Beatles"),
           Album("Hotel California", 9, "Eagles"),
           Album("Led Zeppelin IV", 8, "Led Zeppelin")]
print("\nAlbums2 original order:")
for album in albums2:
    print(album)
albums2 = albums1.copy()  # Creates a separate copy
print("\nAfter assigning albums1 to albums2:")
for album in albums2:
    print(album)

albums2.extend([Album("Dark Side of the Moon", 9, "Pink Floyd"),
                Album("Oops!...I Did It Again", 16, "Britney Spears")])
print("\nAfter extending albums2 with two new albums:")
for album in albums2:
    print(album)

albums2.sort(key=lambda album: album.album_name)
print("\nAlbums2 sorted by album name:")
for album in albums2:
    print(album)


def binary_search_album_by_name(albums, target_album_name):
    """
    Perform a binary search to find an album by its name.

    Args:
        albums (list of Album): The list of albums to search.
        target_album_name (str): The name of the album to search for.

    Returns:
        Album or None: The found album or None if not found.
    """
    low = 0
    high = len(albums) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_name = albums[mid].album_name

        if mid_name == target_album_name:
            return albums[mid]
        elif mid_name < target_album_name:
            low = mid + 1
        else:
            high = mid - 1

    return None


# Searching for Dark Side of the Moon
TARGET_NAME = "Dark Side of the Moon"

print(f"\nSearching for album '{TARGET_NAME}':")
found_album = binary_search_album_by_name(albums2, TARGET_NAME)
if found_album:
    print("Album found:", found_album)
else:
    print("Album not found.")
