# Data files

All files are in `data/`, one record per line, fields separated by `|`, no header line.
Field order is defined in `common/file_handler.py → FIELDS`. Dates are `YYYY-MM-DD`.
Time slots are one-hour blocks from `validation.TIME_SLOTS` (`08:00-09:00` … `21:00-22:00`).

| File | Fields | Owner |
|------|--------|-------|
| `users.txt` | user_id \| username \| password \| role \| linked_id | Mark (staff), Arazmyrat (members) |
| `facilities.txt` | facility_id \| name \| type \| rate_per_hour \| status | Mark |
| `members.txt` | member_id \| name \| phone \| email \| plan \| start_date \| expiry_date \| status | Arazmyrat |
| `bookings.txt` | booking_id \| member_id \| facility_id \| date \| time_slot \| status | Vepa |
| `classes.txt` | class_id \| name \| instructor_id \| day \| time_slot \| capacity \| status | Maxim |
| `registrations.txt` | reg_id \| class_id \| member_id \| reg_date \| attendance | Maxim |

## Allowed values

- `users.role`: `admin`, `membership`, `booking`, `instructor`, `member`
- `users.linked_id`: member_id for role `member`, otherwise `-`
- `facilities.status`: `active`, `maintenance`, `closed`
- `members.plan`: `Monthly` (30 days), `Quarterly` (90), `Yearly` (365)
- `members.status`: `active`, `inactive`
- `bookings.status`: `booked`, `cancelled`
- `classes.status`: `active`, `cancelled`
- `registrations.attendance`: `pending`, `present`, `absent`

## ID prefixes

`U001` users · `F001` facilities · `M001` members · `B001` bookings · `C001` classes · `R001` registrations
Always create IDs with `fh.generate_id("<file>")`.

## Example (how to work with a file)

```python
from common import file_handler as fh

records = fh.read_records("facilities")        # list of dicts
for r in records:
    if r["facility_id"] == "F002":
        r["status"] = "maintenance"
fh.write_records("facilities", records)          # save whole list back
```
