# bigquery-dl

Download data from BigQuery and save results as JSON or CSV files.
You can use temporary or cached authentication credentials.

## Installation
Run the setup script using Python3. For global installtion run the setup script as root.

```
sudo python3 setup.py install
```

## Usage
After installing the script you can use it via command-line using the `bigquery-dl` command.

```
usage: bigquery-dl [-h] --project NAME [--query SQL QUERY] [--batch PATH]
                   [--csv] [--cache]

Send SQL queries to BigQuery and save results as JSON files.

optional arguments:
  -h, --help         show this help message and exit
  --project NAME     Name of BigQuery project.
  --query SQL QUERY  SQL query that will be send to BigQuery.
  --batch PATH       Batch mode. Path to text file containing multiple SQL
                     queries delimited by semicolons.
  --csv              Save results as CSV files instead.
  --cache            Use cached authentication credentials/cache
                     authentication credentials
```
