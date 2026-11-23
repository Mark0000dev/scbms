"""
Booking Officer module
Owner: Vepa Garayev (TP194657)
Files: bookings.txt (main); reads facilities.txt, members.txt.
"""
from common import file_handler as fh
from common import validation as v


# ---------- INTERFACE (other modules call these - implement FIRST, don't rename) ----------
def is_slot_available(facility_id, date, time_slot):
    """Return True if there is NO booking with status 'booked' for the same
    facility + date + time_slot, and the facility status is 'active'.
    (Automatic availability checking + double-booking prevention.)"""
    # TODO: real check
    return True


def has_active_bookings(member_id=None, facility_id=None):
    """Return True if there is any 'booked' booking (date >= today) for this member or facility.
    Used by admin.delete_facility and membership.deactivate_member."""
    # TODO: real check
    return False


def create_booking(member_id, facility_id, date, time_slot):
    """Validate (membership active, slot available), save, return booking_id or None.
    Used by this module AND member.py - don't duplicate the logic there."""
    # TODO
    print("TODO: create_booking")
    return None


def cancel_booking(booking_id):
    """Set status = 'cancelled' (frees the time slot). Return True/False.
    Used by this module AND member.py."""
    # TODO
    print("TODO: cancel_booking")
    return False


# ---------- MENU ACTIONS ----------
def process_booking():
    """TODO: ask member id, facility, date (no past), time slot (v.TIME_SLOTS) -> create_booking."""
    print("TODO: process_booking")


def view_availability():
    """TODO: for a facility + date show every slot in v.TIME_SLOTS as FREE / BOOKED."""
    print("TODO: view_availability")


def search_bookings():
    """TODO: search by member id / facility / date."""
    print("TODO: search_bookings")


def update_booking():
    """TODO: change date / time slot - new slot must pass is_slot_available."""
    print("TODO: update_booking")


def cancel_booking_menu():
    print("TODO: cancel_booking_menu -> cancel_booking(booking_id)")


def booking_report():
    """TODO: bookings grouped by facility and by date (counts)."""
    print("TODO: booking_report")


def menu(user):
    actions = {
        "1": ("Process facility booking", process_booking),
        "2": ("View facility availability", view_availability),
        "3": ("Search bookings", search_bookings),
        "4": ("Update booking", update_booking),
        "5": ("Cancel booking", cancel_booking_menu),
        "6": ("Booking report (facility / date)", booking_report),
    }
    while True:
        print("\n--- Booking Officer ---")
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
