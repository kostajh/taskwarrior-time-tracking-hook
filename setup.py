from setuptools import setup, find_packages

setup(
    name='taskwarrior-time-tracking-hook',
    version='0.1.4',
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
    install_requires=[
        "taskw"
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'taskwarrior_time_tracking_hook = taskwarrior_time_tracking_hook:cmdline'
        ],
    },
)
