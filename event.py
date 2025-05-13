class Event:
    def __init__(self, id=None, title=None, description=None, date=None, location=None):
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.location = location
    
    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Date: {self.date}, Location: {self.location}"
    
    def to_tuple(self):
        """Convert the event object to a tuple for database operations"""
        return (self.title, self.description, self.date, self.location)
    
    def to_tuple_with_id(self):
        """Convert the event object to a tuple including the ID for database operations"""
        return (self.title, self.description, self.date, self.location, self.id)
    
    @staticmethod
    def from_tuple(tuple_data):
        """Create an Event object from a database tuple"""
        return Event(
            id=tuple_data[0],
            title=tuple_data[1],
            description=tuple_data[2],
            date=tuple_data[3],
            location=tuple_data[4]
        )
