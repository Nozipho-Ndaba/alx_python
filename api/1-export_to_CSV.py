import sys
import requests
import csv


def get_employee_info(employee_id):
    # Retrieve employee details
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_data = response.json()
    employee_name = employee_data["name"]

    # Retrieve TODO list for the employee
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    # Export TODO list data to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            task_completed = "True" if todo["completed"] else "False"
            writer.writerow([employee_id, employee_name,
                            task_completed, todo["title"]])

    print(f"Data exported to {filename} successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py [employee_id]")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
