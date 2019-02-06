


create_dataset_master_table():
    sql = """CREATE TABLE public.dataset_master
        (
            id integer,
            database_name text COLLATE pg_catalog."default",
            database_code text COLLATE pg_catalog."default",
            dataset_name text COLLATE pg_catalog."default",
            dataset_code text COLLATE pg_catalog."default",
            publisher_name text COLLATE pg_catalog."default",
            publisher_id text COLLATE pg_catalog."default"
        )"""



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

check_dataset_master_for_dataset(data):
    sql = """SELECT data.dataset_code FROM dataset_master;"""

    if sql_output == data.dataset_code:
        return True
    else:
        return False


check_dataset_master_for_database(data):
    sql = """SELECT data.database_code FROM dataset_master;"""

    if sql_output == data.database_code:
        return True
    else:
        return False


insert_security_dataset(data):
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
