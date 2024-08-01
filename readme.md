# Launch and interact with a SQL database server via a web UI

The main goal of this project is to use PostegreSQL, one of the oldest Structured Query Languages, to implement a data server that can accept queries for retreival and augmentation from the local computer network.

Sub goals in the project consist of making sure the data is persistent, that the database server launches on bootup from a linux computer, and that the project can launch from a pc or mac that has docker desktop running. Of course I also want to learn some PostreSQL queries. 

## Dependencies

Python libraries
- `streamlit`: to create the user interface with pure python
- `psycopg2`: to query the SQL database
- `psycopg2-binary`: also needed for querying the database

Docker
- I am opting for the alpine linux docker cotnainer for a small footprint. 
- Heres the image: PostgreSQL has an [official docker image](https://hub.docker.com/_/postgres) 



