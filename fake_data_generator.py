"""
Fake Data Generator Class

This module contains the FakeDataGenerator class that can be used
to generate various types of fake data for testing and development purposes.
"""


class FakeDataGenerator:
    """A class for generating fake data for testing and development."""
    
    def __init__(self):
        """Initialize the fake data generator."""
        self.data_types = ['names', 'emails', 'addresses', 'phone_numbers']
    
    def generate_data(self, data_type='names', count=10):
        """
        Generate fake data of the specified type.
        
        Args:
            data_type (str): The type of data to generate
            count (int): Number of data items to generate
            
        Returns:
            list: A list of generated fake data items
        """
        # This is a basic implementation - in a real application
        # you might use libraries like Faker or generate actual fake data
        
        if data_type == 'names':
            return [f"Person {i+1}" for i in range(count)]
        elif data_type == 'emails':
            return [f"user{i+1}@example.com" for i in range(count)]
        elif data_type == 'addresses':
            return [f"{i+1} Main St, City {i+1}" for i in range(count)]
        elif data_type == 'phone_numbers':
            return [f"555-{1000+i:04d}" for i in range(count)]
        else:
            return [f"Data item {i+1}" for i in range(count)]
    
    def get_available_types(self):
        """
        Get a list of available data types.
        
        Returns:
            list: Available data types
        """
        return self.data_types