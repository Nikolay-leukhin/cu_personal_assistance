class Note:
    def __init__(self, title, id=None, content=None, timestamp=None):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp

    def __repr__(self):
        return (f"Note(id={self.id}, title='{self.title}', content='{self.content}', "
                f"timestamp='{self.timestamp}')")

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data['id'],
            title=data['title'],
            content=data.get('content'),
            timestamp=data.get('timestamp')
        )
