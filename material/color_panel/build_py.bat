@echo off

set /p var=Please Enter UI file name:
echo %var%
pyuic5 -x %var% -o UI.py

echo UI.py is generated!
pause