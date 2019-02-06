import psycopg2

conn = psycopg2.connect(user='danielgriffin', password='', 
                        database='quandl_ui', host='localhost')

if conn.closed == 0:
    print('Connection successful')
else:
    print('Connection unsuccessful')


def create_dataset_master_table():
    sql = '''CREATE TABLE public.dataset_master
        (
            id integer,
            database_name text COLLATE pg_catalog."default",
            database_code text COLLATE pg_catalog."default",
            dataset_name text COLLATE pg_catalog."default",
            dataset_code text COLLATE pg_catalog."default",
            publisher_name text COLLATE pg_catalog."default",
            publisher_id text COLLATE pg_catalog."default"
        )'''

    with conn.cursor() as cursor:
        cursor.execute(sql)
    connection.commit()
    connection.close()


def create_chris_dataset():
    sql = '''CREATE TABLE chris
            (
            id integer,
            dataset_master_id integer foreign key,
            "date" date,
            open numeric,
            high numeric,
            low numeric,
            last numeric,
            volume integer,
            open_interest integer
            )'''

    with conn.cursor() as cursor:
        cursor.execute(sql)
    connection.commit()
    connection.close()


class DAO:
    pass






'''
Quandl uses a structure where there's a 'database', which roughly means all of the 
data sets for a given publisher; or if the publisher is large enough, then a 
subcategory of all the publisher's datasets.

Within the 'database', the individual time series/table/etc is called a dataset.

Databases and datasets have markedly different columns/table structure, so we
need specialized tables to handle each one, and we need to identify ahead of time
where to put the incoming data
'''

def check_dataset_master_for_dataset(data):
    sql = '''SELECT dataset_code
            FROM dataset_master 
            WHERE dataset_code = ?;'''
    with conn.cursor() as cursor:
        cursor.execute(sql, data.dataset_code) #this is sqlite syntax, needs review

    if sql_output == data.dataset_code:
        return True
    else:
        return False


def check_dataset_master_for_database(data):
    sql = """SELECT data.database_code FROM dataset_master;"""

    if sql_output == data.database_code:
        return True
    else:
        return False


def insert_security_dataset(data):
    sql = """INSERT INTO security_time_series
        (
        id integer
        dataset_master_id integer foreign key
        )
        """
#need to figure out how to splat out column names



class QuandlDatabase:
    pass


class QuandlDataset:
    pass


class ResultSet:
    pass
