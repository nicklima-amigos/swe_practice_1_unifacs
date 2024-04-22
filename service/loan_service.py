from entities.friend import Friend
from entities.loan import Loan
from entities.dvd import DVD
from typing import Optional
from service.loan_report_service import LoanReportService


class LoanService:
    def __init__(
        self, loans: Loan, loan_report_service: Optional[LoanReportService]
    ) -> None:
        self.loans = loans
        self.loan_report_service = loan_report_service

    def borrow(self) -> None: ...

    def return_dvd(self, dvd: DVD) -> None: ...

    def is_borrowed(self, dvd: DVD) -> bool:
        return False

    def is_underage(self, friend: Friend, dvd: DVD) -> bool:
        return False
