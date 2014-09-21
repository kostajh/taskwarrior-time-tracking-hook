from setuptools import setup, find_packages

setup(
    name='taskwarrior-hook-time-tracking',
    version='0.1',
    url='https://github.com/coddingtonbear/taskwarrior-hook-time-tracking',
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
            'taskw_timetracking = time_tracking_hook:main'
        ],
    },
)
