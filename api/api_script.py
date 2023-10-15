import sys
import requests

def get_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    
    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        print(f"Unable to fetch TODO list for employee with ID {employee_id}.")
        return
    
    todos_data = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Format progress
    progress = (
        f"EmployeeSP{employee_name}SisSdoneSwithStasks({completed_tasks}/{total_tasks}):"
    )
    
    # Format completed task titles
    task_titles = [f"T{todo['title']}" for todo in todos_data if todo['completed']]

    # Output formatted progress and task titles
    print(progress)
    for title in task_titles:
        print(title)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
