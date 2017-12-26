#!/bin/bash
#----------------------------------------------------------------------------------------------#
# Script used to build our library and submit it to `PyPi`.                                    #
# https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi #
#----------------------------------------------------------------------------------------------#

# DEVELOPERS NOTE:
# Be sure you have installed the following libraries...
# - pip install twine
# - pip install wheel

# Delete previously created files.
rm -rf build
rm -rf dist
rm -rf django_trapdoor.egg-info

# Minimally, you should create a Source Distribution:
python setup.py sdist

# A wheel is a built package that can be installed without needing to go through the “build” process.
# Installing wheels is substantially faster for the end user than installing from a source distribution.
python setup.py bdist_wheel

# Submit to 'PyPi' distribution service.
twine upload dist/*
