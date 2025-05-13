from database import DatabaseManager
from menu import MenuInterface
import os

def main():
    """Main application entry point"""
    # Set the database path to the current directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "events.db")
    
    # Initialize the database manager
    db_manager = DatabaseManager(db_path)
    
    # Initialize and run the menu interface
    menu = MenuInterface(db_manager)
    try:
        menu.run()
    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        # Make sure to close the database connection
        db_manager.close()

if __name__ == "__main__":
    main()
