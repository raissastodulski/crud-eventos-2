import sqlite3
from event import Event

class DatabaseManager:
    def __init__(self, db_name="events.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.initialize()
    
    def initialize(self):
        """Initialize the database connection and create tables if they don't exist"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self.create_tables()
            print(f"Database connection established: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
    def create_tables(self):
        """Create the events table if it doesn't exist"""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            date TEXT,
            location TEXT
        )
        ''')
        self.conn.commit()
    
    def close(self):
        """Close the database connection"""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
    
    # CRUD Operations
    
    def create_event(self, event):
        """Add a new event to the database"""
        try:
            self.cursor.execute('''
            INSERT INTO events (title, description, date, location)
            VALUES (?, ?, ?, ?)
            ''', event.to_tuple())
            self.conn.commit()
            print(f"Event '{event.title}' added successfully.")
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error creating event: {e}")
            return None
    
    def read_all_events(self):
        """Retrieve all events from the database"""
        try:
            self.cursor.execute("SELECT * FROM events")
            events = []
            for event_data in self.cursor.fetchall():
                events.append(Event.from_tuple(event_data))
            return events
        except sqlite3.Error as e:
            print(f"Error retrieving events: {e}")
            return []
    
    def read_event_by_id(self, event_id):
        """Retrieve a single event by ID"""
        try:
            self.cursor.execute("SELECT * FROM events WHERE id=?", (event_id,))
            event_data = self.cursor.fetchone()
            if event_data:
                return Event.from_tuple(event_data)
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving event: {e}")
            return None
    
    def update_event(self, event):
        """Update an existing event"""
        try:
            self.cursor.execute('''
            UPDATE events
            SET title=?, description=?, date=?, location=?
            WHERE id=?
            ''', event.to_tuple_with_id())
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print(f"Event '{event.title}' updated successfully.")
                return True
            print(f"No event found with ID {event.id}")
            return False
        except sqlite3.Error as e:
            print(f"Error updating event: {e}")
            return False
    
    def delete_event(self, event_id):
        """Delete an event by ID"""
        try:
            self.cursor.execute("DELETE FROM events WHERE id=?", (event_id,))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print(f"Event with ID {event_id} deleted successfully.")
                return True
            print(f"No event found with ID {event_id}")
            return False
        except sqlite3.Error as e:
            print(f"Error deleting event: {e}")
            return False
    
    def search_events(self, search_term):
        """Search for events containing the search term in title or description"""
        try:
            search_pattern = f"%{search_term}%"
            self.cursor.execute("""
            SELECT * FROM events 
            WHERE title LIKE ? OR description LIKE ? OR location LIKE ?
            """, (search_pattern, search_pattern, search_pattern))
            
            events = []
            for event_data in self.cursor.fetchall():
                events.append(Event.from_tuple(event_data))
            return events
        except sqlite3.Error as e:
            print(f"Error searching events: {e}")
            return []
