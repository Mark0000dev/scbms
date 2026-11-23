# Task distribution

Every member writes **their own module**: full CRUD + report for their role, input validation,
and their part of the documentation (pseudocode / flowchart, screenshots of sample runs).

**Rules for everyone**
- Read/write data ONLY through `common/file_handler.py` (`read_records`, `write_records`, `append_record`, `find_by_id`, `generate_id`).
- Use `common/validation.py` for input (`get_text`, `get_int`, `get_date`, `get_choice`, `confirm`, `print_table`).
- **Interface functions** (marked `INTERFACE` in the code) are used by other teammates → implement them FIRST (week 1) and never rename them or change their parameters.
- To call another teammate's module, import it **inside the function** to avoid circular imports:
  ```python
  def deactivate_member():
      from modules import booking
      if booking.has_active_bookings(member_id=mid): ...
  ```
- The program must never crash on bad input. Test every option with wrong values.

---

## 1. Mark Bakulin — Centre Administrator + Team lead
File: `modules/admin.py` (+ owns `main.py`, `common/`)

| Type | Task |
|------|------|
| Create | Add facility; add staff login accounts |
| Read | View facilities; search facilities, members, bookings, class registrations |
| Update | Update facility details (rate, status) |
| Delete | Delete facility — **blocked** if `booking.has_active_bookings(facility_id=...)` |
| Report | Overall centre usage: bookings per facility, active/expired members, classes & registrations |

Lead duties: create GitHub repo, add teammates as collaborators, review & merge Pull Requests, maintain `common/`, final integration test.

## 2. Maxim Kalinin — Fitness Instructor
File: `modules/fitness.py` · Data: `classes.txt`, `registrations.txt`

| Type | Task |
|------|------|
| Interface | `count_registered(class_id)`, `register_member_for_class(member_id, class_id)`, `remove_registration(reg_id)` |
| Create | Add class; register member for class; record attendance |
| Read | View classes (with `registered / capacity`), view participants |
| Update | Update schedule / capacity (capacity can't go below current registrations); update attendance |
| Delete | Delete class — **blocked** if members registered; remove a member's registration |
| Report | Class participation & attendance (registered / present / absent / %) |

Unique feature: **class capacity checking**. Registration also requires `membership.is_membership_active`.

## 3. Vepa Garayev — Booking Officer
File: `modules/booking.py` · Data: `bookings.txt`

| Type | Task |
|------|------|
| Interface | `is_slot_available(...)`, `has_active_bookings(...)`, `create_booking(...)`, `cancel_booking(...)` |
| Create | Process booking (no past dates, member must be active, slot must be free) |
| Read | View availability of a facility for a date (all slots FREE/BOOKED); search bookings |
| Update | Change date / time slot (new slot must be free) |
| Delete | Cancel booking → status `cancelled`, slot becomes free |
| Report | Bookings by facility and by date |

Unique features: **automatic availability checking**, **double booking prevention**.

## 4. Arazmyrat Atajykov — Membership Officer
File: `modules/membership.py` · Data: `members.txt` (+ member accounts in `users.txt`)

| Type | Task |
|------|------|
| Interface | `is_membership_active(member_id)` |
| Create | Register member (calculate expiry from plan) + create login (role `member`) |
| Read | View / search members |
| Update | Update member info; renew membership (extend expiry) |
| Delete | Deactivate / delete — **blocked** if `booking.has_active_bookings(member_id=...)` |
| Report | Active members, expired members, expiring within 7 days |

Unique feature: **membership expiry validation**.

## 5. Liyaqat Rafiq Lone — Member
File: `modules/member.py` · Works only with own data (`user["linked_id"]`)

| Type | Task |
|------|------|
| Create | Book a facility (via `booking.create_booking`); register for class (via `fitness.register_member_for_class`) |
| Read | View available facilities and classes (free places) |
| Update | Update own upcoming booking; update own phone / email |
| Delete | Cancel own booking; cancel own class registration |
| Report | Personal booking & class history |

Must **reuse** Vepa's and Maxim's interface functions — no copied logic. A member must not see or change other members' data.

---

## Timeline (adjust to your deadline)

| Week | Goal |
|------|------|
| 1 | Repo set up, everyone runs `main.py`. **Interface functions done** (Vepa, Maxim, Arazmyrat). |
| 2 | All CRUD options of own module working. |
| 3 | Reports, validation, edge cases; merge everything into `main`. |
| 4 | Full integration test with all roles, documentation & screenshots, final submission. |

## Definition of done (per module)
- [ ] All menu options work, no "TODO" left
- [ ] Wrong input handled (letters instead of numbers, past dates, unknown IDs)
- [ ] Business rules enforced (blocked deletes, capacity, double booking, expiry)
- [ ] Pushed via Pull Request and merged into `main`
- [ ] Pseudocode/flowchart + screenshots added to the report
