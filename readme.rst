Taskwarrior Time Tracking Hook
==============================

Ensure you have taskwarrior `2.4.x` or higher.


Install using pip::

    pip install taskwarrior-time-tracking-hook

And add it to your Taskwarrior hooks::

    mkdir -p ~/.task/hooks
    ln -s `which taskwarrior_time_tracking_hook` ~/.task/hooks/on-modify.timetracking

Add the ``totalactivetime`` user defined attribute configuration::

    task config uda.totalactivetime.type duration
    task config uda.totalactivetime.label Total active time
    task config uda.totalactivetime.values ''

Use ``task <TASK ID> start`` and ``task <TASK ID> stop`` to record when you have
started and stopped working on tasks.

Tracked time is stored in a task duration attribute named ``totalactivetime``
holding the total number of seconds that the task was active.

By default, this plugin allows you to have one task active at a time. You can
change this by setting `max_active_tasks` in `taskrc` to a value greater than 1.
