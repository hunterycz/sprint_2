from sqlite_example import connect_to_db, execute_q
from mongo import mongo_connect
import queries as q

# credentials
DBNAME = 'rpg_data'
PASSWORD = 'Hunter3472'

# connect to mongodb and create a collection named 'characters'
mongo_connect(PASSWORD, DBNAME, collection_name='characters')

# query to get all characters names with
# id, item_id, item_name, and character_name
ARMORY_ITEMS = '''
SELECT cc_char.character_id, cc_char.name as character_name,
 ai.name as item_name, ai.item_id, aw.power
FROM charactercreator_character as cc_char
LEFT JOIN charactercreator_character_inventory as cc_inv
ON cc_inv.character_id = cc_char.character_id
LEFT JOIN armory_item as ai
ON cc_inv.item_id = ai.item_id
LEFT JOIN armory_weapon as aw
ON ai.item_id = aw.item_ptr_id
'''


if __name__ == '__main__':
    collection = mongo_connect(PASSWORD, DBNAME, collection_name='characters')
    # use to drop all documents in collection
    # collection.drop()

    # connect to sqlite and query all characters
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, q.GET_CHARACTERS)
    sl_items = execute_q(sl_conn, ARMORY_ITEMS)

    # for loop to create a document of each character
    # with their name, level, exp, hp, strength,
    # intelligence, dexterity, wisdom, item names
    # in a list, and weapons name in a list
    for character in sl_characters:
        name = character[1]
        item_list = []
        weapon_list = []

        mongo_doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8]
        }

        for i in range(len(sl_items)):
            if sl_items[i][1] == name:
                item_list.append(sl_items[i][2])
                if type(sl_items[i][4]) == int:
                    weapon_list.append(sl_items[i][2])

        mongo_doc["items"] = item_list
        mongo_doc["weapons"] = weapon_list
        collection.insert_one(mongo_doc)
