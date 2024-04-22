from entities.dvd import DVD
from entities.friend import Friend


class DVDService:
    def __init__(self, dvds: list[DVD]) -> None:
        self.dvds = dvds

    def include(self, friend: Friend) -> None: ...

    def change(self, id: int) -> None: ...

    def remove(self, id: int) -> None: ...
