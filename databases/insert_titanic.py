import psycopg2
from pipeline import connect_to_pg, modify_db
import pandas as pd

# "User and Default Database" from elephantSQL
DBNAME_TITANIC = 'btzpiyhl'
USER_TITANIC= 'btzpiyhl'

# Password from elephantSQL
PASSWORD_TITANIC = 'CZu9LCl1izSeLga7tJSWxIoifug5iRCR'

# "Server" from elephantSQL
HOST_TITANIC = 'bubble.db.elephantsql.com'

# import titanic.csv as pandas dataframe
df = pd.read_csv('titanic_modified.csv')

# use connect_to_pg function 
# to connect db in elephantSQL
pg_conn, pg_curs = connect_to_pg(
                            DBNAME_TITANIC,
                            USER_TITANIC,
                            PASSWORD_TITANIC,
                            HOST_TITANIC)

current_table = 'titanic_survived'

# queries to create tables elephantSQL
DROP_TABLE = f'''
DROP TABLE IF EXISTS {current_table}
'''

PASSENGER_STRUCTURE = '''
CREATE TABLE IF NOT EXISTS titanic_passengers
(
"passenger_id" SERIAL NOT NULL PRIMARY KEY,
"name" VARCHAR(100),
"age" FLOAT NOT NULL,
"fare" FLOAT NOT NULL,
"sex" VARCHAR(6) NOT NULL
);
'''
PCLASS1_STRUCTURE = '''
CREATE TABLE IF NOT EXISTS titanic_pclass1
(
"passenger_p1_id" INT NOT NULL,
"pclass" INT NOT NULL
)
'''

PCLASS2_STRUCTURE = '''
CREATE TABLE IF NOT EXISTS titanic_pclass2
(
"passenger_p2_id" INT NOT NULL,
"pclass" INT NOT NULL
)
'''

PCLASS3_STRUCTURE = '''
CREATE TABLE IF NOT EXISTS titanic_pclass3
(
"passenger_p3_id" INT NOT NULL,
"pclass" INT NOT NULL
)
'''

SURVIVED_STRUCTURE = '''
CREATE TABLE IF NOT EXISTS titanic_survived
(
"passenger_id" SERIAL NOT NULL PRIMARY KEY,
"survived" INT NOT NULL
)
'''

if __name__ == '__main__':

    # use modify_db to change the db in elephantSQL
    modify_db(pg_conn, pg_curs, PASSENGER_STRUCTURE)

    # add in data into passenger table
    for i in range(len(df)):
        name = df['Name'][i].replace("'", "''")
        modify_db(pg_conn, pg_curs,
                  f'''INSERT INTO titanic_passengers ("name",
                                                      "age",
                                                      "fare",
                                                      "sex")
                       VALUES ('{name}', {df['Age'][i]},
                                {df['Fare'][i]}, '{df['Sex'][i]}');
        ''')

    # use modify_db to create the table Pclass1
    modify_db(pg_conn, pg_curs, PCLASS1_STRUCTURE)

    # add in data in the titanic_pclass1 table
    for i in range(len(df)):
        if df['Pclass'][i] == 1:
            modify_db(pg_conn, pg_curs,
                    f'''INSERT INTO titanic_pclass1 ("passenger_p1_id",
                                                    "pclass")
                        VALUES ({df['idx'][i]}, {df['Pclass'][i]});
            ''')

    # use modify_db to create the table Pclass2
    modify_db(pg_conn, pg_curs, PCLASS2_STRUCTURE)

    # add in data in the titanic_pclass1 table
    for i in range(len(df)):
        if df['Pclass'][i] == 2:
            modify_db(pg_conn, pg_curs,
                    f'''INSERT INTO titanic_pclass2 ("passenger_p2_id",
                                                    "pclass")
                        VALUES ({df['idx'][i]}, {df['Pclass'][i]});
            ''')

    # use modify_db to create the table Pclass3
    modify_db(pg_conn, pg_curs, PCLASS3_STRUCTURE)

    # # add in data in the titanic_pclass1 table
    for i in range(len(df)):
        if df['Pclass'][i] == 3:
            modify_db(pg_conn, pg_curs,
                    f'''INSERT INTO titanic_pclass3 ("passenger_p3_id",
                                                     "pclass")
                        VALUES ({df['idx'][i]}, {df['Pclass'][i]}); ''')

    # use modify_db to create the titanic_survived table
    modify_db(pg_conn, pg_curs, SURVIVED_STRUCTURE)

    # add in the data in the titanic_survived table
    for i in range(len(df)):
        modify_db(pg_conn, pg_curs,
                  f'''INSERT INTO titanic_survived ("survived")
                      VALUES ({df['Survived'][i]})
        ''')
