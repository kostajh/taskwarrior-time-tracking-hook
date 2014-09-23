#!/usr/bin/env python
import datetime
import json
import sys
import subprocess
from taskw import TaskWarrior

TIME_FORMAT = '%Y%m%dT%H%M%SZ'
UDA_KEY = 'timetrackingseconds'

w = TaskWarrior()
config = w.load_config()
if ('max_active_tasks' in config):
    MAX_ACTIVE = int(config['max_active_tasks'])
else:
    MAX_ACTIVE = 1


def main(stdin):
    lines = stdin.split('\n')
    original = json.loads(lines[0])
    modified = json.loads(lines[1])

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
        sys.exit(0)

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
            + datetime.timedelta(seconds=int(modified[UDA_KEY]))
        )
        print(
            "Total Time Tracked: %s (%s in this instance)" % (
                total_duration,
                this_duration,
            )
        )
        modified[UDA_KEY] = str(int(
            total_duration.days * (60 * 60 * 24) + total_duration.seconds
        ))

    return json.dumps(modified)


def cmdline():
    sys.stdout.write(main(sys.stdin.read()))


if __name__ == '__main__':
    cmdline()
