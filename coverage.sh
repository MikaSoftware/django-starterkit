#!/bin/bash
# Script will run the unit tests and keep output our code coverage. Please ensure "coverage" is installed before running this script.
clear
coverage run --source=starterkit manage.py test
coverage report -m
coverage report -m > coverage.txt
