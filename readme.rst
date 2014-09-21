Taskwarrior Time Tracking Hook
==============================


.. note::

   Currently this hook does not work as it appears that Taskwarrior does
   not execute ``on-modify`` hooks when "stop"-ing a task.


Install using pip::

    pip install taskwarrior-hook-time-tracking

And add it to your Taskwarrior hooks::

    mkdir -p ~/.task/hooks
    ln -s `which taskwarrior_timetracking` ~/.task/hooks/on-modify.timetracking
