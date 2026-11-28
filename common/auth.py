# Login: check username and password in users.txt
from common.file_handler import read_records


def login():
    # returns the user (dict) or None after 3 wrong tries
    for attempt in range(3):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        for user in read_records("users"):
            if user["username"] == username and user["password"] == password:
                print("\nWelcome,", username)
                return user
        print("  Wrong username or password.")
    print("Too many wrong tries.")
    return None
