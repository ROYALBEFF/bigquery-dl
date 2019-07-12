import argparse
import pydata_google_auth as pga
import pandas_gbq as pgbq
import datetime


def main():
    parser = argparse.ArgumentParser(description='Send SQL queries to BigQuery and save results as JSON files.')
    parser.add_argument('--project', metavar='NAME', type=str, required=True,
                        help='Name of BigQuery project.')
    parser.add_argument('--query', metavar='SQL QUERY', type=str, default=None,
                        help='SQL query that will be send to BigQuery.')
    parser.add_argument('--batch', metavar='PATH', type=str, default=None,
                        help='Batch mode. Path to text file containing multiple SQL queries delimited by semicolons.')
    parser.add_argument('--csv', action='store_true', help='Save results as CSV files instead.')
    parser.add_argument('--cache', action='store_true',
                        help='Use cached authentication credentials/cache authentication credentials')
    args = parser.parse_args()

    # authentication scopes
    scopes = ['https://www.googleapis.com/auth/bigquery']
    # use no or read-write cache
    cache = pga.cache.NOOP if not args.cache else pga.cache.READ_WRITE
    # get user credentials for Google APIs
    credentials = pga.auth.get_user_credentials(scopes, credentials_cache=cache)

    if args.query is not None:
        # send SQL query to BigQuery
        result = [pgbq.read_gbq(args.query, args.project, credentials=credentials)]
    elif args.batch is not None:
        # read SQL queries from file
        with open(args.batch) as f:
            queries = f.readlines()

        # join all lines to one string
        queries = ' '.join(queries)
        # remove new line symbols
        queries = queries.replace('\n', '')
        # split queries
        queries = queries.split(';')
        # if the last query also ended with a semicolon the queries list last element is an empty string
        queries = queries[:-1] if queries[-1] == '' else queries

        for q in queries:
            print(q)
        # send SQL query to BigQuery
        result = map(lambda q: pgbq.read_gbq(q, args.project, credentials=credentials), queries)
    else:
        print('Either a query (--query) or a file of queries (--batch) must be passed!')
        exit(1)

    if args.csv:
        for r in result:
            dt = str(datetime.datetime.now()).replace(' ', '_')
            with open('result_{}.csv'.format(dt), 'w+') as f:
                f.write(r.to_csv(orient='records'))
        exit(0)

    for r in result:
        dt = str(datetime.datetime.now()).replace(' ', '_')
        with open('result_{}.json'.format(dt), 'w+') as f:
            f.write(r.to_json(orient='records'))
