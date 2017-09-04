from setuptools import setup, find_packages
from codecs import open
from os import path
import sys

appversion = "0.0.8-07"

here = path.abspath(path.dirname(__file__))

with open(here + '/encry_dl/__init__.py', 'w') as initpy:
    initpy.write('__version__ = "{}"'.format(appversion))

setup(
    
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Sound/Audio',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
        'requests',
        'unicode-slugify',
        'mock',
        'chardet',
    ],
    entry_points={
        'console_scripts': [
            'encryp=faus_dl.__main__:main',
        ],
    },
)
