## CSV Utilities

This directory contains a set of Python scripts that are designed to read a CSV file.

* create_from_csv.py
* claim_from_csv.py
* release_from_csv.py
* delete_from_csv.py

## Creating a virtual environment

We recommend that you create a new virtual environment for these scripts.

Example using virtualenv:

| Linux                                | Windows                               |
| ------------------------------------ | ------------------------------------- |
| `$ virtualenv --python=python3 env3` | `> virtualenv --python=python3 env3`  |
| `$ source env3/bin/activate`         | `> .\env3\Scripts\activate`           |
| `$ pip install -r requirements3.txt` | `> pip install -r requirements3.txt`  |


## Usage

Make sure you *activate* the virtualenv before every script execution.

For detailed usage information, run the script with `-h` as an argument.
All 4 scripts are very similar:
```
> .\create_from_csv.py -h
usage: create_from_csv.py [-h] [-host HOST] [-username USERNAME]
                          [-password PASSWORD]
                          [-console_loglevel {debug,info,warning,error,critical}]
                          [-file_loglevel {debug,info,warning,error,critical}]
                          CSVfile

Create devices on WA/DMP

positional arguments:
  CSVfile               Path to CSV file.

optional arguments:
  -h, --help            show this help message and exit
  -host HOST            URL of the WADMP server's API gateway. Check the code
                        for the default!
  -username USERNAME    Username. Check the code for the default!
  -password PASSWORD    Password. Check the code for the default!
  -console_loglevel {debug,info,warning,error,critical}
                        Log verbosity level. The higher the level, the fewer
                        messages that will be logged. Default = info
  -file_loglevel {debug,info,warning,error,critical}
                        Log verbosity level. The higher the level, the fewer
                        messages that will be logged. Default = info
```

```
> .\claim_from_csv.py -h
usage: claim_from_csv.py [-h] [-host HOST] [-username USERNAME]
                         [-password PASSWORD]
                         [-console_loglevel {debug,info,warning,error,critical}]
                         [-file_loglevel {debug,info,warning,error,critical}]
                         CSVfile Company

Claim devices to a company on WA/DMP

positional arguments:
  CSVfile               Path to CSV file.
  Company               Company name. Check the code for the default!

optional arguments:
  -h, --help            show this help message and exit
  -host HOST            URL of the API gateway. Default =
                        'https://gateway.wadmp.com'
  -username USERNAME    Username. Check the code for the default!
  -password PASSWORD    Password. Check the code for the default!
  -console_loglevel {debug,info,warning,error,critical}
                        Log verbosity level. The higher the level, the fewer
                        messages that will be logged. Default = info
  -file_loglevel {debug,info,warning,error,critical}
                        Log verbosity level. The higher the level, the fewer
                        messages that will be logged. Default = info
```

```
> .\release_from_csv.py -h
usage: release_from_csv.py [-h] [-host HOST] [-username USERNAME]
                           [-password PASSWORD]
                           [-console_loglevel {debug,info,warning,error,critical}]
                           [-file_loglevel {debug,info,warning,error,critical}]
                           CSVfile

Release devices from a company on WA/DMP

positional arguments:
  CSVfile               Path to CSV file.

optional arguments:
  -h, --help            show this help message and exit
  -host HOST            URL of the API gateway. Default =
                        'https://gateway.wadmp.com'
  -username USERNAME    Username. Check the code for the default!
  -password PASSWORD    Password. Check the code for the default!
  -console_loglevel {debug,info,warning,error,critical}
                        Log verbosity level. The higher the level, the fewer
                        messages that will be logged. Default = info
  -file_loglevel {debug,info,warning,error,critical}
                        Log verbosity level. The higher the level, the fewer
                        messages that will be logged. Default = info
```

```
> .\delete_from_csv.py -h
usage: delete_from_csv.py [-h] [-host HOST] [-username USERNAME]
                          [-password PASSWORD]
                          [-console_loglevel {debug,info,warning,error,critical}]
                          [-file_loglevel {debug,info,warning,error,critical}]
                          CSVfile

Delete devices from WA/DMP

positional arguments:
  CSVfile               Path to CSV file.

optional arguments:
  -h, --help            show this help message and exit
  -host HOST            URL of the WADMP server's API gateway. Check the code
                        for the default!
  -username USERNAME    Username. Check the code for the default!
  -password PASSWORD    Password. Check the code for the default!
  -console_loglevel {debug,info,warning,error,critical}
                        Log verbosity level. The higher the level, the fewer
                        messages that will be logged. Default = info
  -file_loglevel {debug,info,warning,error,critical}
                        Log verbosity level. The higher the level, the fewer
                        messages that will be logged. Default = info
```

You can change the default command-line arguments in the Python files, or specify new values on the command-line:

```.\create_from_csv.py .\example.csv -username USERNAME -password PASSWORD```

```.\claim_from_csv.py .\example.csv COMPANY -username USERNAME -password PASSWORD```

```.\release_from_csv.py .\example.csv COMPANY -username USERNAME -password PASSWORD```

```.\delete_from_csv.py .\example.csv -username USERNAME -password PASSWORD```

(These examples show backslashes because they were run on Windows)

### CSVfile

The `example.csv` file is provided to illustrate the expected schema.
- The first row is ignored.
- Edit the rest of the file with your own device information.

> Note: We **highly** recommend including the IMEI number when creating cellular devices.

### Company

The `claim_from_csv.py` file takes an argument which is your company name.
If the name contains a space, then you should enclose it in single-quotes. For example:
```
> .\claim_from_csv.py .\example.csv 'Krejuv Limited' -username bkinsella@advantech-bb.com -password PASSWORD -console_loglevel info -file_loglevel debug
```

### loglevel

There are 2 different `loglevel` arguments:
- `console_loglevel` determines what messages are printed to the console;
- `file_loglevel` determines what messages are printed to a file.

The logfile name is automatically based on the script name:
- `create_from_csv.log`
- `claim_from_csv.log`
- `delete_from_csv.log`

Python's logging module has a set of default loglevels. The higher the level, the fewer messages that will be logged:
```
 CRITICAL
 ERROR
 WARNING
 INFO
 DEBUG
```

Both loglevel arguments default to `info`. If you want more detail, you may change one or both to `debug`.

> Note: If you have a lot of devices, this will create a lot of verbose output!