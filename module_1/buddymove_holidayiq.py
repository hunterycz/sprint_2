import sqlite3
import pandas as pd

# import the csv to a dataframe
df = pd.read_csv('buddymove_holidayiq.csv')
# create a connection to the sql database
connection = sqlite3.connect('buddymove_holidayiq.sqlite3')
# use pd.to_sql to send df to the sql database
df.to_sql(name='review', con=connection)

NUM_OF_ROWS = 'SELECT COUNT(*) AS num_rows FROM review'
NATURE_SHOPPING_100 = '''SELECT COUNT(*) AS num_user_100 FROM review
                         WHERE Nature > 100 AND Shopping > 100;'''
AVG_REVIEWS_EACH_CATEGORY = '''SELECT AVG(Sports), AVG(Religious),
                               AVG(Nature), AVG(Theatre), AVG(Shopping),
                               AVG(Picnic) FROM review'''
