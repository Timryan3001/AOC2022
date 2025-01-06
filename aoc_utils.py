import requests
import os
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()

SESSION_COOKIE = os.getenv("SESSION")
BASE_URL = "https://adventofcode.com/2022/day/{day}/input"

# Define the inputs folder path, located one level up from the current script's directory
current_directory = os.path.dirname(os.path.abspath(__file__))
inputs_folder = os.path.join(current_directory, 'inputs')

def fetch_input(day, save_to_file=True):
    """
    Fetch the input for the specified AoC day.
    Args:
        day (int): The day of the challenge.
        save_to_file (bool): Whether to save the input to a file.
    Returns:
        str: The input as a string.
    """
    # Ensure the inputs folder exists
    os.makedirs(inputs_folder, exist_ok=True)
    
    # Define the path to the input file
    file_path = os.path.join(inputs_folder, f"day{day}.txt")
    
    # Check if the input file already exists
    if os.path.exists(file_path):
        print(f"Input file for day {day} already exists. Reading from file: {file_path}")
        with open(file_path, "r") as f:
            return f.read().strip()  # Read and return the file contents

    # If the file doesn't exist, fetch it from the Advent of Code site
    url = BASE_URL.format(day=day)
    cookies = {"session": SESSION_COOKIE}
    
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        input_data = response.text.strip()  # Remove any trailing whitespace
        
        if save_to_file:
            # Save the input to a file
            with open(file_path, "w") as f:
                f.write(input_data)
            print(f"Input for day {day} saved to: {file_path}")
        
        return input_data
    else:
        raise Exception(f"Failed to fetch input for day {day}. Status code: {response.status_code}")


def get_day_from_filename(filename=None):
    """
    Extracts the day number from the filename provided.
    Args:
        filename (str): The filename to extract the day from. If None, defaults to __file__.
    Returns:
        int: The day number.
    """
    # If no filename is passed, use __file__ (current file)
    if filename is None:
        filename = os.path.basename(__file__)
    
    print(f"Filename: {filename}")  # Debugging line
    match = re.search(r'day(\d+)', filename, re.IGNORECASE)
    if not match:
        raise ValueError("Could not find 'dayXX' in the filename. Ensure the script is named like 'day01.py'.")
    
    day = match.group(1)
    return int(day.lstrip('0'))
