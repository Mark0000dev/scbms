# ActiveLife Sports Centre – Booking Management System (SCBMS)

PWP 102026 · Lab 40 · Group 02 · Case Study 2

Menu-driven Python program for managing facilities, memberships, facility bookings and fitness classes.
Data is stored in plain text files (`data/*.txt`, one record per line, fields separated by `|`).

## Team

| # | Name | TP | Role | File |
|---|------|----|------|------|
| 1 | Mark Bakulin (Team lead) | TP137767 | Centre Administrator | `modules/admin.py` + `common/`, `main.py` |
| 2 | Maxim Kalinin | TP082468 | Fitness Instructor | `modules/fitness.py` |
| 3 | Vepa Garayev | TP194657 | Booking Officer | `modules/booking.py` |
| 4 | Arazmyrat Atajykov | TP190160 | Membership Officer | `modules/membership.py` |
| 5 | Liyaqat Rafiq Lone | TP194752 | Member | `modules/member.py` |

## Run

Python 3.10+, no external libraries.

```
cd scbms
python main.py
```

Test logins (from `data/users.txt`):

| Role | Username | Password |
|------|----------|----------|
| Administrator | admin | admin123 |
| Membership Officer | membership | mem123 |
| Booking Officer | booking | book123 |
| Fitness Instructor | instructor | fit123 |
| Member | ali | ali123 |

## Structure

```
scbms/
├── main.py              # login + role menu dispatch
├── common/
│   ├── file_handler.py  # read/write/append/find/generate_id  (ONLY way to touch data files)
│   ├── validation.py    # input helpers, TIME_SLOTS, print_table
│   └── auth.py          # login
├── modules/
│   ├── admin.py         # Centre Administrator
│   ├── membership.py    # Membership Officer
│   ├── booking.py       # Booking Officer
│   ├── fitness.py       # Fitness Instructor
│   └── member.py        # Member
└── data/                # *.txt data files with sample records
```

## Unique features → where they live

| Feature | Function |
|---------|----------|
| Automatic facility availability checking | `booking.is_slot_available` |
| Prevention of double booking | `booking.is_slot_available` (called in `create_booking`) |
| Membership expiry validation | `membership.is_membership_active` |
| Fitness class capacity checking | `fitness.register_member_for_class` + `count_registered` |

## Git workflow

1. `git pull` before you start.
2. Work on your own branch: `git checkout -b feature/booking`.
3. Edit **only your own module**. Changes to `common/` → ask Mark.
4. Commit often with clear messages: `git commit -m "booking: add double booking check"`.
5. `git push -u origin feature/booking` → open a Pull Request into `main` → Mark reviews and merges.
