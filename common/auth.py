"""
Login. Owner: Mark (Team lead).
"""
from common.file_handler import read_records

MAX_ATTEMPTS = 3


def login():
    """Return the logged-in user dict, or None after 3 failed attempts."""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        for user in read_records("users"):
            if user["username"] == username and user["password"] == password:
                print(f"\nWelcome, {username} ({user['role']})!")
                return user
        print(f"  Wrong username or password ({attempt}/{MAX_ATTEMPTS}).")
    print("Too many failed attempts.")
    return None
