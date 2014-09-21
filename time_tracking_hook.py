#!/usr/bin/env python
import datetime
import json
import sys

TIME_FORMAT = '%Y%m%dT%H%M%SZ'
UDA_KEY = 'timetrackingseconds'


def main(stdin):
    lines = stdin.split('\n')
    original = json.loads(lines[0])
    modified = json.loads(lines[1])

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
