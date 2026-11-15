
import csv
import os
from datetime import datetime

# Registered students and simulated fingerprint IDs
students = {
    "FP01": {"id": "101", "name": "Student A"},
    "FP02": {"id": "102", "name": "Student B"},
    "FP03": {"id": "103", "name": "Student C"}
}

# Attendance file location
folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "attendance.csv")


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Student ID",
                "Student Name",
                "Date",
                "Time",
                "Status"
            ])


# Check whether attendance is already marked
def already_marked(student_id, today):
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if row[0] == student_id and row[2] == today:
                return True

    return False


# Simulated fingerprint identification
def scan_fingerprint():

    fingerprint = input("\nEnter Fingerprint ID (FP01/FP02/FP03): ")

    if fingerprint not in students:
        print("Invalid Fingerprint!")
        print("Access Denied")
        return

    student = students[fingerprint]

    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    print("\nFingerprint Matched!")
    print("Student Name:", student["name"])
    print("Student ID:", student["id"])

    if already_marked(student["id"], today):
        print("Attendance already marked today!")
        return

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            student["id"],
            student["name"],
            today,
            current_time,
            "Present"
        ])

    print("Attendance Successfully Marked!")
    print("Date:", today)
    print("Time:", current_time)


# Main program
def main():

    create_file()

    while True:
        print("\n===== BIOMETRIC ATTENDANCE SYSTEM =====")
        print("1. Scan Fingerprint")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            scan_fingerprint()

        elif choice == "2":
            print("Attendance System Closed.")
            break

        else:
            print("Invalid Choice! Try Again.")


main()
