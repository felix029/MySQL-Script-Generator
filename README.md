# MySQL-Script-Generator
Simple program that generates a MySQL script to insert values contained in a given .xlsx file.

The xlsx file must follow this format: First row is the table columns names, other rows are the values to insert.

## Setup
To be able to run the program, you will need to install openpyxl by running this command:
```
pip install openpyxl
```

## How to run

| Option  | Description                                                          |
| ------- | -------------------------------------------------------------------- |
| --table | (Required) Give the name of the table you want to insert values into |
| --path  | (Required) Path of the .xlsx file that contains the values to insert |

To run, simply call the main.py file with the two required options shown in the table above and the program will create a .sql script
in the directory the main.py file is.

```
main.py --table table_name --path exemple_spreadsheet.xlsx
```

