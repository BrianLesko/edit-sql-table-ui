#!/bin/bash

# Brian Lesko 6/17/2024
# Run a postgres Database server in a container with the alpine image

# 1. Pull a stable docker Image for the postgres database
#docker pull postgres:alpine # Opt for the alpine OS version for a smaller footprint

# 2 Create a container from the iamge and run it
#docker run --name my_postgres -e POSTGRES_HOST_AUTH_METHOD=trust -d -p 5432:5432 postgres:alpine

# 3. stop the container
#docker stop my_postgres

# 4. restart the container
docker start my_postgres