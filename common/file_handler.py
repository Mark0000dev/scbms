# Read and save data in .txt files.
# One line = one record, fields separated by "|".
# Run the program from the scbms folder:  python main.py

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


def read_records(name):
    # returns a list of dicts
    records = []
    file = open("data/" + name + ".txt", "r")
    for line in file:
        line = line.strip()
        if line != "":
            values = line.split("|")
            record = dict(zip(FIELDS[name], values))
            records.append(record)
    file.close()
    return records


def write_records(name, records):
    # overwrite the whole file (used for update and delete)
    file = open("data/" + name + ".txt", "w")
    for record in records:
        values = []
        for field in FIELDS[name]:
            values.append(str(record[field]))
        file.write("|".join(values) + "\n")
    file.close()


def append_record(name, record):
    # add one record to the end of the file (used for create)
    values = []
    for field in FIELDS[name]:
        values.append(str(record[field]))
    file = open("data/" + name + ".txt", "a")
    file.write("|".join(values) + "\n")
    file.close()


def find_by_id(name, record_id):
    # returns the record or None
    id_field = FIELDS[name][0]
    for record in read_records(name):
        if record[id_field] == record_id:
            return record
    return None


def generate_id(name):
    # next ID after the last record, e.g. F004 -> F005
    records = read_records(name)
    prefix = ID_PREFIX[name]
    if len(records) == 0:
        return prefix + "001"
    last_id = records[-1][FIELDS[name][0]]
    number = int(last_id[1:]) + 1
    return prefix + str(number).zfill(3)
