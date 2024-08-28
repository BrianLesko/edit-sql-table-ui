#!/bin/bash

# Brian Lesko 6/17/2024
# Run a postgres Database server in a container with the alpine image

# 1. Pull a stable docker Image for the postgres database
#docker pull postgres:alpine # Opt for the alpine OS version for a smaller footprint

# 2 Create a container from the iamge and run it
#docker run --name my_postgres -e POSTGRES_USER=lesko -e POSTGRES_PASSWORD=lesko -d -p 5432:5432 -v /home/lesko/postgres_data:/var/lib/postgresql/data postgres:alpine

# 3. stop the container
#docker stop my_postgres

# 4. restart the container
docker start my_postgres 

# 5. Start the GUI interface
cd "$(dirname "$(realpath "$0")")"
source my_env/bin/activate
streamlit run app.py --server.port 8508 & # for general queries, setting up your tables etc

streamlit run employees.py --server.port 8509 # Edit your table with a clean UI

# now you can access the server via the terminal with: psql -h 127.0.0.1 -U myuser -d postgres