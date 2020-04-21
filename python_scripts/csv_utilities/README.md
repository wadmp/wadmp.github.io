## CSV Utilities

This directory contains a set of Python scripts that are designed to read a CSV file.

* create_from_csv.py
* claim_fram_csv.py
* delete_from_csv.py

## Creating a virtual environment

We recommend that you create a new virtual environment for these scripts.

Example using virtualenv:

| Linux                              | Windows                             |
| ---------------------------------- |-------------------------------------|
| $ virtualenv --python=python3 env3 | PS virtualenv --python=python3 env3 |
| $ source env3/bin/activate         | PS .\env3\Scripts\activate          |
| $ pip install -r requirements3.txt | PS pip install -r requirements3.txt |


## Usage

Make sure you *activate* the virtualenv before every script execution.

The `example.csv` file is provided to illustrate the expected schema.
- The first row is ignored.
- Edit the rest of the file with your own device information.

Note: We **highly** recommend including the IMEI number when creating cellular devices.

You can change the default command-line arguments in the Python files, or specify new values on the command-line:

```.\create_from_csv.py .\example.csv -host https://gateway.wadmp.com -username USERNAME -password PASSWORD -loglevel debug```

```.\claim_from_csv.py .\example.csv COMPANY -host https://gateway.wadmp.com -username USERNAME -password PASSWORD -loglevel debug```

```.\claim_from_csv.py .\example.csv -host https://gateway.wadmp.com -username USERNAME -password PASSWORD -loglevel debug```

(These examples show backslashes because they were run on Windows)