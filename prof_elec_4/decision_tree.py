class DT:
    def __init__(self, refund: bool, marital_status: str, taxable_income: float):
        self.refund = refund
        self.marital_status = marital_status.lower()
        self.taxable_income = taxable_income
        self.cheat = "no"

        if not self.refund:
            if self.marital_status == "married":
                self.cheat = "no"
            elif self.marital_status in ["single", "divorced"] and self.taxable_income >= 80000.0:
                self.cheat = "yes"


class People:
    def __init__(self):
        self.lst = []

    def insert(self, person: DT):
        self.lst.append(person)

    def print_details(self):
        for i, j in enumerate(self.lst, start=1):
            print(f"{i}   {j.refund}   {j.marital_status}   {j.taxable_income}   {j.cheat}")

    def count_cheat(self):
        yes = sum(1 for i in self.lst if i.cheat == "yes")
        no = len(self.lst) - yes
        return [yes, no]

    def get_size(self):
        return len(self.lst)

    def get_json(self):
        pass
