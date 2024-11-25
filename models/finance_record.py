class FinanceRecord:
    def __init__(self, id, amount, category, date, description):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __repr__(self):
        return (f"FinanceRecord(id={self.id}, amount={self.amount}, category='{self.category}', "
                f"date='{self.date}', description='{self.description}')")
