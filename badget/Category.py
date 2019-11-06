import json

class Category:
    
    def __init__(self, name, note):
        self.name = name
        self.note = note

    def __str__(self):
        return f'{json.dumps(self.to_dict(), default=str, indent=4)}'

    def to_dict(self):
        return {
            'name': self.name,
            'note': self.note,
        }

    @staticmethod
    def from_dict(d):
        return Category(d.get('name'), d.get('note'))
