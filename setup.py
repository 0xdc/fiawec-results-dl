#!/usr/bin/env python

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as requirements:
    REQUIREMENTS = requirements.read().split("\n")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='fiawec-results-dl',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Script to download timing data for official FIA WEC sessions.',
    long_description=README,
    url='https://github.com/0xdc/fiawec-results-dl',
    author='Daniel Cordero',
    author_email='fiawec-results-dl@0xdc.io',
    entry_points = {
            'console_scripts': ['fiawec-results-dl=fiawec.__main__:main'],
    },
    install_requires=REQUIREMENTS,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
