# geo-coder
 import postcodes in CSV, exports postcodes + coords in .csv
 
tested with:
requests==2.27.1
Python 3.10.1

Setup for Windows:
Run the geo-coding.bat file, this will create the following directories
%userprofile%\geo-coding\input
%userprofile%\geo-coding\output
and the following file:
%userprofile%\geo-coding\input\postcodes.csv

Install the requests library for Python if not already installed.
pip install requests

Setup for Linux:
The geo-coding.py file uses the pathlib library and therefore is able to use both Linux and Windows file structures, however, there is no script to create the directories.
Therefore, the directories must be created manually in the users home directory - $home
i.e 
$home/geo-coder/input
$home/geo-coder/output

How to run:
open the postcodes.csv file and in cell A1, enter a heading of "postcode".
Enter postcodes to geo-code in the cells below column A.

run the python script.

information will be output to %userprofile%\geo-coding\output\\{timestamp}--postcodes-and-coordinates.csv
