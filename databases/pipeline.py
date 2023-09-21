import psycopg2
from sqlite_example import connect_to_db, execute_q
from queries import DROP_CHARACTER_TABLE, CREATE_CHARACTER_TABLE
from queries import GET_CHARACTERS
# PostgreSQL Connection Credentials

# "User and Default Database" from ElephantSQL
# DBNAME = 'hkddulhy'
# USER = 'hkddulhy'
# # "Password" from ElephantSQL
# PASSWORD = 'qBW6H-7E0vuvFTBaiYDQFtTWEZ2om4tr'
# # "Server" from ElephantSQL
# HOST = 'bubble.db.elephantsql.com'


def connect_to_pg(DBNAME, USER, PASSWORD, HOST):
    pg_conn = psycopg2.connect(
                                dbname=DBNAME, user=USER,
                                password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()

    return pg_conn, pg_curs


def modify_db(conn, curs, query):
    curs.execute(query)
    conn.commit()


if __name__ == '__main__':

    # Get data from SQLite
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, GET_CHARACTERS)

    # Create destination talbe within PostgreSQL DB
    pg_conn, pg_curs = connect_to_pg()
    # modify_db(pg_conn, pg_curs, DROP_CHARACTER_TABLE)
    # modify_db(pg_conn, pg_curs, CREATE_CHARACTER_TABLE)
    modify_db(pg_conn, pg_curs, '''ALTER TABLE characters
                                   RENAME TO charactercreator_character ''')

    # print(sl_characters[0][1])

    # Loop over characters and insert into PostgreSQL with correct values
    # for character in sl_characters:
    #     modify_db(pg_conn, pg_curs,
    #             f'''
    #                 INSERT INTO characters ("name", "level",
    #                                         "exp", "hp", "strength",
    #                                         "intelligence", "dexterity",
    #                                         "wisdom")
    #                 VALUES ('{character[1]}', {character[2]},
    #                          {character[3]}, {character[4]},
    #                          {character[5]}, {character[6]},
    #                          {character[7]}, {character[8]});
    #                 '''
    #               )

