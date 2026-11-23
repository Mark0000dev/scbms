"""
Shared input / output helpers so every menu behaves the same way.
Owner: Mark (Team lead).
"""
from datetime import date, datetime

TIME_SLOTS = [f"{h:02d}:00-{h + 1:02d}:00" for h in range(8, 22)]  # 08:00-09:00 ... 21:00-22:00
DATE_FORMAT = "%Y-%m-%d"


def get_text(prompt):
    """Ask until the user types something non-empty (and without '|')."""
    while True:
        value = input(prompt).strip()
        if value and "|" not in value:
            return value
        print("  Invalid input: cannot be empty or contain '|'.")


def get_int(prompt, minimum=None, maximum=None):
    while True:
        value = input(prompt).strip()
        if value.lstrip("-").isdigit():
            number = int(value)
            if (minimum is None or number >= minimum) and (maximum is None or number <= maximum):
                return number
        print(f"  Enter a whole number between {minimum} and {maximum}.")


def get_date(prompt, allow_past=True):
    """Ask for a date in YYYY-MM-DD format. Returns the string."""
    while True:
        value = input(prompt + " (YYYY-MM-DD): ").strip()
        try:
            parsed = datetime.strptime(value, DATE_FORMAT).date()
        except ValueError:
            print("  Wrong date format.")
            continue
        if not allow_past and parsed < date.today():
            print("  Date cannot be in the past.")
            continue
        return value


def get_choice(prompt, options):
    """Show numbered options, return the chosen option (not the number)."""
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")
    index = get_int(prompt, 1, len(options))
    return options[index - 1]


def confirm(prompt):
    return input(prompt + " (y/n): ").strip().lower() == "y"


def today():
    return date.today().strftime(DATE_FORMAT)


def print_table(records, fields):
    """Print a list of dicts as a simple aligned table."""
    if not records:
        print("  (no records found)")
        return
    widths = {f: max(len(f), *(len(str(r[f])) for r in records)) for f in fields}
    print("  " + "  ".join(f.upper().ljust(widths[f]) for f in fields))
    print("  " + "  ".join("-" * widths[f] for f in fields))
    for r in records:
        print("  " + "  ".join(str(r[f]).ljust(widths[f]) for f in fields))


def pause():
    input("\nPress Enter to continue...")
