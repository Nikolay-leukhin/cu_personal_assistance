class Contact:
    def __init__(self, id, name, phone=None, email=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return (f"Contact(id={self.id}, name='{self.name}', phone='{self.phone}', "
                f"email='{self.email}')")
