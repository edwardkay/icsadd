icsadd
======

Quick script to increment all events in an ICS calendar file by a set number of days

## Purpose

I run marathons and like to use a Google calendar to manage my training schedules.

I now store these training calendars in [ICS format](http://en.wikipedia.org/wiki/ICalendar). When a new race comes along, I want to be able to quickly update the dates of the training runs so they're correctly set up for the new race day.

## Usage

As a quick script there's no pretty UI. Simply edit the file to define:

- the race date (last entry) in the input file
- the new race date (to calculate the date difference)
- the input filename

iCal proceesing is handled using [icalendar](https://github.com/collective/icalendar). Install this using `pip install -r requirements.txt`.

Then simply run `python icsadd.py` and a new ICS/iCal file will be created with the date of all events incremented by the defined amount.
