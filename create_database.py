import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
 
    return conn
 
 
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
 
 
def create_database_and_tables(database):
    #database = r"db/information_database.db"
  
    sql_create_video_information_table = """ CREATE TABLE IF NOT EXISTS video_information (
                                        GCDate Date,
                                        EthDate Date,
                                        Clock time,
                                        Client text,
                                        Commercial text,
                                        Station text,
                                        Ad text,
                                        Stream text,
                                        broadcast_information text,
                                        Ad_duration text,
                                        Time_in_video text
                                    ); """
    sql_create_audio_information_table = """ CREATE TABLE IF NOT EXISTS audio_information (
                                        GCDate Date,
                                        EthDate Date,
                                        Clock time,
                                        Client text,
                                        Commercial text,
                                        Radio_Station text,
                                        Ad text,
                                        Stream text,
                                        broadcast_information text,
                                        Ad_duration text,
                                        Time_in_video text
                                    ); """

    # create a database connection
    conn = create_connection(database)
 
    # create tables
    if conn is not None:
 
        # create tasks table
        create_table(conn, sql_create_video_information_table)
        create_table(conn, sql_create_audio_information_table)
    else:
        print("Error! cannot create the database connection.")
 
 

    