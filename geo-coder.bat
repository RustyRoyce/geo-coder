ECHO OFF
ECHO Creating Directories for geo-coding script...
@md %userprofile%\geo-coder\input
@type nul > %userprofile%\geo-coder\input\postcodes.csv
@md %userprofile%\geo-coder\output
pause
ECHO Complete... close the terminal to exit.