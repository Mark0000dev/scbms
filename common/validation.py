# Ask the user for input and print tables.
from datetime import datetime

TIME_SLOTS = ["08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00",
              "12:00-13:00", "13:00-14:00", "14:00-15:00", "15:00-16:00",
              "16:00-17:00", "17:00-18:00", "18:00-19:00", "19:00-20:00",
              "20:00-21:00", "21:00-22:00"]


def get_text(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("  Cannot be empty.")


def get_int(prompt, minimum, maximum):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and minimum <= int(value) <= maximum:
            return int(value)
        print("  Enter a number from", minimum, "to", maximum)


def get_date(prompt):
    # returns date as text "YYYY-MM-DD"
    while True:
        value = input(prompt + " (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("  Wrong date format.")


def get_choice(prompt, options):
    # shows a numbered list, returns the chosen option
    for i in range(len(options)):
        print("  " + str(i + 1) + ". " + options[i])
    number = get_int(prompt, 1, len(options))
    return options[number - 1]


def confirm(prompt):
    answer = input(prompt + " (y/n): ").strip().lower()
    return answer == "y"


def today():
    return datetime.now().strftime("%Y-%m-%d")


def print_table(records, fields):
    if len(records) == 0:
        print("  No records found.")
        return
    header = ""
    for field in fields:
        header += field.upper().ljust(20)
    print(header)
    print("-" * len(header))
    for record in records:
        line = ""
        for field in fields:
            line += str(record[field]).ljust(20)
        print(line)


def pause():
    input("\nPress Enter to continue...")
