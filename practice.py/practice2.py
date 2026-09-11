import datetime

# Define a dictionary to store attendance records
attendance_records = {}

# Define a function to add an attendance record for a specific employee
def add_attendance_record(employee_id):
    # Get the current date and time
    current_time = datetime.datetime.now()
    # Add the attendance record to the dictionary
    attendance_records[employee_id] = current_time
    print(f"Attendance record added for employee {employee_id} at {current_time}")

# Define a function to display all attendance records
def display_attendance_records():
    # Check if there are any attendance records
    if not attendance_records:
        print("No attendance records found.")
    else:
        # Loop through the attendance records and display them
        for employee_id, time in attendance_records.items():
            print(f"Employee {employee_id} attended at {time}")

# Define a function to remove an attendance record for a specific employee
def remove_attendance_record(employee_id):
    # Check if the employee has an attendance record
    if employee_id in attendance_records:
        # Remove the attendance record from the dictionary
        del attendance_records[employee_id]
        print(f"Attendance record removed for employee {employee_id}")
    else:
        print(f"No attendance record found for employee {employee_id}")

# Define a function to update an attendance record for a specific employee
def update_attendance_record(employee_id):
    # Check if the employee has an attendance record
    if employee_id in attendance_records:
        # Get the current date and time
        current_time = datetime.datetime.now()
        # Update the attendance record in the dictionary
        attendance_records[employee_id] = current_time
        print(f"Attendance record updated for employee {employee_id} at {current_time}")
    else:
        print(f"No attendance record found for employee {employee_id}")

# Define a function to search for an attendance record by employee ID
def search_attendance_record(employee_id):
    # Check if the employee has an attendance record
    if employee_id in attendance_records:
        # Display the attendance record
        print(f"Employee {employee_id} attended at {attendance_records[employee_id]}")
    else:
        print(f"No attendance record found for employee {employee_id}")

# Define a main function to run the attendance tracker app
def main():
    # Loop until the user decides to exit
    while True:
        # Display the menu options
        print("\nAttendance Tracker App")
        print("1. Add attendance record")
        print("2. Display all attendance records")
        print("3. Remove attendance record")
        print("4. Update attendance record")
        print("5. Search attendance record by employee ID")
        print("6. Exit")
        # Get the user's choice
        choice = input("Enter your choice: ")
        # Call the appropriate function based on the user's choice
        if choice == "1":
            employee_id = input("Enter employee ID: ")
            add_attendance_record(employee_id)
        elif choice == "2":
            display_attendance_records()
        elif choice == "3":
            employee_id = input("Enter employee ID: ")
            remove_attendance_record(employee_id)
        elif choice == "4":
            employee_id = input("Enter employee ID: ")
            update_attendance_record(employee_id)
        elif choice == "5":
            employee_id = input("Enter employee ID: ")
            search_attendance_record(employee_id)
        elif choice == "6":
            print("Exiting attendance tracker app...")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to run the attendance tracker app
if __name__ == "__main__":
    main()