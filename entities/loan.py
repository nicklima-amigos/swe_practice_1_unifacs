from dataclasses import dataclass
from datetime import date

from entities.dvd import DVD
from entities.friend import Friend


@dataclass
class Loan:
    loan_date: date
    return_date: date
    friend: Friend
    dvd: DVD
