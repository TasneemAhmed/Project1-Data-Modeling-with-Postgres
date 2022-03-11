#import library to connect to Postgres
import psycopg2

def create_DB():
    """
    - Connect to postgres DB with crediantials
    - Get cursor to execute any query
    - Drop sparkify DB if exists
    - Create sparkify DB
    - commit changes to able to rollback
    - return connection & cursor
    """
    hostname = "localhost"
    database = "postgres"
    username = "postgres"
    password = "Tasneem_999"
    port_id = 5432

    #create instance of Postgres & we check we have correct privillages to DB
    try:
        conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=password, port=port_id)
    except psycopg2.Error as e:
        print("Error: Could not connect to PosgreeSQL DB")
        print(e)
    
    #use connection to get cursor to execute any query
    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Counld not connect to the cursor of DB")
        print(e)
    
    #change DB name
    database = "sparkify"

    #Dropping sparkify DB if exists
    try:
        cur.execute("drop database if exists sparkify")
    except psycopg2.Error as e:
        print("Error: can't dropping sparkify DB")
        print(e)

    #Creating sparkify DB
    try:
        cur.execute("create database if not exists sparkify")
    except psycopg2.Error as e:
        print("Error: can't creating sparkify DB")
        print(e)

    #autocommit to not make conn.commit() after every command, commit transactions make us rollback (feature of relational DB)
    conn.set_session(autocommit=True)

    #return connection & cursor
    return conn, cur