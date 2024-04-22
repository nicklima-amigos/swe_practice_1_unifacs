from entities.friend import Friend


class FriendsService:
    def __init__(self, friends: list[Friend]) -> None:
        self.friends = friends

    def include(self, friend: Friend) -> None: ...

    def change(self, id: int) -> None: ...

    def remove(self, id: int) -> None: ...
