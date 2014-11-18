from icalendar import Calendar, Event, vDDDTypes
from datetime import date

# Define the date of the race in the input calendar
INPUT_RACE_DATE = date(2015,04,26)

# Define the date of the new race
NEW_RACE_DATE = date(2015,04,26)

# Calculate the adjustment needed to the dates
DT_DELTA = NEW_RACE_DATE - INPUT_RACE_DATE 


def date_add(dt, delta=DT_DELTA):
    if not isinstance(dt, date):
        raise ValueError('Value passed must be an object of type date')
    return dt + delta

f = open('./input.ics', 'rb')
gcal = Calendar.from_ical(f.read())

for component in gcal.walk():
    if component.name == 'VEVENT':
        component['dtstart'] = vDDDTypes(date_add(component.get('dtstart').dt))
        component['dtend'] = vDDDTypes(date_add(component.get('dtend').dt))

f.close()

f = open('./race-cal-' + NEW_RACE_DATE.strftime('%Y%m%d') + '.ics', 'wb')
f.write(gcal.to_ical())
f.close()

