from event import Event
import os
import datetime

class MenuInterface:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        """Display the main menu options"""
        self.clear_screen()
        print("\n===== EVENT MANAGEMENT SYSTEM =====")
        print("1. Add New Event")
        print("2. View All Events")
        print("3. View Event Details")
        print("4. Update Event")
        print("5. Delete Event")
        print("6. Search Events")
        print("0. Exit")
        print("===================================")
        return input("Enter your choice: ")
    
    def run(self):
        """Run the menu interface"""
        while True:
            choice = self.display_menu()
            
            if choice == '1':
                self.add_event()
            elif choice == '2':
                self.view_all_events()
            elif choice == '3':
                self.view_event_details()
            elif choice == '4':
                self.update_event()
            elif choice == '5':
                self.delete_event()
            elif choice == '6':
                self.search_events()
            elif choice == '0':
                print("Exiting the application. Goodbye!")
                self.db_manager.close()
                break
            else:
                input("Invalid choice. Press Enter to continue...")
    
    def add_event(self):
        """Add a new event"""
        self.clear_screen()
        print("\n===== ADD NEW EVENT =====")
        
        title = input("Enter event title: ")
        description = input("Enter event description: ")
        
        # Date validation
        while True:
            date_str = input("Enter event date (YYYY-MM-DD): ")
            try:
                # Validate date format
                if date_str:
                    datetime.datetime.strptime(date_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        location = input("Enter event location: ")
        
        event = Event(title=title, description=description, date=date_str, location=location)
        self.db_manager.create_event(event)
        
        input("\nPress Enter to continue...")
    
    def view_all_events(self):
        """View all events"""
        self.clear_screen()
        print("\n===== ALL EVENTS =====")
        
        events = self.db_manager.read_all_events()
        
        if not events:
            print("No events found.")
        else:
            for event in events:
                print(event)
        
        input("\nPress Enter to continue...")
    
    def view_event_details(self):
        """View details of a specific event"""
        self.clear_screen()
        print("\n===== EVENT DETAILS =====")
        
        event_id = input("Enter event ID: ")
        if not event_id.isdigit():
            print("Invalid ID. Please enter a number.")
            input("\nPress Enter to continue...")
            return
        
        event = self.db_manager.read_event_by_id(int(event_id))
        
        if event:
            print("\nEvent Details:")
            print(f"ID: {event.id}")
            print(f"Title: {event.title}")
            print(f"Description: {event.description}")
            print(f"Date: {event.date}")
            print(f"Location: {event.location}")
        else:
            print(f"No event found with ID {event_id}")
        
        input("\nPress Enter to continue...")
    
    def update_event(self):
        """Update an existing event"""
        self.clear_screen()
        print("\n===== UPDATE EVENT =====")
        
        event_id = input("Enter event ID to update: ")
        if not event_id.isdigit():
            print("Invalid ID. Please enter a number.")
            input("\nPress Enter to continue...")
            return
        
        event = self.db_manager.read_event_by_id(int(event_id))
        
        if not event:
            print(f"No event found with ID {event_id}")
            input("\nPress Enter to continue...")
            return
        
        print("\nCurrent Event Details:")
        print(f"ID: {event.id}")
        print(f"Title: {event.title}")
        print(f"Description: {event.description}")
        print(f"Date: {event.date}")
        print(f"Location: {event.location}")
        print("\nEnter new details (leave blank to keep current value):")
        
        new_title = input(f"New title [{event.title}]: ")
        if new_title:
            event.title = new_title
        
        new_description = input(f"New description [{event.description}]: ")
        if new_description:
            event.description = new_description
        
        # Date validation
        while True:
            new_date = input(f"New date [{event.date}] (YYYY-MM-DD): ")
            if not new_date:
                break
            try:
                # Validate date format
                datetime.datetime.strptime(new_date, "%Y-%m-%d")
                event.date = new_date
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        new_location = input(f"New location [{event.location}]: ")
        if new_location:
            event.location = new_location
        
        success = self.db_manager.update_event(event)
        if not success:
            print("Failed to update the event.")
        
        input("\nPress Enter to continue...")
    
    def delete_event(self):
        """Delete an event"""
        self.clear_screen()
        print("\n===== DELETE EVENT =====")
        
        event_id = input("Enter event ID to delete: ")
        if not event_id.isdigit():
            print("Invalid ID. Please enter a number.")
            input("\nPress Enter to continue...")
            return
        
        event = self.db_manager.read_event_by_id(int(event_id))
        
        if not event:
            print(f"No event found with ID {event_id}")
            input("\nPress Enter to continue...")
            return
        
        print("\nEvent to delete:")
        print(f"ID: {event.id}")
        print(f"Title: {event.title}")
        print(f"Description: {event.description}")
        print(f"Date: {event.date}")
        print(f"Location: {event.location}")
        
        confirm = input("\nAre you sure you want to delete this event? (y/n): ")
        
        if confirm.lower() == 'y':
            success = self.db_manager.delete_event(int(event_id))
            if not success:
                print("Failed to delete the event.")
        else:
            print("Deletion cancelled.")
        
        input("\nPress Enter to continue...")
    
    def search_events(self):
        """Search for events"""
        self.clear_screen()
        print("\n===== SEARCH EVENTS =====")
        
        search_term = input("Enter search term: ")
        
        if not search_term:
            print("Search term cannot be empty.")
            input("\nPress Enter to continue...")
            return
        
        events = self.db_manager.search_events(search_term)
        
        if not events:
            print(f"No events found matching '{search_term}'.")
        else:
            print(f"\nFound {len(events)} matching events:")
            for event in events:
                print(event)
        
        input("\nPress Enter to continue...")
