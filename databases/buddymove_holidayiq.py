import sqlite3
import pandas as pd

# import the csv to a dataframe
df = pd.read_csv('buddymove_holidayiq.csv')
# create a connection and a cursor to the sql database
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
# use pd.to_sql to send df to the sql database


if __name__ == '__main__':
    # turn the DF into a table called 'review'
    df.to_sql(name='review', con=conn, if_exists='replace')

    # Query the table to ensure that the data was truly added.
    curs.execute('''SELECT * FROM review;''')
    # print(curs.fetchall())

    # Nature and Shopping both >= 100
    NATURE_SHOPPING = '''
    SELECT COUNT(*) AS num_user_100
    FROM review
    WHERE Nature > 100 AND Shopping > 100;
    '''

    # Average reviews from each category
    AVG_REVIEWS_EACH_CATEGORY = '''
    SELECT AVG(Sports), AVG(Religious),
    AVG(Nature), AVG(Theatre),
    AVG(Shopping), AVG(Picnic) FROM review
    '''

    # Number of rows
    NUM_OF_ROWS = '''
    SELECT COUNT(*) AS num_rows
    FROM review
    '''
