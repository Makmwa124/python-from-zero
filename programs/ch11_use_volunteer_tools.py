# programs/ch11_use_volunteer_tools.py
"""Use the volunteer tools module."""
from ch11_volunteer_tools import OPEN_DAYS, is_open_day

print("Sunny Paws is open:", ", ".join(OPEN_DAYS))
for day in ["Mon", "Tue", "Sun"]:
    if is_open_day(day):
        print(f"{day}: open, volunteers needed")
    else:
        print(f"{day}: closed")
