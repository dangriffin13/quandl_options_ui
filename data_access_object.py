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
            id bigserial PRIMARY KEY,
            database_name text COLLATE pg_catalog."default",
            database_code text COLLATE pg_catalog."default",
            dataset_name text COLLATE pg_catalog."default",
            dataset_code text COLLATE pg_catalog."default",
            dataset_description text COLLATE pg_catalog."default"
        )'''

    with conn.cursor() as cursor:
        cursor.execute(sql)
    conn.commit()
    conn.close()


def create_chris_dataset(): #need to add chris to dataset_master
    add_chris_to_master_sql = '''INSERT INTO dataset_master
            (database_name, database_code, dataset_name, dataset_code, dataset_description) 
            values (')
            )'''

    create_table_sql = '''CREATE TABLE chris
            (
            id bigserial PRIMARY KEY,
            dataset_master_id integer REFERENCES dataset_master (id),
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

    print('cursor executed')
    conn.commit()
    conn.close()



def disconnect_all_db_sessions(database): #need to insert database as variable in SQL
    sql = '''SELECT pg_terminate_backend(pg_stat_activity.pid)
                FROM pg_stat_activity
                WHERE datname = ?()
                AND pid <> pg_backend_pid();
            '''

            

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
    sql = '''SELECT database_code, dataset_code
            FROM dataset_master 
            WHERE database_code = %s
                AND dataset_code = %s;'''
    with conn.cursor() as cursor:
        cursor.execute(sql, data.database_code, data.dataset_code) #this is sqlite syntax, needs review

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
    
    def __init__(self, database_name, database_code, dataset_name, 
                dataset_code, dataset_description, data=None):
        self.database_name = database_name
        self.database_code = database_code
        self.dataset_name = dataset_name
        self.dataset_code = dataset_code
        self.dataset_description = dataset_description
        self.data = data


class ResultSet:
    pass


seed = QuandlDataset('Seed', '1234', 'Test', '5678', 'Initializing Dataset Master Table')
