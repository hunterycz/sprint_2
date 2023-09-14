SELECT_ALL = 'SELECT  character_id, name FROM charactercreator_character;'

AVG_ITEM_PER_CHARACTER = '''
SELECT cc_char.name, AVG(ai.weight)
FROM charactercreator_character AS cc_char
JOIN charactercreator_character_inventory AS cc_inv
ON cc_char.character_id = cc_inv.character_id
JOIN armory_item AS ai
ON ai.item_id = cc_inv.item_id
GROUP BY cc_char.character_id
'''
TOTAL_CHARACTERS = '''
SELECT COUNT(name) as total_characters
FROM charactercreator_character
'''
TOTAL_NECROMANCERS = '''
SELECT COUNT(*)
FROM charactercreator_necromancer
'''
TOTAL_ITEMS = '''
SELECT COUNT(DISTINCT name) AS
num_unique_items FROM armory_item
'''
WEAPONS = '''SELECT COUNT(*) FROM armory_weapon'''
NON_WEAPONS = '''
SELECT COUNT( name) AS num_non_weapons
FROM armory_item AS ai
LEFT JOIN armory_weapon AS aw
ON ai.item_id = aw.item_ptr_id
WHERE item_ptr_id IS NULL
'''
CHARACTER_ITEMS = '''
SELECT name, COUNT(item_id) AS num_items
FROM charactercreator_character AS cc_char
INNER JOIN charactercreator_character_inventory AS cc_inv
ON cc_char.character_id = cc_inv.character_id
GROUP BY cc_char.character_id
LIMIT 20;
'''
CHARACTER_WEAPONS = '''
SELECT name, COUNT(*) AS  num_weapons FROM
charactercreator_character AS cc_char
LEFT JOIN charactercreator_character_inventory AS cci
ON cc_char.character_id = cci.character_id
JOIN armory_weapon AS aw ON cci.item_id = aw.item_ptr_id
GROUP BY name LIMIT 20;
'''
AVG_CHARACTER_ITEMS = '''
SELECT AVG(num_items) AS average_items
FROM (SELECT name, COUNT(item_id) AS num_items
FROM charactercreator_character AS cc_char
INNER JOIN charactercreator_character_inventory AS cc_inv
ON cc_char.character_id = cc_inv.character_id
GROUP BY cc_char.character_id)
'''
AVG_CHARACTER_WEAPONS = '''
SELECT AVG(total_weapons) AS average_weapons
FROM (SELECT cc_char.name, COUNT(ai.item_id) AS total_weapons
FROM armory_item as ai
INNER JOIN armory_weapon as aw
ON ai.item_id = aw.item_ptr_id
--37 weapons
INNER JOIN charactercreator_character_inventory as cc_inv
ON ai.item_id = cc_inv.item_id
--203 weapons
INNER JOIN charactercreator_character as cc_char
ON cc_char.character_id = cc_inv.character_id
GROUP BY cc_char.character_id)
'''

QUERY_LIST = [SELECT_ALL, AVG_ITEM_PER_CHARACTER, TOTAL_CHARACTERS,
              TOTAL_NECROMANCERS, TOTAL_ITEMS, WEAPONS, NON_WEAPONS,
              CHARACTER_ITEMS, CHARACTER_WEAPONS, AVG_CHARACTER_ITEMS,
              AVG_CHARACTER_WEAPONS]
