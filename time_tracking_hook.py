#!/usr/bin/env python
import datetime
import json
import sys

TIME_FORMAT = '%Y-%m-%dT%H%M%SZ'
UDA_KEY = 'timetrackingseconds'


def main(stdin):
    lines = stdin.split('\n')
    original = json.loads(lines[0])
    modified = json.loads(lines[0])

    if 'end' in modified and 'end' not in original:
        # Let's see how much time has elapsed
        start = datetime.datetime.strptime(modified['start'], TIME_FORMAT)
        end = datetime.datetime.strptime(modified['end'], TIME_FORMAT)

        if UDA_KEY not in modified:
            modified[UDA_KEY] = 0

        total_duration = (
            (end - start)
            + datetime.timedelta(seconds=modified[UDA_KEY])
        )
        modified[UDA_KEY] = (
            total_duration.days * (3600 * 24) + total_duration.seconds
        )

    return json.dumps(modified)


def cmdline():
    sys.stdout.write(main(sys.stdin.read()))


if __name__ == '__main__':
    cmdline()
