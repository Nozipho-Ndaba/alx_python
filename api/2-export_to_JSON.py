"""
Export Employee TODO Progress to JSON

This script fetches an employee's TODO list and creates a JSON file with the data.
The script takes an employee ID as a command-line argument and generates a JSON
file containing the employee's TODO tasks in the desired format.

Usage:
    python script_name.py employee_id

Args:
    employee_id (int): The ID of the employee for whom to fetch the TODO list
        and create a JSON file.

Example:
    To export the TODO progress of an employee with ID 2:
    python script_name.py 2
"""


import json
import requests
import sys

def export_employee_todo_progress_to_json(employee_id):
    """
    Fetches an employee's TODO list and creates a JSON file with the data.

    Args:
        employee_id (int): The ID of the employee for whom to fetch TODO list and create a JSON file.
    """
    # Construct the URL for the employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    
    # Fetch employee details using an HTTP GET request
    employee_response = requests.get(employee_url)

    # Check if the employee exists (HTTP status code 200 indicates success)
    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    # Parse the JSON response to obtain employee data
    employee_data = employee_response.json()
    employee_username = employee_data['username']

    # Construct the URL for the employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    # Fetch the employee's TODO list using an HTTP GET request
    todos_response = requests.get(todos_url)

    # Check if the TODO list was successfully fetched
    if todos_response.status_code != 200:
        print(f"Unable to fetch TODO list for employee with ID {employee_id}.")
        return

    # Parse the JSON response to obtain the TODO list data
    todos_data = todos_response.json()

    # Create JSON data in the desired format
    json_data = {
        str(employee_id): [
            {"task": todo["title"], "completed": todo["completed"], "username": employee_username}
            for todo in todos_data
        ]
    }

    # Create a JSON file and write the data
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    # Extract the employee ID from the command-line argument
    employee_id = int(sys.argv[1])
    
    # Call the function to export the employee's TODO progress to JSON
    export_employee_todo_progress_to_json(employee_id)
