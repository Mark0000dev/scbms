"""
Centre Administrator module
Owner: Mark Bakulin (TP137767)
Files: facilities.txt (main), users.txt (staff accounts);
       reads members, bookings, classes, registrations for search and reports.
"""
from common import file_handler as fh
from common import validation as v

FACILITY_TYPES = ["Badminton Court", "Basketball Court", "Fitness Room", "Exercise Room"]
FACILITY_STATUSES = ["active", "maintenance", "closed"]
STAFF_ROLES = ["admin", "membership", "booking", "instructor"]
FACILITY_FIELDS = ["facility_id", "name", "type", "rate_per_hour", "status"]

SEARCH_TARGETS = {
    "Facilities": ("facilities", FACILITY_FIELDS),
    "Members": ("members", ["member_id", "name", "phone", "email", "plan", "expiry_date", "status"]),
    "Bookings": ("bookings", ["booking_id", "member_id", "facility_id", "date", "time_slot", "status"]),
    "Class registrations": ("registrations", ["reg_id", "class_id", "member_id", "reg_date", "attendance"]),
}


# ---------- helpers ----------
def ask_facility():
    """Show facilities, ask for an ID. Return (record, all_records) or (None, all_records)."""
    facilities = fh.read_records("facilities")
    v.print_table(facilities, FACILITY_FIELDS)
    if not facilities:
        return None, facilities
    facility_id = v.get_text("Facility ID: ").upper()
    for facility in facilities:
        if facility["facility_id"] == facility_id:
            return facility, facilities
    print("  Facility not found.")
    return None, facilities


# ---------- CREATE ----------
def add_facility():
    print("\n[Add facility]")
    name = v.get_text("Facility name: ")
    for facility in fh.read_records("facilities"):
        if facility["name"].lower() == name.lower():
            print("  A facility with this name already exists.")
            return
    facility_type = v.get_choice("Facility type: ", FACILITY_TYPES)
    rate = v.get_int("Rate per hour (RM): ", 1, 1000)

    new_facility = {
        "facility_id": fh.generate_id("facilities"),
        "name": name,
        "type": facility_type,
        "rate_per_hour": rate,
        "status": "active",
    }
    fh.append_record("facilities", new_facility)
    print(f"  Facility {new_facility['facility_id']} added.")


def add_staff_user():
    print("\n[Add staff account]")
    username = v.get_text("Username: ")
    for user in fh.read_records("users"):
        if user["username"].lower() == username.lower():
            print("  This username is already taken.")
            return
    password = v.get_text("Password: ")
    if len(password) < 6:
        print("  Password must be at least 6 characters.")
        return
    role = v.get_choice("Role: ", STAFF_ROLES)

    new_user = {
        "user_id": fh.generate_id("users"),
        "username": username,
        "password": password,
        "role": role,
        "linked_id": "-",
    }
    fh.append_record("users", new_user)
    print(f"  Account {new_user['user_id']} ({role}) created.")


# ---------- READ ----------
def view_facilities():
    print("\n[All facilities]")
    v.print_table(fh.read_records("facilities"), FACILITY_FIELDS)


def search_records():
    print("\n[Search records]")
    label = v.get_choice("Search in: ", list(SEARCH_TARGETS))
    file_name, fields = SEARCH_TARGETS[label]
    keyword = v.get_text("Keyword (ID, name, date, status...): ").lower()

    results = []
    for record in fh.read_records(file_name):
        for value in record.values():
            if keyword in value.lower():
                results.append(record)
                break
    print(f"\n  {len(results)} result(s) in {label}:")
    v.print_table(results, fields)


# ---------- UPDATE ----------
def update_facility():
    print("\n[Update facility]")
    facility, facilities = ask_facility()
    if facility is None:
        return

    field = v.get_choice("What to update: ", ["Name", "Rate per hour", "Status"])
    if field == "Name":
        facility["name"] = v.get_text("New name: ")
    elif field == "Rate per hour":
        facility["rate_per_hour"] = v.get_int("New rate per hour (RM): ", 1, 1000)
    else:
        facility["status"] = v.get_choice("New status: ", FACILITY_STATUSES)

    fh.write_records("facilities", facilities)
    print(f"  Facility {facility['facility_id']} updated.")


# ---------- DELETE ----------
def delete_facility():
    print("\n[Delete facility]")
    facility, facilities = ask_facility()
    if facility is None:
        return

    from modules import booking  # imported here to avoid circular imports
    if booking.has_active_bookings(facility_id=facility["facility_id"]):
        print("  Cannot delete: this facility has active bookings.")
        print("  Cancel the bookings first or set the status to 'closed'.")
        return
    if not v.confirm(f"Delete {facility['facility_id']} - {facility['name']}?"):
        print("  Cancelled.")
        return

    facilities.remove(facility)
    fh.write_records("facilities", facilities)
    print("  Facility deleted.")


# ---------- REPORT ----------
def usage_report():
    facilities = fh.read_records("facilities")
    bookings = fh.read_records("bookings")
    members = fh.read_records("members")
    classes = fh.read_records("classes")
    registrations = fh.read_records("registrations")
    today = v.today()

    print("\n========== CENTRE USAGE REPORT ==========")
    print(f"Date: {today}")

    # facility usage
    rows = []
    total_income = 0
    for facility in facilities:
        booked = cancelled = 0
        for b in bookings:
            if b["facility_id"] == facility["facility_id"]:
                if b["status"] == "booked":
                    booked += 1
                else:
                    cancelled += 1
        income = booked * int(facility["rate_per_hour"])
        total_income += income
        rows.append({"facility": facility["name"], "status": facility["status"],
                     "booked": booked, "cancelled": cancelled, "income_rm": income})
    print("\nFacility usage:")
    v.print_table(rows, ["facility", "status", "booked", "cancelled", "income_rm"])
    print(f"  Total bookings: {len(bookings)}   Expected income: RM {total_income}")

    # memberships (dates are YYYY-MM-DD, so string comparison works)
    active = expired = inactive = 0
    for m in members:
        if m["status"] != "active":
            inactive += 1
        elif m["expiry_date"] >= today:
            active += 1
        else:
            expired += 1
    print("\nMembership:")
    print(f"  Total members: {len(members)}")
    print(f"  Active: {active}   Expired: {expired}   Inactive: {inactive}")

    # classes
    present = sum(1 for r in registrations if r["attendance"] == "present")
    print("\nFitness classes:")
    print(f"  Classes: {len(classes)}   Registrations: {len(registrations)}   Attended: {present}")
    print("=========================================")


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
