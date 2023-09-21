import psycopg2
from os import getenv
import pandas as pd

# info needed to connect and interact
# with a database
DBNAME = getenv('DBNAME')
USER = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')

# make out postgres connection
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, 
                           password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()


def execute_query_pg(curs, conn, query):
    results = curs.execute(query)
    conn.commit()
    return results


CREATE_TITANIC_TABLE = '''
CREATE TABLE IF NOT EXISTS titanic_table(
    "passenger_id" SERIAL PRIMARY KEY,
    "survived" INT NOT NULL,
    "pclass" INT NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "sex" VARCHAR(10) NOT NULL,
    "age" FLOAT NOT NULL,
    "siblings_spouses_aboard" INT NOT NULL,
    "parents_children_aboard" INT NOT NULL,
    "fare" FLOAT NOT NULL
);
'''

DROP_TITANIC_TABLE = '''
    DROP TABLE IF EXISTS titanic_table;
'''

df = pd.read_csv('titanic.csv')
# removing any single quotes in the Name column
df['Name'] = df['Name'].str.replace("'", "")

if __name__ == '__main__':
    # create the table and its associated Schema
    # drop table
    execute_query_pg(pg_curs, pg_conn, DROP_TITANIC_TABLE)
    # create table
    execute_query_pg(pg_curs, pg_conn, CREATE_TITANIC_TABLE)

    records = df.values.tolist()
    
    for record in records:
        insert_statement = f'''
            INSERT INTO titanic_table (survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children_aboard, fare)
            VALUES {tuple(record)};
        '''
        execute_query_pg(pg_curs, pg_conn, insert_statement)
