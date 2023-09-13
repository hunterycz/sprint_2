import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_q(conn, query):
    # Make the "cursor"
    curs = conn.cursor()
    # Execute the query
    curs.execute(query)
    # Pull (and return) the results
    return curs.fetchall()


SELECT_ALL = 'SELECT  character_id, name FROM charactercreator_character;'

AVG_ITEM_PER_CHARACTER = '''SELECT cc_char.name, AVG(ai.weight)
                            FROM charactercreator_character AS cc_char
                            JOIN charactercreator_character_inventory AS cc_inv
                            ON cc_char.character_id = cc_inv.character_id
                            JOIN armory_item AS ai
                            ON ai.item_id = cc_inv.item_id
                            GROUP BY cc_char.character_id
                            '''
TOTAL_CHARACTERS = '''SELECT COUNT(name) as total_characters FROM
                      charactercreator_character'''
TOTAL_NECROMANCERS = '''SELECT COUNT(character_id) AS num_necromancers
                        FROM charactercreator_character AS cc_char
                        JOIN charactercreator_necromancer AS ccn
                        ON cc_char.character_id = ccn.mage_ptr_id'''
TOTAL_ITEMS = '''SELECT COUNT(DISTINCT name) AS
                 num_unique_items FROM armory_item'''
WEAPONS = '''SELECT COUNT(name) AS num_weapons FROM armory_item AS ai
             JOIN armory_weapon AS aw
             ON ai.item_id = aw.item_ptr_id'''
NON_WEAPONS = '''SELECT COUNT( name) AS num_non_weapons
                 FROM armory_item AS ai
                 LEFT JOIN armory_weapon AS aw
                 ON ai.item_id = aw.item_ptr_id
                 WHERE item_ptr_id IS NULL'''
CHARACTER_ITEMS = '''SELECT name, COUNT(item_id) AS num_items FROM
                     charactercreator_character AS cc_char
                     LEFT JOIN charactercreator_character_inventory
                     AS cci ON cc_char.character_id = cci.character_id
                     GROUP BY item_id LIMIT 20;'''
CHARACTER_WEAPONS = '''SELECT name, COUNT(*) AS  num_weapons FROM
                       charactercreator_character AS cc_char
                       LEFT JOIN charactercreator_character_inventory AS cci
                       ON cc_char.character_id = cci.character_id
                       JOIN armory_weapon AS aw ON cci.item_id = aw.item_ptr_id
                       GROUP BY name LIMIT 20;
                       '''
AVG_CHARACTER_ITEMS = '''SELECT COUNT(*) / COUNT(DISTINCT name)
                         AS avg_num_item_character
                         FROM charactercreator_character AS cc_char
                         LEFT JOIN charactercreator_character_inventory AS cci
                         ON cc_char.character_id = cci.character_id
                         '''
AVG_CHARACTER_WEAPONS = '''SELECT COUNT(item_id) / COUNT(name) AS
                           num_weapons_character FROM
                           charactercreator_character AS cc_char
                           LEFT JOIN charactercreator_character_inventory
                           AS cci ON cc_char.character_id =
                           cci.character_id JOIN armory_weapon AS aw
                           ON cci.item_id = aw.item_ptr_id
                           '''

QUERY_LIST = [SELECT_ALL, AVG_ITEM_PER_CHARACTER, TOTAL_CHARACTERS,
              TOTAL_NECROMANCERS, TOTAL_ITEMS, WEAPONS, NON_WEAPONS,
              CHARACTER_ITEMS, CHARACTER_WEAPONS, AVG_CHARACTER_ITEMS,
              AVG_CHARACTER_WEAPONS]

if __name__ == '__main__':
    for query in QUERY_LIST:
        conn = connect_to_db()
        results = execute_q(conn, query)
        print(results)
