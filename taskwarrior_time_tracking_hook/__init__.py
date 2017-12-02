#!/usr/bin/env python
import datetime
import json
import re
import sys
import subprocess
from taskw import TaskWarrior

TIME_FORMAT = '%Y%m%dT%H%M%SZ'
UDA_KEY = 'totalactivetime'

w = TaskWarrior()
config = w.load_config()
if ('max_active_tasks' in config):
    MAX_ACTIVE = int(config['max_active_tasks'])
else:
    MAX_ACTIVE = 1

ISO8601DURATION = re.compile(
    "P((\d*)Y)?((\d*)M)?((\d*)D)?T((\d*)H)?((\d*)M)?((\d*)S)?")

# Convert duration string into a timedelta object.
# Valid formats for duration_str include
# - int (in seconds)
# - string ending in seconds e.g "123seconds"
# - ISO-8601: e.g. "PT1H10M31S"
def durationstrtotimedelta(duration_str):
    if (duration_str.startswith("P")):
        match = ISO8601DURATION.match(duration_str)
        if (match):
            year = match.group(2)
            month = match.group(4)
            day = match.group(6)
            hour = match.group(8)
            minute = match.group(10)
            second = match.group(12)
            value = 0
            if (second):
                value += int(second)
            if (minute):
                value += int(minute)*60
            if (hour):
                value += int(hour)*3600
            if (day):
                value += int(day)*3600*24
            if (month):
                # Assume a month is 30 days for now.
                value += int(month)*3600*24*30
            if (year):
                # Assume a month is 365 days for now.
                value += int(year)*3600*24*365
        else:
            value = int(duration_str)
    elif (duration_str.endswith("seconds")):
        value = int(duration_str.rstrip("seconds"))
    else:
        value = int(duration_str)
    return datetime.timedelta(seconds=value)

def main():
    original = json.loads(sys.stdin.readline())
    modified = json.loads(sys.stdin.readline())

    # An inactive task has just been started.
    if 'start' in modified and 'start' not in original:
        # Check if `task +ACTIVE count` is greater than MAX_ACTIVE. If so
        # prevent this task from starting.
        p = subprocess.Popen(
            ['task', '+ACTIVE', 'status:pending', 'count', 'rc.verbose:off'],
            stdout=subprocess.PIPE)
        out, err = p.communicate()
        count = int(out.rstrip())
        if count >= MAX_ACTIVE:
            print("Only %d task(s) can be active at a time. "
                  "See 'max_active_tasks' in .taskrc." % (MAX_ACTIVE))
            sys.exit(1)

    # An active task has just been stopped.
    if 'start' in original and 'start' not in modified:
        # Let's see how much time has elapsed
        start = datetime.datetime.strptime(original['start'], TIME_FORMAT)
        end = datetime.datetime.utcnow()

        if UDA_KEY not in modified:
            modified[UDA_KEY] = 0

        this_duration = (end - start)
        total_duration = (
            this_duration
            + durationstrtotimedelta(str(modified[UDA_KEY]))
        )
        print(
            "Total Time Tracked: %s (%s in this instance)" % (
                total_duration,
                this_duration,
            )
        )
        modified[UDA_KEY] = str(int(
            total_duration.days * (60 * 60 * 24) + total_duration.seconds
        )) + "seconds"

    return json.dumps(modified, separators=(',',':'))


def cmdline():
    sys.stdout.write(main())


if __name__ == '__main__':
    cmdline()
