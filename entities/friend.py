from dataclasses import dataclass
from entities.person import Person


@dataclass
class Friend(Person):
    phone_number: str
    email: str
    address: str
