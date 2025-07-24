"""
Fake Data Generator Application

This application demonstrates using GitHub Copilot for project setup
and code scaffolding in Python.
"""

from fake_data_generator import FakeDataGenerator


def main():
    """Main function that runs the fake data generator application."""
    print("Fake data generator is running!")
    
    # Initialize the fake data generator
    generator = FakeDataGenerator()
    
    # Demonstrate the functionality
    print("\nAvailable data types:", generator.get_available_types())
    
    # Generate some sample data
    print("\nGenerating sample data:")
    names = generator.generate_data('names', 3)
    emails = generator.generate_data('emails', 3)
    
    print("Names:", names)
    print("Emails:", emails)
    
    print("\nDemo completed! Check out create_fake_data.py for AI-generated data.")


if __name__ == "__main__":
    main()