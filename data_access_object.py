import psycopg2

conn = psycopg2.connect(user='danielgriffin', password='', 
                        database='quandl_ui', host='localhost')

if conn.closed == 0:
    print('Connection successful')
else:
    print('Connection unsuccessful')


def reconnect_to_db():
    conn = psycopg2.connect(user='danielgriffin', password='', 
                        database='quandl_ui', host='localhost')


def test_insert():
    sql = '''INSERT INTO dataset_master
            (database_name, database_code, dataset_name, dataset_code, quandl_dataset_id, dataset_description) 
            values ('test', 'test', 'test', 'test', 123, 'test successful');
            '''

    with conn.cursor() as cursor:
        cursor.execute(sql)

    print('cursor executed')
    conn.commit()
    conn.close()


def create_dataset_master_table():
    sql = '''CREATE TABLE public.dataset_master
        (
            id bigserial PRIMARY KEY,
            database_name text,
            database_code text,
            dataset_name text,
            dataset_code text,
            quandl_dataset_id text,
            dataset_description text
        )'''

    with conn.cursor() as cursor:
        cursor.execute(sql)
    conn.commit()
    conn.close()


def create_db_to_dataset_mapping_table():
    pass


def create_chris_dataset(): 
    chris_metadata = ('Wiki Continuous Futures', 'CHRIS', 
        'WTI Crude Futures, Continuous Contract', 'ICE_T1', 11272034,
        'Historical Futures Prices: WTI Crude Futures, Continuous Contract #1. Non-adjusted price based on spot-month continuous contract calculations. Raw data from ICE.'
        )

    #need to add chris to dataset_master so that there's a foreign key
    sql_add_chris_to_master = '''INSERT INTO dataset_master
            (database_name, database_code, dataset_name, dataset_code, quandl_dataset_id, dataset_description) 
            values (%s, %s, %s, %s, %s, %s);
            '''

    with conn.cursor() as cursor:
        cursor.execute(sql_add_chris_to_master, chris_metadata)

    sql_create_chris_table = '''CREATE TABLE chris
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
        cursor.execute(sql_create_chris_table)

    print('cursor executed')
    conn.commit()
    conn.close()



def chris_add_data(quandl_dataset_id, df):
    sql = '''INSERT INTO chris 
            values
            (%(date)s, %(dataset_master_id)s, %(open)s, %(high)s,
            %(low)s, %(last)s, %(volume)s, %(open_interest)s
            )'''

    cols = df.columns.tolist()

    with conn.cursor() as cursor:
        for row in df:
            values = {k:v for (k, v) in zip(cols, row)}  #concern about order matching between cols and row vals
            cursor.execute(sql, tuple(values))

    conn.commit()
    conn.close()



def disconnect_all_db_sessions(database):
    db_string = database + '()'

    sql = '''SELECT pg_terminate_backend(pg_stat_activity.pid)
                FROM pg_stat_activity
                WHERE datname = %s #database name
                AND pid <> pg_backend_pid();
            ''' % (db_string)



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

    tup = (data['database_code'],data['dataset_code'])

    with conn.cursor() as cursor: #do i need to reopen connection?
        cursor.execute(sql, tup) #this is sqlite syntax, needs review
        result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def check_dataset_master_for_database(data):
    sql = """SELECT data.database_code FROM dataset_master;"""


    with conn.cursor() as cursor:
        cursor.execute(sql, tup)
        result = cursor.fetchone()

    if result == data.database_code:
        return True
    else:
        return False


def fetchone_result(sql, data=None):
    with conn.cursor() as cursor:
        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)
        result = cursor.fetchone()

    return result

def insert_security_dataset(data):
    sql = """INSERT INTO security_time_series
        (
        id integer
        dataset_master_id integer foreign key
        )
        """



class QuandlDatabase:
    pass



class QuandlDataset:
    
    def __init__(self, database_name, database_code, dataset_name, 
                dataset_code, quandl_dataset_id, dataset_description, data=None):
        self.database_name = database_name
        self.database_code = database_code
        self.dataset_name = dataset_name
        self.dataset_code = dataset_code
        self.quandl_dataset_id = quandl_dataset_id
        self.dataset_description = dataset_description
        self.data = data


class ResultSet:
    pass


seed = QuandlDataset('Seed', '1234', 'Test', '5678', -1, 'Initializing Dataset Master Table')
