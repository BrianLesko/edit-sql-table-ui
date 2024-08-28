# Brian Lesko
# 8/27/2024
# Web App UI for editing the employees table in the lesko database

import streamlit as st
import psycopg2
from psycopg2 import Error
import subprocess
from time import sleep
import pandas as pd
from style import style, footer, header, make_title

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

def save_changes(df, original_df, cursor):
    # Identify deleted rows
    deleted_rows = original_df[~original_df['email'].isin(df['email'])]
    #st.write(f"deleting: {deleted_rows}")

    # Delete rows from the database
    for index, row in deleted_rows.iterrows():
        delete_query = "DELETE FROM employees WHERE email = %s"
        cursor.execute(delete_query, (row['email'],))

    # Update existing rows and insert new rows
    for index, row in df.iterrows():
        if row['email'] in original_df['email'].values:
            # Check for updates
            original_row = original_df[original_df['email'] == row['email']].iloc[0]
            if not row.equals(original_row):
                update_query = "UPDATE employees SET name = %s, manager_email = %s, yearly_pto = %s WHERE email = %s"
                cursor.execute(update_query, (row['name'], row['manager_email'], row['yearly_pto'], row['email']))
                #st.write(f"updating: {row}")
        else:
            # New row added
            insert_query = "INSERT INTO employees (name, email, manager_email, yearly_pto) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (row['name'], row['email'], row['manager_email'], row['yearly_pto']))
            #st.write(f"inserting: {row}")
    cursor.connection.commit()

# Main application function
def main():
    st.set_page_config(
    page_title="Edit PTO Approvals",
    page_icon='./CCBS.png',
    layout="wide"  # This sets the layout to wide format
    )
    style()
    st.html(header)
    st.html(make_title('Edit Employees'))
    col1, col2, col3 = st.columns([1, 2, 1])
    col2.write("**Edit the company's employee records here.**")
    col2.write("")

    # Establish database connection
    all_databases = get_database_list()
    selected_db = 'lesko' # st.selectbox("Select a database:", all_databases)
    connection = create_connection(selected_db)
    if connection:
        cursor = connection.cursor()

        # Fetch column names in the order they are defined in the table
        cursor.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = 'employees'
            ORDER BY ordinal_position;
        """)
        columns = cursor.fetchall()
        column_names = [col[0] for col in columns]

        # Filter out the 'inserted_at' column
        filtered_columns = [col for col in column_names if col != 'inserted_at']

        # Fetch the employee data
        cursor.execute("SELECT * FROM employees;")
        employees = cursor.fetchall()

        # Convert the data into a Pandas DataFrame with the filtered columns
        df = pd.DataFrame(employees, columns=column_names)[filtered_columns]

        # Fetch manager names and their corresponding emails
        cursor.execute("SELECT name, email FROM employees WHERE email IN (SELECT DISTINCT manager_email FROM employees);")
        manager_data = cursor.fetchall()
        manager_dict = {name: email for name, email in manager_data}

        # Get Filter inputs from the user
        col2.write("")
        manager_names = ['All'] + list(manager_dict.keys())
        filter_by_manager = col2.selectbox("Select a manager", options=manager_names)
        col1, col2, col3 = st.columns([1, 2, 1])
        col2.write("")

        # Filtering the DF
        fdf = df.copy()
        if filter_by_manager != 'All':
            manager_email = manager_dict[filter_by_manager]
            filtered_df = fdf[fdf['manager_email'] == manager_email].reset_index(drop=True)  # Filtered by manager
            anti_filtered_df = fdf[fdf['manager_email'] != manager_email].reset_index(drop=True)  # Anti-filtered by manager
        else:
            filtered_df = fdf[filtered_columns].reset_index(drop=True)
            anti_filtered_df = pd.DataFrame(columns=filtered_columns)  # Empty DataFrame with filtered columns

        # Display the DataFrame in Streamlit
        edited_df = col2.data_editor(filtered_df, num_rows="dynamic")
        
        # Remove empty rows from combined_df
        edited_df = edited_df.dropna(how='all')
        combined_df = pd.concat([edited_df, anti_filtered_df])
        
        # Convert DataFrames to sets of tuples for comparison
        combined_df_set = set([tuple(row) for row in combined_df.to_numpy()])
        df_set = set([tuple(row) for row in df.to_numpy()])

        # Compare the sets
        if combined_df_set != df_set:
            save_changes(combined_df, df, cursor)
            col2.success(f'Changes saved successfully at {pd.Timestamp.now().strftime("%I:%M%p").lower()}!')

        # Close the cursor and connection
        cursor.close()
        connection.close()

# Run the main function
if __name__ == "__main__":
    main()