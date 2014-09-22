from setuptools import setup, find_packages

setup(
    name='taskwarrior-time-tracking-hook',
    version='0.1.1',
    url='https://github.com/coddingtonbear/taskwarrior-time-tracking-hook',
    description=(
        'Track your time in a UDA in taskwarrior'
    ),
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'taskwarrior_timetracking_hook = taskwarrior_time_tracking_hook:cmdline'
        ],
    },
)
