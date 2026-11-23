"""
Shared file layer. EVERYONE uses these functions - nobody opens data files directly.

Records are stored one per line, fields separated by "|".
In Python a record is a dict: {"facility_id": "F001", "name": "Court A", ...}
Field order for every file is defined in FIELDS below.

Owner: Mark (Team lead). Ask before changing a function signature.
"""
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
SEP = "|"

FIELDS = {
    "users":         ["user_id", "username", "password", "role", "linked_id"],
    "facilities":    ["facility_id", "name", "type", "rate_per_hour", "status"],
    "members":       ["member_id", "name", "phone", "email", "plan", "start_date", "expiry_date", "status"],
    "bookings":      ["booking_id", "member_id", "facility_id", "date", "time_slot", "status"],
    "classes":       ["class_id", "name", "instructor_id", "day", "time_slot", "capacity", "status"],
    "registrations": ["reg_id", "class_id", "member_id", "reg_date", "attendance"],
}

ID_PREFIX = {
    "users": "U", "facilities": "F", "members": "M",
    "bookings": "B", "classes": "C", "registrations": "R",
}


def _path(name):
    return os.path.join(DATA_DIR, name + ".txt")


def read_records(name):
    """Return all records of a file as a list of dicts. Missing file -> []."""
    fields = FIELDS[name]
    records = []
    if not os.path.exists(_path(name)):
        return records
    with open(_path(name), "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            values = line.split(SEP)
            if len(values) != len(fields):
                continue  # skip broken lines instead of crashing
            records.append(dict(zip(fields, values)))
    return records


def write_records(name, records):
    """Overwrite the whole file with the given list of dicts (used for update/delete)."""
    fields = FIELDS[name]
    with open(_path(name), "w", encoding="utf-8") as f:
        for rec in records:
            f.write(SEP.join(str(rec[k]).replace(SEP, "/") for k in fields) + "\n")


def append_record(name, record):
    """Add one new record to the end of the file (used for create)."""
    fields = FIELDS[name]
    with open(_path(name), "a", encoding="utf-8") as f:
        f.write(SEP.join(str(record[k]).replace(SEP, "/") for k in fields) + "\n")


def find_by_id(name, record_id):
    """Return the record whose first field equals record_id, or None."""
    id_field = FIELDS[name][0]
    for rec in read_records(name):
        if rec[id_field] == record_id:
            return rec
    return None


def generate_id(name):
    """Next ID for a file, e.g. F001 -> F002."""
    prefix = ID_PREFIX[name]
    id_field = FIELDS[name][0]
    biggest = 0
    for rec in read_records(name):
        number = rec[id_field][len(prefix):]
        if number.isdigit():
            biggest = max(biggest, int(number))
    return f"{prefix}{biggest + 1:03d}"
