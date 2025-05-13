# Event Management System

A simple console-based CRUD application for managing events with SQLite integration.

## Features

- Add new events with title, description, date, and location
- View all events in a simple list format
- View detailed information about a specific event
- Update existing events
- Delete events
- Search for events by title, description, or location

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses built-in SQLite)

## Usage

1. Navigate to the application directory:
   ```
   cd C:\Cesar\crud-eventos-2
   ```

2. Run the application:
   ```
   python main.py
   ```

3. Follow the on-screen instructions to interact with the application.

## File Structure

- `main.py` - Main application entry point
- `database.py` - Database operations using SQLite
- `event.py` - Event model class
- `menu.py` - Console menu interface
- `events.db` - SQLite database file (created automatically)

## Database Schema

The application creates a SQLite database with a single table:

```sql
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    date TEXT,
    location TEXT
)
```
