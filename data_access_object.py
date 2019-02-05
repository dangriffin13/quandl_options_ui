


class DAO:
    pass


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




check_dataset_master_for_dataset(data):
    sql = """SELECT data.database_code, data.dataset_code FROM dataset_master;"""

    if sql_output == tuple(data.database_code, data.dataset_code):
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



