#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io
import re
import os
import sys


def readme():
    with io.open("README.md", "r", encoding="utf-8") as my_file:
        return my_file.read()

setup(
    name='django-starterkit',
    version='1.0.4',
    url='https://github.com/mikasoftware/django-starterkit',
    license='BSD 3-Clause License',
    description="Library with reusable code for every django project you work with.",
    long_description=readme(),
    author='Bartlomiej Mika',
    author_email='bart@mikasoftware.com',
    packages=find_packages(),
    install_requires=[
        'django>=2.0',
        'djangorestframework>=3.7.7'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities'
    ],
    keywords='library starter helper',
)
