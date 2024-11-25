class Note:
    def __init__(self, id, title, content=None, timestamp=None):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp

    def __repr__(self):
        return (f"Note(id={self.id}, title='{self.title}', content='{self.content}', "
                f"timestamp='{self.timestamp}')")
