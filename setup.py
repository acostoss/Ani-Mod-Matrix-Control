from distutils.core import setup
import py2exe

setup(
    zipfile = None,
    windows=[
        {
            'script':'ProjectorControl.py'
        }
    ],
)
