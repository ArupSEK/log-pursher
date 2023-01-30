# log-pursher
Log File Parser
This is a python script for parsing a log file. The script uses a regular expression to search for specific patterns in the log file and extract the matches. The extracted data is then written to a new file, with the current date and time included in the file name.

Prerequisites
The following packages must be installed to run this script:

re
time
Usage
Save the script to a file with a .py extension (e.g. parser.py)
Update the log_file_path variable with the path to the log file you want to parse.
Run the script using a Python interpreter.
Copy code
python parser.py
Customization
You can modify the regular expression in the script to match different patterns in the log file. The current regular expression is set to extract data in the following format:

python
Copy code
<property name="{property_name}">{property_value}</property>
Output
The script outputs a new file with the extracted data. The file will be named:

parsher_output{current_time}.txt
Where {current_time} is the current date and time. The extracted data will be written to this file in the same format as it appears in the log file.

