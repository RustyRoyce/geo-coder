# GEO-CODER

Transform postcodes to postcodes with longitude & latitude co-ordinates in .CSV format

## Description

Transform postcodes to postcodes with longitude & latitude co-ordinates in .CSV format.
This script uses the postcodes.io API - https://api.postcodes.io which requires no authorisation/access token.

The postcodes API is only applicable for locations based in the United Kingdom.

## Getting Started

### Dependencies

tested with:
* requests==2.27.1
* Python 3.10.1

Check if requests module is installed by running commands in terminal:

```
pip freeze
```

if not present, install using PIP:

```
pip install requests
```



### Installing for Windows

Run the geo-coding.bat file, this will create the following directories
%userprofile%\geo-coding\input
%userprofile%\geo-coding\output
and the following file:
%userprofile%\geo-coding\input\postcodes.csv

### Installing for Linux

Setup for Linux:
The geo-coding.py file uses the pathlib library and therefore is able to use both Linux and Windows file structures, however, there is no script to create the directories.
Therefore, the directories must be created manually in the users home directory - $home
i.e 
$home/geo-coder/input
$home/geo-coder/output

### Executing program

* Open postcodes.csv file created in earlier Installation step.
* Add field "postcode" in first column - the script looks for this exact string.
* Add postcodes to be geo-coded in cells below postcode heading.
* Open your terminal (CMD, Powershell, etc)
* Run Python and specify the script (No arguments required)
* Output file will be printed to terminal.

```
python3 geo-coder.py
```

## Authors

Contributors names and contact info

ex. Louis Royce 

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the [Apache 2.0] License - see the LICENSE.md file for details

## Future Improvements

* Create Directories and File Structure automatically without requirement to run .BAT script

* Ability to Pass single postcode as argument if there isn't a requirement for bulk geo-coding. 


