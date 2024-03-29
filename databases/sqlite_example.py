# step 0 - import sqlite3
import sqlite3
import queries as q
import pandas as pd

# DB Connect function


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_q(conn, query):
    # Make the "cursor"
    curs = conn.cursor()
    # Execute the query
    curs.execute(query)
    # Pull (and return) the results
    return curs.fetchall()


if __name__ == '__main__':
    conn = connect_to_db()
    print(execute_q(conn, q.GET_CHARACTERS)[:2])
    # results = execute_q(conn, q.GET_CHARACTERS)
    # df = pd.DataFrame(results)
    # df.columns = ['name', 'average_item_weight']
    # print(df.head())
    # df.to_csv('rpg_db.csv', index=False)
