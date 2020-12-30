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


#### Alias

Alias is an optional string that will be displayed in the WA/DMP User Interface.

It allows the user to identify a device using a more human-friendly name.

You should only specify an alias when *claiming* a device, not when *creating* it!
An alias only has meaning within the context of the company that claims it.

#### Serial No.

This is printed on the physical label of the device.

Serial No. is mandatory when creating, claiming, or releasing a device.

#### Order Code

Order Code is an optional string.

#### MAC

This is the MAC address of the *primary ethernet* interface on the device.
It is also printed on the physical label of the device.

MAC is mandatory when creating, claiming, releasing, or deleting a device.

#### IMEI

IMEI stands for "International Mobile Equipment Identity". It is the unique number of the cellular module in the device, and is available on the physical label of the device.

When creating a device, IMEI is optional. However. we **highly** recommend including the IMEI number when creating cellular devices.

If the IMEI number was included when creating a device, then the IMEI number must be included when claiming or releasing that device later.

#### Type

In order to avoid any ambiguity with various names that are used in sales and marketing (e.g. product type, product name, order code, etc.), the string in the Type column should be the name of the *firmware* used by the device.

(ICR-1601 devices are an exception, as their firmware cannot be changed via WA/DMP)

| Product Platform | Product Family | Product Name | WA/DMP Device Type |
| ---------------- | -------------- | ------------ | ------------------ |
| lite             | ICR-1601       | ICR-1601G    | ICR-1601G          |
|                  |                | ICR-1601W    | ICR-1601W          |
| v2               | Conel v2       | LR77 v2      | LR77-v2            |
|                  |                | LR77 v2L     | LR77-v2L           |
|                  |                | UR5i v2      | UR5i-v2            |
|                  |                | UR5i v2L     | UR5i-v2L           |
|                  |                | XR5i v2      | XR5i-v2            |
|                  |                | XR5i v2E     | XR5i-v2e           |
| v3               | SmartStart     | SL304, SL305, SL306 | SPECTRE-v3L-LTE |
|                  |                | SL302        | SPECTRE-v3L-LTE-US |
|                  | SmartFlex      | SR300        | SPECTRE-v3-ERT     |
|                  |                | SR303, SR304, SR306, SR307, SR308, SR309 | SPECTRE-v3-LTE |
|                  |                | SR305        | SPECTRE-v3-LTE-US  |
|                  | SmartMotion    | ST353, ST355 | SPECTRE-v3T-LTE    |
|                  | ICR-3200       | ICR-3211     | ICR-321x           |
|                  |                | ICR-3231, ICR-3232 | ICR-323x     |
|                  |                | ICR-3241     | ICR-324x           |

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
- `release_from_csv.log`
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