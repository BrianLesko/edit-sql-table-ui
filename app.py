# Brian Lesko
# 8/27/2024
# Web App UI for querying a postgresql database running in a container

import streamlit as st
import psycopg2
from psycopg2 import Error
import subprocess
from time import sleep

# Function to establish a connection to the PostgreSQL database
def create_connection(db_name="postgres"):
    try:
        connection = psycopg2.connect(
            database=db_name,
            host="127.0.0.1",
            user="lesko",
            password="lesko",
            port=5432
        )
        return connection
    except (Exception, Error) as error:
        st.error(f"Error connecting to PostgreSQL database: {error}")
        if st.button("Restart the SQL server"):
            with st.spinner("Restarting SQL server..."):
                result1 = subprocess.run("docker stop my_postgres", shell=True, capture_output=True, text=True)
                sleep(2.5)
                result2 = subprocess.run("docker start my_postgres", shell=True, capture_output=True, text=True)
                sleep(2.5)
                st.write(result2)
                st.rerun()
        return None

def run_query(query, cursor):
    try:
        if query.lower().startswith("create database"):
            # Handle CREATE DATABASE separately
            cursor.connection.set_isolation_level(0)  # Set autocommit mode
            cursor.execute(query)
            cursor.connection.set_isolation_level(1)  # Reset to default mode
            return "Database created successfully."
        else:
            cursor.execute(query)
            if query.lower().startswith("select"):
                # Fetch and return results for SELECT queries
                return cursor.fetchall()
            else:
                # Commit changes for non-SELECT queries (INSERT, UPDATE, DELETE)
                cursor.connection.commit()
                return "Query executed successfully."
    except (Exception, Error) as error:
        return f"Error: {error}"
    
def get_database_list():
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
            databases = cursor.fetchall()
            database_list = [db[0] for db in databases]
            cursor.close()
            connection.close()
            return database_list
    except (Exception, Error) as error:
        print(f"Error retrieving database list: {error}")
        return []

# Function to get list of tables in the database
def get_sidebar(conn, cursor):
    # get all the DB's with SELECT datname FROM pg_database;
    cursor.execute("SELECT datname FROM pg_database;")
    databases = cursor.fetchall()
    database_list = [db[0] for db in databases]

    # Separate default and user-created databases
    default_dbs = ['postgres', 'template0', 'template1']
    user_dbs = [db for db in database_list if db not in default_dbs]

    with st.sidebar:
        st.caption("Default Databases:")
        for db in default_dbs:
            if db in database_list:  # Check if the default DB exists in the list
                st.write(db)

        st.caption("Databases:")
        for db in user_dbs:
            connection = create_connection(db)
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='public';")
                table_count = cursor.fetchone()[0]
                st.write(f"{db}: {table_count} tables")
                cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
                tables = cursor.fetchall()
                for table in tables:
                    st.write(f" - {table[0]}")
                cursor.close()
                connection.close()

# Main application function
def main():
    # Streamlit UI
    st.title("PostgreSQL Query Interface")

    # Establish database connection
    all_databases = get_database_list()
    selected_db = st.selectbox("Select a database:", all_databases)
    connection = create_connection(selected_db)
    if connection:
        cursor = connection.cursor()

        # Show tables in the sidebar
        st.sidebar.title("Database Connections")
        get_sidebar(connection, cursor)

        # User input for SQL query
        user_query = st.text_area("Enter your SQL query here:", height=150)

        if st.button("Run Query"):
            # Execute the query and display results
            result = run_query(user_query, cursor)
            if isinstance(result, list):
                # Display query results if it's a SELECT query
                for row in result:
                    st.write(row)
            else:
                # Display execution status for non-SELECT queries
                st.write(result)

        # Close the cursor and connection
        cursor.close()
        connection.close()

# Run the main function
if __name__ == "__main__":
    main()
