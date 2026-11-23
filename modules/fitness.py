"""
Fitness Instructor module
Owner: Maxim Kalinin (TP082468)
Files: classes.txt, registrations.txt (main); reads members.txt.
"""
from common import file_handler as fh
from common import validation as v

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


# ---------- INTERFACE (other modules call these - implement FIRST, don't rename) ----------
def count_registered(class_id):
    """Number of registrations for this class."""
    # TODO
    return 0


def register_member_for_class(member_id, class_id):
    """Checks: class exists & active, membership active, not already registered,
    count_registered < capacity (Fitness class capacity checking).
    Save to registrations.txt (attendance = 'pending'). Return reg_id or None.
    Used by this module AND member.py."""
    # TODO
    print("TODO: register_member_for_class")
    return None


def remove_registration(reg_id):
    """Delete a registration. Return True/False. Used by this module AND member.py."""
    # TODO
    print("TODO: remove_registration")
    return False


# ---------- MENU ACTIONS ----------
def add_class(user):
    """TODO: name, day (DAYS), time slot (v.TIME_SLOTS), capacity; instructor_id = user['user_id']."""
    print("TODO: add_class")


def register_member_menu(user):
    print("TODO: ask member id + class id -> register_member_for_class")


def record_attendance(user):
    """TODO: pick class, for each registration set attendance present/absent."""
    print("TODO: record_attendance")


def view_classes(user):
    """TODO: list classes with 'registered / capacity'."""
    print("TODO: view_classes")


def view_participants(user):
    print("TODO: view_participants of a class")


def update_class(user):
    """TODO: change day / time / capacity (capacity can't go below count_registered)."""
    print("TODO: update_class")


def delete_class(user):
    """TODO: BLOCK if count_registered(class_id) > 0."""
    print("TODO: delete_class")


def remove_member_from_class(user):
    print("TODO: remove_member_from_class -> remove_registration")


def attendance_report(user):
    """TODO: per class: registered, present, absent, attendance %."""
    print("TODO: attendance_report")


def menu(user):
    actions = {
        "1": ("Add fitness class", add_class),
        "2": ("Register member for class", register_member_menu),
        "3": ("Record attendance", record_attendance),
        "4": ("View classes", view_classes),
        "5": ("View participants", view_participants),
        "6": ("Update class", update_class),
        "7": ("Delete class", delete_class),
        "8": ("Remove member from class", remove_member_from_class),
        "9": ("Participation & attendance report", attendance_report),
    }
    while True:
        print("\n--- Fitness Instructor ---")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("0. Logout")
        choice = input("Choose: ").strip()
        if choice == "0":
            return
        if choice in actions:
            actions[choice][1](user)
            v.pause()
        else:
            print("Invalid choice.")
