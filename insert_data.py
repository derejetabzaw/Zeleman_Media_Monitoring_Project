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
    except Error as e:
        print(e)
 
    return conn
 
 
def create_video_information(conn, video_information):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO video_information(GCDate,EthDate,Clock,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_duration,Time_in_video)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, video_information)
    return cur.lastrowid

 
def create_audio_information(conn, audio_information):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
 
    sql = ''' INSERT INTO audio_information(GCDate,EthDate,Clock,Client,Commercial,Radio_Station,Ad,Stream,broadcast_information,Ad_duration,Time_in_video)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, audio_information)
    return cur.lastrowid
 
 
def insert_information_to_database(database,Date,Eth_Date,Time,Client,Commercial,Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video):
    # create a database connection
    conn = create_connection(database)
    with conn:
        # tasks
        information = Date,Eth_Date,Time,Client, Commercial, Station,Ad,Stream,broadcast_information,Ad_dur,Time_in_video
        create_video_information(conn, information)
        #create_audio_information(conn, information)
 
 
# if __name__ == '__main__':
#     main()