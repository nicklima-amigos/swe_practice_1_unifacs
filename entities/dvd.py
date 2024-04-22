from dataclasses import dataclass
from entities.genre import Genre
from entities.person import Person
from entities.age_group import AgeGroup


@dataclass
class DVD:
    title: str
    synopsis: str
    genre: Genre
    main_artist: Person
    director: Person
    age_group: AgeGroup
