from db_handler import *
import signals

signals = signals.Signals()
db = DBHandler(signals)


recipe = db.find_recipe("Icarus's Wings", 1)
# for item in recipe:
#     print(f'{item}: {recipe[item]}')

# try:
#     bi = set()
#     for a in BasicItems.select():
#         bi.add(a.name)

#     ci = set()
#     for a in CraftedItems.select():
#         ci.add(a.name)

#     end = set()
#     for a in BL.select().where(BL.item.not_in(bi)&BL.item.not_in(ci)):
#         end.add(a.item)

#     for a in end:
#         print(a)
# finally:
#     db.close()