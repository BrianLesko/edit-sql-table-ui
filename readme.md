# Containerized SQL server with web UI

Written in pure Python and using PostgreSQL, this repository hosts web based UI's. One, for administrative querying of the whole database - app.py. The second, for end users to edit a single table. The current implementation is being deployed in production for an HR department to edit their website access list and PTO days. 

The SQL server is containerized, with a docker volume for persistent data. 

## Dependencies

Python libraries
- `streamlit`: to create the user interface with pure python
- `psycopg2-binary`: the binary installed correctly while the normal library did not. 

Docker
- I am opting for the alpine linux docker cotnainer for a small footprint. 
- Heres the image: PostgreSQL has an [official docker image](https://hub.docker.com/_/postgres) 



