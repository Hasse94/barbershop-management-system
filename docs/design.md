# Domain Design

## AppointmentStatus (Enum)
- Values: SCHEDULED, COMPLETED, CANCELLED, NO_SHOW

## Service
- Attributes: id, name, price, duration_minutes, is_active
- Methods: update_price(new_price), deactivate()
- Private: _price (never negative), _is_active
- Belongs to: BarberShop's service catalogue

## Barber
- Attributes: id, name, phone, is_active
- Methods: deactivate(), activate()
- Private: _is_active (only changes through methods)
- Belongs to: BarberShop. Referenced by Appointments.
- Note: does NOT store its own appointment list (BarberShop is the single source of truth)

## Customer
- Attributes: id, name, phone, email
- Methods: update_contact(phone, email)
- Private: _phone, _email (validated inside update_contact)
- Belongs to: BarberShop. Referenced by Appointments.

## AppointmentItem
- Attributes: service, price, duration_minutes
- Purpose: a snapshot of the service's price and duration at booking time
- Belongs to: one Appointment

## Appointment
- Attributes: id, customer, barber, items, start_time, status, tip
- Calculated (not stored): end_time, total_price, total_duration
- Methods: complete(tip), cancel(), mark_no_show()
- Private: _status, _tip, _items
- Rules:
  - Status can only change from SCHEDULED; final states never change
  - Tip can only be added when completing, and must be >= 0
- Contains: Customer, Barber, list of AppointmentItems (composition)

## BarberShop
- Attributes: name, _barbers, _customers, _services, _appointments
- Methods:
  - add_barber(), remove_barber(barber_id)          → soft delete
  - register_customer()
  - add_service(), update_service_price(), remove_service()
  - book_appointment(customer_id, barber_id, service_ids, start_time)
  - complete_appointment(id, tip), cancel_appointment(id)
  - get_appointments(status=None)                    → track completed/cancelled
  - calculate_earnings(barber_id, start, end)        → revenue and tips separately
- Private: all four collections, so nothing gets added without going through the checks
- Booking rules: barber and services must be active, no time in the past, no overlap with the barber's other appointments
- Contains: everything