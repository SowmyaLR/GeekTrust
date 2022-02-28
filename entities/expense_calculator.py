from constants.constants import OWES_TO, AMOUNT, RECORD

class ExpenseCalculator:
    def __init__(self):
        self.expense_tracker = {}

    def initialize(self, person):
        self.expense_tracker[person] = {
            OWES_TO: [],
            RECORD: []
        }

    def add_expense(self, person, spent_by, amnt):
        if person in self.expense_tracker[spent_by][OWES_TO]:
            for record in self.expense_tracker[spent_by][RECORD]:
                if record[OWES_TO] == person:
                    record[AMOUNT] -= amnt
        else:
            if spent_by in self.expense_tracker[person][OWES_TO]:
                for record in self.expense_tracker[spent_by][RECORD]:
                    if record[OWES_TO] == person:
                        record[AMOUNT] += amnt
            else:
                self.expense_tracker[person][OWES_TO].append(spent_by)
                self.expense_tracker[person][RECORD].append({
                    OWES_TO: spent_by,
                    AMOUNT: amnt
                })

