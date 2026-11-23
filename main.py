"""
ActiveLife Sports Centre - Booking Management System (SCBMS)
Entry point: login -> open the menu for the user's role.
Run from the project folder:  python main.py
"""
from common.auth import login
from modules import admin, membership, booking, fitness, member

ROLE_MENUS = {
    "admin": admin.menu,            # Mark Bakulin       - Centre Administrator
    "membership": membership.menu,  # Arazmyrat Atajykov - Membership Officer
    "booking": booking.menu,        # Vepa Garayev       - Booking Officer
    "instructor": fitness.menu,     # Maxim Kalinin      - Fitness Instructor
    "member": member.menu,          # Liyaqat Rafiq Lone - Member
}


def main():
    while True:
        print("\n========================================")
        print("   ActiveLife Sports Centre - SCBMS")
        print("========================================")
        print("1. Login")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            user = login()
            if user:
                ROLE_MENUS[user["role"]](user)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
