ECHO OFF
ECHO Creating Directories for geo-coding script...
@md %userprofile%\geo-coding\input
@type nul > %userprofile%\geo-coding\input\postcodes.csv
@md %userprofile%\geo-coding\output
pause
ECHO Complete... close the terminal to exit.