Taskwarrior Time Tracking Hook
==============================

Ensure you have taskwarrior `2.4.x` or higher.

Install
+++++++

Install using pip::

    pip install taskwarrior-time-tracking-hook

And add it to your Taskwarrior hooks::

    mkdir -p ~/.task/hooks
    ln -s `which taskwarrior_time_tracking_hook` ~/.task/hooks/on-modify.timetracking

Add the ``totalactivetime`` user defined attribute configuration::

    task config uda.totalactivetime.type duration
    task config uda.totalactivetime.label Total active time
    task config uda.totalactivetime.values ''
    
Add to reports (replace list with whichever report type you want to modify)::

    task show report.list.labels
        ID,Active,Age,...,Urg
    task show report.list.columns
        id,start.age,entry.age,...,urgency
    
    task config report.list.labels 'ID,Active,Age,Time Spent,...,Urg'
    task config report.list.labels 'id,start.age,entry.age,totalactivetime,...,urgency'

Usage
+++++

Use ``task <TASK ID> start`` and ``task <TASK ID> stop`` to record when you have
started and stopped working on tasks.

Tracked time is stored in a task duration attribute named ``totalactivetime``
holding the total number of seconds that the task was active.

By default, this plugin allows you to have one task active at a time. You can
change this by setting `max_active_tasks` in `taskrc` to a value greater than 1.

Un-install
++++++++++

Delete the hook::

    rm ~/.task/hooks/on-modify.timetracking
    
Remove the User Defined Attribute (UDA) configuration::

    task config uda.totalactivetime.values
    task config uda.totalactivetime.label
    task config uda.totalactivetime.type

Remove the Python program::

    pip uninstall taskwarrior-time-tracking-hook
