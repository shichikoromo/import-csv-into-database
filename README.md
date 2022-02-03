# import-csv-into-database
Python script to import csv file into database (MSSQL)

# Requirement

* python 3.10
* pyodbc 4.0.32

# Installation

```bash
pip install pyodbc
```

On Windows, you may be prompted to install "Microsoft Visual C++ 14.0".
This can be resolved by installing the "Build Tools for Visual Studio".

# Usage

* The configuration file (`settings.py`) needs to be modified according to the environment.
* `.xlsx` file must be converted to the `.csv` file

```bash
git clone https://github.com/shichikoromo/import-csv-into-database.git
python script.py
```
