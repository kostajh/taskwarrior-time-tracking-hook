Taskwarrior Time Tracking Hook
==============================


Install using pip::

    pip install taskwarrior-time-tracking-hook

And add it to your Taskwarrior hooks::

    mkdir -p ~/.task/hooks
    ln -s `which taskwarrior_timetracking_hook` ~/.task/hooks/on-modify.timetracking

Use ``task <TASK ID> start`` and ``task <TASK ID> stop`` to record when you have
started and stopped working on tasks.

Tracked time is stored in a task attribute named ``timetrackingseconds`` holding
the total number of seconds that the task was active.
