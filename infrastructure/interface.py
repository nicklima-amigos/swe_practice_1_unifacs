from entities.dvd import DVD
from entities.friend import Friend
from service.loan_report_service import LoanReportService


class Interface:
    def __init__(self, loan_report_service: LoanReportService) -> None:
        self.loan_report_service = loan_report_service

    def print(self, message: str) -> None: ...

    def print_menu(self) -> None: ...

    def read_dvd(self) -> DVD: ...

    def read_friend(self) -> Friend: ...

    def read_loan(self) -> None: ...
