"""
Boolean expressions evaluate to either ``True`` or ``False``.  Python's
Boolean operators are ``and``, ``or``, and ``not``.
"""

# and: True only when both conditions are true.
has_ticket = True
is_old_enough = True
can_enter = has_ticket and is_old_enough
print(can_enter)  # True

# or: True when at least one condition is true.
is_weekend = False
is_holiday = True
day_off = is_weekend or is_holiday
print(day_off)  # True

# not: reverses a Boolean value.
is_raining = False
can_play_outside = not is_raining
print(can_play_outside)  # True
