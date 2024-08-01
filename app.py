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
            user="postgres",
            password="",
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

# Function to execute query safely
def run_query(query, cursor):
    try:
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
            if st.button(f"Show tables in {db}"):
                connection = create_connection(db)
                if connection:
                    cursor = connection.cursor()
                    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' ORDER BY table_name;")
                    tables = cursor.fetchall()
                    table_list = [table[0] for table in tables]
                    for table in table_list:
                        if st.button(f"Show data in {table}", key=f"{db}_{table}"):  # Ensure unique key for button
                            st.write(f"Table: {table}")
                            cursor.execute(f"SELECT * FROM {table};")
                            data = cursor.fetchall()
                            for row in data:
                                st.write(row)
                    cursor.close()
                    connection.close()



# Main application function
def main():
    # Streamlit UI
    st.title("PostgreSQL Query Interface")

    # Establish database connection
    connection = create_connection()
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
