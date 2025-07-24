"""
Create Fake Data using Ollama

This script connects to a local Ollama server and uses an AI model
to generate fake data in CSV format.
"""

import requests
import json


def create_ollama_prompt():
    """Generate a prompt for fake data generation."""
    prompt = """Generate data for 5 people in CSV format with these columns:
name,email,age,city,occupation

Please only return the raw CSV data without any additional text or explanations."""
    return prompt


def call_ollama_api(prompt, model="phi3.5:latest"):
    """
    Send a prompt to Ollama API and return the response.
    
    Args:
        prompt (str): The prompt to send to the model
        model (str): The model name to use (default: phi3.5:latest)
        
    Returns:
        str: The response from the model
    """
    # Setup connection parameters for Ollama server
    url = "http://localhost:11434/api/generate"
    
    # Prepare the request payload
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        # Make the API request
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        # Parse the response
        result = response.json()
        return result.get('response', '')
        
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Ollama: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing response: {e}")
        return None


def save_csv_data(data, filename="fake_data.csv"):
    """
    Save the generated data to a CSV file.
    
    Args:
        data (str): The CSV data to save
        filename (str): The filename to save to
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")


def main():
    """Main function to generate and save fake data."""
    print("Connecting to Ollama to generate fake data...")
    
    # Create the prompt
    prompt = create_ollama_prompt()
    
    # Call Ollama API
    response = call_ollama_api(prompt)
    
    if response:
        # Save the response to a CSV file
        save_csv_data(response)
        print("Fake data generation completed!")
    else:
        print("Failed to generate fake data. Make sure Ollama is running.")
        print("You can start Ollama with: ollama serve")
        print("And pull the model with: ollama pull phi3.5:latest")


if __name__ == "__main__":
    main()