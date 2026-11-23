"""
Member (self-service) module
Owner: Liyaqat Rafiq Lone (TP194752)
Works only with the logged-in member's own data: member_id = user["linked_id"].
REUSE functions from booking.py and fitness.py - don't copy their logic.
"""
from common import file_handler as fh
from common import validation as v
from modules import booking, fitness


def make_booking(member_id):
    """TODO: choose facility + date + slot -> booking.create_booking(member_id, ...)."""
    print("TODO: make_booking")


def register_class(member_id):
    """TODO: show classes -> fitness.register_member_for_class(member_id, class_id)."""
    print("TODO: register_class")


def view_facilities_and_classes(member_id):
    """TODO: show active facilities and classes (with free places)."""
    print("TODO: view_facilities_and_classes")


def update_my_booking(member_id):
    """TODO: only OWN upcoming bookings; new slot must pass booking.is_slot_available."""
    print("TODO: update_my_booking")


def update_contact(member_id):
    """TODO: change own phone / email in members.txt."""
    print("TODO: update_contact")


def cancel_my_booking(member_id):
    """TODO: only own upcoming bookings -> booking.cancel_booking."""
    print("TODO: cancel_my_booking")


def cancel_my_registration(member_id):
    """TODO: only own registrations -> fitness.remove_registration."""
    print("TODO: cancel_my_registration")


def my_history(member_id):
    """TODO: personal booking history + class history (with attendance)."""
    print("TODO: my_history")


def menu(user):
    member_id = user["linked_id"]
    actions = {
        "1": ("Book a facility", make_booking),
        "2": ("Register for a fitness class", register_class),
        "3": ("View facilities & classes", view_facilities_and_classes),
        "4": ("Update my booking", update_my_booking),
        "5": ("Update my contact details", update_contact),
        "6": ("Cancel my booking", cancel_my_booking),
        "7": ("Cancel class registration", cancel_my_registration),
        "8": ("My booking & class history", my_history),
    }
    while True:
        print(f"\n--- Member Area ({member_id}) ---")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("0. Logout")
        choice = input("Choose: ").strip()
        if choice == "0":
            return
        if choice in actions:
            actions[choice][1](member_id)
            v.pause()
        else:
            print("Invalid choice.")
