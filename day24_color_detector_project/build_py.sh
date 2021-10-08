#!/bin/bash
# Ask the user
echo Please Enter UI file name:
read var
pyuic5 -x $var -o UI.py

