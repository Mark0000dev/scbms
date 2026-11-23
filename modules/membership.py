"""
Membership Officer module
Owner: Arazmyrat Atajykov (TP190160)
Files: members.txt (main), users.txt (member login accounts).
"""
from common import file_handler as fh
from common import validation as v

PLANS = {"Monthly": 30, "Quarterly": 90, "Yearly": 365}  # plan -> days


# ---------- INTERFACE (other modules call these - implement FIRST, don't rename) ----------
def is_membership_active(member_id):
    """Return True if member exists, status == 'active' and expiry_date >= today.
    Used by booking.py, fitness.py, member.py (Membership expiry validation)."""
    # TODO: real check. Temporary: any existing member is active.
    return fh.find_by_id("members", member_id) is not None


# ---------- CREATE ----------
def register_member():
    """TODO: ask name, phone, email, plan (PLANS). start_date = today,
    expiry_date = start + PLANS[plan] days, status = active.
    Also create login in users.txt (role 'member', linked_id = member_id)."""
    print("TODO: register_member")


# ---------- READ ----------
def view_members():
    print("TODO: view_members")


def search_member():
    """TODO: search by id / name / phone."""
    print("TODO: search_member")


# ---------- UPDATE ----------
def update_member():
    """TODO: change phone / email / plan."""
    print("TODO: update_member")


def renew_membership():
    """TODO: extend expiry_date by plan days (from max(today, old expiry)), status = active."""
    print("TODO: renew_membership")


# ---------- DELETE ----------
def deactivate_member():
    """TODO: BLOCK if booking.has_active_bookings(member_id=...) is True.
    Otherwise set status = 'inactive' (or delete record)."""
    print("TODO: deactivate_member")


# ---------- REPORT ----------
def membership_report():
    """TODO: list active members, expired members, and members expiring in next 7 days."""
    print("TODO: membership_report")


def menu(user):
    actions = {
        "1": ("Register new member", register_member),
        "2": ("View members", view_members),
        "3": ("Search member", search_member),
        "4": ("Update member info", update_member),
        "5": ("Renew membership", renew_membership),
        "6": ("Deactivate / delete member", deactivate_member),
        "7": ("Active & expiring membership report", membership_report),
    }
    while True:
        print("\n--- Membership Officer ---")
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
