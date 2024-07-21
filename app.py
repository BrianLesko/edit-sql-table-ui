# Brian Lesko
# 6/17/2024
# interact with a PostreSQL database container from python using streamlit 

import streamlit as st
# to interact with the database

# create the database connection
import psycopg2
from psycopg2 import Error

# create the connection

try:
    connection = psycopg2.connect(user = "postgres", password = "password", host = "0.0.0.0", port = "5432", database = "postgres")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, Error) as error :    
    print ("Error while connecting to PostgreSQL", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")




