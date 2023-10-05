import requests
import sys


def get_todo_progress(employee_id):
    # Get employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Get TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Count completed tasks and total tasks
    completed_tasks = [task for task in todos_data if task["completed"]]
    total_tasks = len(todos_data)
    num_completed_tasks = len(completed_tasks)

    # Print the result
    print(
        f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid employee ID.")
