"""
Centre Administrator module
Owner: Mark Bakulin (TP137767)
Files: facilities.txt (main), users.txt, members.txt; reads bookings/classes/registrations for reports.
"""
from common import file_handler as fh
from common import validation as v

FACILITY_TYPES = ["Badminton Court", "Basketball Court", "Fitness Room", "Exercise Room"]
FACILITY_STATUSES = ["active", "maintenance", "closed"]


# ---------- CREATE ----------
def add_facility():
    """TODO: ask name, type (FACILITY_TYPES), rate per hour; status = active;
    id = fh.generate_id("facilities"); save with fh.append_record."""
    print("TODO: add_facility")


def add_staff_user():
    """TODO: create a login account in users.txt for staff (role: membership/booking/instructor).
    Username must be unique."""
    print("TODO: add_staff_user")


# ---------- READ ----------
def view_facilities():
    """TODO: show all facilities with v.print_table."""
    print("TODO: view_facilities")


def search_records():
    """TODO: search facilities / members / bookings / class registrations by keyword."""
    print("TODO: search_records")


# ---------- UPDATE ----------
def update_facility():
    """TODO: choose facility by id, change rate and/or status (FACILITY_STATUSES)."""
    print("TODO: update_facility")


# ---------- DELETE ----------
def delete_facility():
    """TODO: BLOCK delete if booking.has_active_bookings(facility_id=...) is True.
    Otherwise remove from list and fh.write_records."""
    print("TODO: delete_facility")


# ---------- REPORT ----------
def usage_report():
    """TODO: overall centre usage: bookings per facility, total members (active/expired),
    number of classes and registrations."""
    print("TODO: usage_report")


def menu(user):
    actions = {
        "1": ("Add facility", add_facility),
        "2": ("Add staff account", add_staff_user),
        "3": ("View facilities", view_facilities),
        "4": ("Search records", search_records),
        "5": ("Update facility", update_facility),
        "6": ("Delete facility", delete_facility),
        "7": ("Centre usage & membership report", usage_report),
    }
    while True:
        print("\n--- Centre Administrator ---")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("0. Logout")
        choice = input("Choose: ").strip()
        if choice == "0":
            return
        if choice in actions:
            actions[choice][1]()
            v.pause()
        else:
            print("Invalid choice.")
