import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn
def select_all_video_information(conn):
    """
    Query all rows in the video_information table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM video_information")
 
    rows = cur.fetchall()
    
    return rows
def select_some_video_information(conn,Client,Commercial):
    """
    Query all rows in the video_information table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT GCDate , broadcast_information FROM video_information WHERE Client=? and Commercial=?",(Client,Commercial))
    #cur.execute("SELECT GCDate , broadcast_information FROM video_information WHERE Commercial=?",(Commercial,))
 
    rows = cur.fetchall()
    return rows 
    
def select_video_information_date(conn, date):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM video_information WHERE GCDate=?", (date,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
def select_video_information_client(conn, Client):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    #cur.execute("SELECT * FROM video_information WHERE Client=?", (Client,))
    cur.execute("SELECT * FROM video_information WHERE Client=? ", (Client,))
 
    rows = cur.fetchall()
 

    return rows 
def select_video_information_commercial(conn, Commercial):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM video_information WHERE Commercial=?", (Commercial,))
 
    rows = cur.fetchall()
    return rows 

    
 
def database_query():
    database = r"C:/Users/dereje/Desktop/Media_Monitoring_Project/Frontend/frontend_codes/information_database.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        #print("1. Query video_information by Date:")
        #select_video_information_date(conn, '1,30,2020')
 
        # print("2. Query all video_information")
        # select_all_video_information(conn)

        # print("3. Query video_information by Client")
        # select_video_information_client(conn, 'Cactus')
        
        # print("4. Query video_information by Commercial")
        # select_video_information_commercial(conn, 'Coca Cola')

        print("5")
        select_some_video_information(conn,' Zeleman', 'Coca Cola')
 
 
# if __name__ == '__main__':
#     database_query()