from infrastructure.interface import Interface
from service.dvd_service import DVDService
from service.friends_service import FriendsService
from service.loan_service import LoanService


class Main:
    def __init__(
        self,
        friends_service: FriendsService,
        dvd_service: DVDService,
        loan_service: LoanService,
        interface: Interface,
    ) -> None:
        pass

    def cadastra_amigos(self) -> None:
        pass

    def cadastra_dvd(self) -> None:
        pass

    def registra_emprestimos(self) -> None:
        pass


if __name__ == "__main__":
    pass
