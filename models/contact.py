class Contact:
    def __init__(self, name, id=None, phone=None, email=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return (f"Contact(id={self.id}, name='{self.name}', phone='{self.phone}', "
                f"email='{self.email}')")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            phone=data.get('phone'),
            email=data.get('email')
        )
