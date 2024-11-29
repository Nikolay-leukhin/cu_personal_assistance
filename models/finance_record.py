class FinanceRecord:
    def __init__(self, amount, category, date, description, id=None):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __repr__(self):
        return (f"FinanceRecord(id={self.id}, amount={self.amount}, category='{self.category}', "
                f"date='{self.date}', description='{self.description}')")

    def to_json(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data['id'],
            amount=data['amount'],
            category=data['category'],
            date=data['date'],
            description=data.get('description')
        )
