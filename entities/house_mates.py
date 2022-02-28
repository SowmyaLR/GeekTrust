from constants.constants import HOUSEFUL, SUCCESS, MEMEBER_NOT_FOUND
from entities.expense_calculator import ExpenseCalculator


class HouseMates:
    def __init__(self):
        self.house_mates = []
        self.expense_cal = ExpenseCalculator()

    def _is_house_ful(self):
        return len(self.house_mates) >= 3

    def move_in(self, member):
        if self._is_house_ful():
            print(HOUSEFUL)
        else:
            self.house_mates.append(member)
            self.expense_cal.initialize(member)
            print(SUCCESS)

    def _is_valid_house_mate(self, members):
        for mem in members:
            if mem not in self.house_mates:
                return False
        return True

    def spend(self, amount, members):
        if self._is_valid_house_mate(members):
            req_amnt = amount/len(members)
        else:
            print(MEMEBER_NOT_FOUND)
