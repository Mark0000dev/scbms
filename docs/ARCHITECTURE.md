# How the program works

## 1. Layers (who calls whom)

```
              ┌────────────────────────┐
              │  main.py + auth.py     │   login, open menu by role
              └───────────┬────────────┘
                          ▼
              ┌────────────────────────┐
              │  role module           │   business logic:
              │  (admin, membership,   │   rules, checks, reports
              │   booking, fitness,    │
              │   member)              │
              └─────┬────────────┬─────┘
           calls    │            │    calls
                    ▼            ▼
       ┌───────────────┐  ┌────────────────┐
       │ validation.py │  │ file_handler.py│
       │ user input /  │  │ read / save    │
       │ print tables  │  │ data/*.txt     │
       └───────────────┘  └────────────────┘
```

- **Modules** decide WHAT to do.
- **validation.py** talks to the USER (input / output).
- **file_handler.py** talks to the FILES (read / write).
- validation and file_handler don't know about each other.

## 2. Login

```
main.py → auth.login()
            ├─ ask username + password (input)
            ├─ search users.txt
            └─ return user {"role": "booking", ...}  or None after 3 tries
main.py → open menu for user["role"]
```

There is **no self-registration**:
- Admin creates staff accounts.
- Membership Officer registers members and creates their login.

## 3. How validation asks for data

Every `get_...` function = `input()` inside a loop:

```
   ┌──► input()
   │       │
   │   valid? ──yes──► return value
   │       │
   │      no
   └── print error
```

| Function | Checks |
|----------|--------|
| `get_text` | not empty, no `\|` |
| `get_int` | is a number, between min and max |
| `get_date` | format YYYY-MM-DD, not in the past (optional) |
| `get_choice` | number from the shown list |
| `confirm` | y / n |

validation checks **format** only.
**Business rules** (slot free? member exists? class full?) are checked in the module.

## 4. Example: one action step by step

Booking Officer → "Process booking":

```
booking.process_booking()
 ├─ validation.get_text("Member ID")            → "M001"
 ├─ file_handler.find_by_id("members", "M001")  → exists? active?
 ├─ validation.get_date("Date")                  → "2026-12-01"
 ├─ validation.get_choice("Slot", TIME_SLOTS)    → "10:00-11:00"
 ├─ is_slot_available(...)                       → reads bookings.txt
 ├─ file_handler.append_record("bookings", {...})  → saved
 └─ print("Booking B003 created")
```

## 5. Data files (tables linked by ID)

```
users.txt          U005|ali|ali123|member|M001 ─────┐
                                                    ▼
members.txt        M001|Ali Hassan|...|2027-01-10|active
                     ▲                    ▲
bookings.txt       B001|M001|F001|2026-12-01|10:00-11:00|booked
                               │
facilities.txt                 └─► F001|Badminton Court 1|...|active

registrations.txt  R001|C001|M001|2026-11-01|present
                         │
classes.txt              └─► C001|Morning Yoga|U004|Monday|08:00-09:00|10|active
```

One line = one record. Fields separated by `|`. Full field list: [DATA_FORMAT.md](DATA_FORMAT.md).
