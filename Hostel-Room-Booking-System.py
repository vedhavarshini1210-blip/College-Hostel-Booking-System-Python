import random

# -----------------------------
# College Hostel Booking System
# -----------------------------

rooms = {
    101: {"type": "Single", "status": "Available"},
    102: {"type": "Single", "status": "Available"},
    103: {"type": "Double", "status": "Available"},
    104: {"type": "Double", "status": "Available"},
    105: {"type": "Triple", "status": "Available"},
    106: {"type": "Triple", "status": "Available"},
    107: {"type": "Single", "status": "Available"},
    108: {"type": "Double", "status": "Available"},
    109: {"type": "Triple", "status": "Available"},
    110: {"type": "Single", "status": "Available"}
}

bookings = {}

# -----------------------------
# View Available Rooms
# -----------------------------

def view_available_rooms():
    print("\n========== AVAILABLE ROOMS ==========")

    available = False

    for room_no, info in rooms.items():
        if info["status"] == "Available":
            print(f"Room {room_no} | Type: {info['type']}")
            available = True

    if not available:
        print("No rooms are available.")

# -----------------------------
# Book Room
# -----------------------------

def book_room(room_number):

    if room_number not in rooms:
        print("Invalid room number.")
        return

    if rooms[room_number]["status"] == "Occupied":
        print("Room already occupied.")
        return

    print("\nEnter Student Details")

    name = input("Student Name : ")
    reg_no = input("Register Number : ")
    department = input("Department : ")
    year = input("Year : ")
    mobile = input("Mobile Number : ")

    booking_id = random.randint(1000, 9999)

    bookings[room_number] = {
        "Booking ID": booking_id,
        "Name": name,
        "Register Number": reg_no,
        "Department": department,
        "Year": year,
        "Mobile": mobile
    }

    rooms[room_number]["status"] = "Occupied"

    print("\n========== BOOKING SUCCESSFUL ==========")
    print(f"Booking ID     : {booking_id}")
    print(f"Room Number    : {room_number}")
    print(f"Room Type      : {rooms[room_number]['type']}")
    print(f"Student Name   : {name}")

# -----------------------------
# Cancel Booking
# -----------------------------

def cancel_booking(room_number):

    if room_number not in rooms:
        print("Invalid room number.")
        return

    if rooms[room_number]["status"] == "Available":
        print("This room is already available.")
        return

    del bookings[room_number]
    rooms[room_number]["status"] = "Available"

    print("Booking cancelled successfully.")

# -----------------------------
# Admin View
# -----------------------------

def admin_manage_rooms():

    print("\n========== ALL ROOM STATUS ==========")

    for room_no in sorted(rooms.keys()):

        room = rooms[room_no]

        print(f"\nRoom Number : {room_no}")
        print(f"Room Type   : {room['type']}")
        print(f"Status      : {room['status']}")

        if room_no in bookings:
            student = bookings[room_no]
            print(f"Student     : {student['Name']}")
            print(f"Register No : {student['Register Number']}")
            print(f"Department  : {student['Department']}")
            print(f"Year        : {student['Year']}")
            print(f"Mobile      : {student['Mobile']}")
# -----------------------------
# Room Statistics
# -----------------------------

def show_statistics():

    total_rooms = len(rooms)
    available = sum(1 for room in rooms.values()
                    if room["status"] == "Available")
    occupied = total_rooms - available

    print("\n========== ROOM STATISTICS ==========")
    print(f"Total Rooms     : {total_rooms}")
    print(f"Available Rooms : {available}")
    print(f"Occupied Rooms  : {occupied}")

# -----------------------------
# Search Booking
# -----------------------------

def search_booking():

    room_number = int(input("Enter Room Number: "))

    if room_number in bookings:

        student = bookings[room_number]

        print("\n========== BOOKING DETAILS ==========")
        print(f"Booking ID     : {student['Booking ID']}")
        print(f"Student Name   : {student['Name']}")
        print(f"Register No    : {student['Register Number']}")
        print(f"Department     : {student['Department']}")
        print(f"Year           : {student['Year']}")
        print(f"Mobile Number  : {student['Mobile']}")

    else:
        print("No booking found for this room.")

# -----------------------------
# Main Menu
# -----------------------------

def main():

    while True:

        print("\n===================================")
        print("   COLLEGE HOSTEL BOOKING SYSTEM")
        print("===================================")
        print("1. View Available Rooms")
        print("2. Book a Room")
        print("3. Cancel Booking")
        print("4. Admin - View All Rooms")
        print("5. Show Statistics")
        print("6. Search Booking")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            view_available_rooms()

        elif choice == "2":

            try:
                room = int(input("Enter Room Number: "))
                book_room(room)

            except ValueError:
                print("Please enter a valid room number.")

        elif choice == "3":

            try:
                room = int(input("Enter Room Number: "))
                cancel_booking(room)

            except ValueError:
                print("Please enter a valid room number.")

        elif choice == "4":
            admin_manage_rooms()

        elif choice == "5":
            show_statistics()

        elif choice == "6":

            try:
                search_booking()

            except ValueError:
                print("Please enter a valid room number.")

        elif choice == "7":

            print("\n===================================")
            print(" Thank You for Using")
            print(" College Hostel Booking System")
            print("===================================")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# -----------------------------
# Program Entry Point
# -----------------------------

if __name__ == "__main__":
    main()