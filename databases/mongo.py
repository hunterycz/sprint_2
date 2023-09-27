import pymongo
from sqlite_example import connect_to_db, execute_q
import queries as q

test_characters = [(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1),
                   (2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1)
                   
]

character_documents = [
    {
    'character_id': 1,
    'name': 'Aliquid iste optio reiciendi',
    'level': 0,
    'exp': 0,
    'hp': 10,
    'strength': 1,
    'intelligence': 1,
    'dexterity': 1,
    'wisdom': 1
    },
    {
    'character_id': 1,
    'name': 'Aliquid iste optio reiciendi',
    'level': 0,
    'exp': 0,
    'hp': 10,
    'strength': 1,
    'intelligence': 1,
    'dexterity': 1,
    'wisdom': 1
    }
]

# credentials
DBNAME = 'test'
PASSWORD = 'Hunter3472'


def mongo_connect(password, dbname, collection_name='characters'):
    client = pymongo.MongoClient(f'mongodb+srv://hunterpeterson410:{password}@cluster0.nglzk5i.mongodb.net/{dbname}?retryWrites=true&w=majority')
    db = client[dbname]
    collection = db[collection_name]

    return collection


mongo_connect(PASSWORD, DBNAME, collection_name='characters')


if __name__ == '__main__':

    # Get data from SQLite
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, q.GET_CHARACTERS)
    # print(sl_characters[:3])

    # connect to a specific mongodb collection
    collection = mongo_connect(collection_name='characters')

    for character in sl_characters:
        doc = {
        'character_id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
        }

        collection.insert_one(doc)
