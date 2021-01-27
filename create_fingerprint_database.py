import sqlite3
from sqlite3 import Error
import numpy as np
 
def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)

 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
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
#def main():
    
    # Converts np.array to TEXT when inserting
    sqlite3.register_adapter(np.ndarray, adapt_array)

    # Converts TEXT to np.array when selecting
    sqlite3.register_converter("array", convert_array)

    sql_create_video_fingerprint_information_table = """ CREATE TABLE IF NOT EXISTS video_fingerprint_information (
                                                    Client text,
                                                    Commercial text,
                                                    Ad text,
                                                    Ad_Duration text,
                                                    fingerprint_array text,
                                                    fingerprint_json text
                                                ); """
    sql_create_audio_fingerprint_information_table = """ CREATE TABLE IF NOT EXISTS audio_fingerprint_information (
                                                    Client text,
                                                    Commercial text,
                                                    Ad text,
                                                    Ad_Duration text
                                                ); """



    sql_create_video_broadcast_information_table = """ CREATE TABLE IF NOT EXISTS video_broadcast_information (
                                            Station text,
                                            Date_of_broadcast text,
                                            Ethiopian_date date,
                                            Client text,
                                            Commercial text,
                                            Broadcast_information text, 
                                            Ad text,
                                            Ad_Duration text,
                                            Stream text,
                                            Stream_Duartion text,
                                            match_time text
                                        ); """





    sql_create_audio_broadcast_information_table = """ CREATE TABLE IF NOT EXISTS audio_broadcast_information (
                                                Station text,
                                                Date_of_broadcast date,
                                                Ethiopian_date date,
                                                Client text,
                                                Commercial text,
                                                Broadcast_information text, 
                                                Ad text,
                                                Ad_Duration text,
                                                Stream text,
                                                Stream_Duartion text,
                                                match_time text
                                            ); """
                                    



    # create a database connection
    conn = create_connection(database)
    # create tables
    if conn is not None:
 
        # create tasks table
        create_table(conn, sql_create_video_fingerprint_information_table)
        create_table(conn, sql_create_audio_fingerprint_information_table)
        create_table(conn, sql_create_video_broadcast_information_table)
        create_table(conn, sql_create_audio_broadcast_information_table)
    else:
        print("Error! cannot create the database connection.")
 
def create_video_information(conn, video_information):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO video_fingerprint_information(Client,Commercial,Ad,Ad_Duration,fingerprint_array,fingerprint_json)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, video_information)
    return cur.lastrowid
def create_audio_information(conn, audio_information):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO audio_fingerprint_information(Client,Commercial,Ad,Ad_Duration)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, audio_information)
    return cur.lastrowid

def create_video_broadcast_information(conn, video_information):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id

    """
    sql = ''' INSERT INTO video_broadcast_information(Station,Date_of_broadcast,Ethiopian_date,Client,Commercial,Broadcast_information,Ad,Ad_Duration,Stream,Stream_Duartion,match_time)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, video_information)
    return cur.lastrowid

def create_audio_broadcast_information(conn, audio_information):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO audio_broadcast_information(Station,Date_of_broadcast,Ethiopian_date,Client,Commercial,Broadcast_information,Ad,Ad_Duration,Stream,Stream_Duartion,match_time)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, audio_information)
    return cur.lastrowid

def insert_video_information_to_database(database,Client,Commercial,Ad,Ad_Duration,fingerprint_array,fingerprint_json):
    # create a database connection
    conn = create_connection(database)
    with conn:
        # tasks
        information = Client,Commercial,Ad,Ad_Duration,fingerprint_array,fingerprint_json
        create_video_information(conn, information)

def insert_audio_information_to_database(database,Client,Commercial,Ad,Ad_Duration):
    # create a database connection
    conn = create_connection(database)
    with conn:
        # tasks
        information = Client,Commercial,Ad,Ad_Duration
        create_audio_information(conn, information)        


def insert_video_broadcast_information_to_database(database,Station,Date_of_broadcast,Ethiopian_date,Client,Commercial,Broadcast_information,Ad,Ad_Duration,Stream,Stream_Duartion,match_time):
    # create a database connection
    conn = create_connection(database)
    with conn:
        # tasks
        information = Station,Date_of_broadcast,Ethiopian_date,Client,Commercial,Broadcast_information,Ad,Ad_Duration,Stream,Stream_Duartion,match_time
        create_video_broadcast_information(conn, information)

def insert_audio_broadcast_information_to_database(database,Station,Date_of_broadcast,Ethiopian_date,Client,Commercial,Broadcast_information,Ad,Ad_Duration,Stream,Stream_Duartion,match_time):
    # create a database connection
    conn = create_connection(database)
    with conn:
        # tasks
        information = Station,Date_of_broadcast,Ethiopian_date,Client,Commercial,Broadcast_information,Ad,Ad_Duration,Stream,Stream_Duartion,match_time
        create_audio_broadcast_information(conn, information)   



def select_video_fingerprint_information_from_database_by_commercial(database,Commercial):
    """
    Query information by Commercial
    :param conn: The Connection Object 
    :param Commercial: 
    :return:
    """
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT fingerprint_array FROM video_fingerprint_information WHERE Commercial=?", (Commercial,))
    #cur.execute("SELECT * FROM video_fingerprint_information")

    rows = cur.fetchall()
    return rows 

# 

def select_video_information_from_database_by_commercial(database,Commercial):
    """
    Query information by Commercial
    :param conn: The Connection Object 
    :param Commercial: 
    :return:
    """
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Client,Ad,Ad_Duration,fingerprint_json FROM video_fingerprint_information WHERE Commercial=?", (Commercial,))
    #cur.execute("SELECT * FROM video_fingerprint_information")

    rows = cur.fetchall()
    return rows 

def select_all_commercial_video_information_from_database(database):
    """
    Query information by Commercial
    :param conn: The Connection Object 
    :param Commercial: 
    :return:
    """
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Commercial,Ad_Duration,fingerprint_json FROM video_fingerprint_information")
    #cur.execute("SELECT * FROM video_fingerprint_information")

    rows = cur.fetchall()
    return rows 








def select_audio_information_from_database_by_commercial(database,Commercial):
    """
    Query information by Commercial
    :param conn: The Connection Object 
    :param Commercial: 
    :return:
    """
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Client, Ad, Ad_duration FROM audio_fingerprint_information WHERE Commercial=?", (Commercial,))
    #cur.execute("SELECT * FROM video_fingerprint_information")

    rows = cur.fetchall()
    return rows 


def select_audio_broadcast_information_from_database_by_commercial(database,Commercial):
    """
    Query information by Commercial
    :param conn: The Connection Object 
    :param Commercial: 
    :return:
    """
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Client, Ad, Ad_Duration FROM audio_broadcast_information WHERE Commercial=?", (Commercial,))
    #cur.execute("SELECT * FROM video_fingerprint_information")

    rows = cur.fetchall()
    return rows 




# def delete_video_information_from_database(database):
#     conn = create_connection(database)
#     cur = conn.cursor()
#     cur.execute("DELETE FROM video_fingerprint_information WHERE rowid NOT IN (SELECT max(rowid) FROM video_fingerprint_information);")

def delete_video_information_from_database_by_commercial(database,Commercial):
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("DELETE FROM video_fingerprint_information WHERE Commercial=?",(Commercial,))




# def delete_audio_information_from_database(database):
#     conn = create_connection(database)
#     cur = conn.cursor()
#     cur.execute("DELETE FROM audio_fingerprint_information WHERE rowid NOT IN (SELECT max(rowid) FROM audio_fingerprint_information);")


# def delete_video_broadcast_information_from_database(database):
#     conn = create_connection(database)
#     cur = conn.cursor()
#     cur.execute("DELETE FROM video_broadcast_information WHERE rowid NOT IN (SELECT max(rowid) FROM video_broadcast_information);")



# def delete_audio_broadcast_information_from_database(database):
#     conn = create_connection(database)
#     cur = conn.cursor()
#     sql = 'DELETE FROM audio_broadcast_information WHERE rowid NOT IN (SELECT max(rowid) FROM audio_broadcast_information)'
#     cur.execute(sql)


    