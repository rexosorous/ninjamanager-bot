import peewee



db = peewee.SqliteDatabase('items.db', pragmas={
            'journal_mode': 'wal',
            'cache_size': -1 * 64000,
            'foreign_keys': 1,
            'ignore_check_counstraints': 0,
            'synchronous': 0
            })



class BaseModel(peewee.Model):
    class Meta:
        database = db

class LW(BaseModel):
    # legendary weapons without a recipe
    name = peewee.CharField()
    location = peewee.CharField() # link to the world area
    mission = peewee.CharField() # mission number
    chance = peewee.CharField() # percent chance to find item

class CraftedLW(BaseModel):
    # crafted legendary weapons
    name = peewee.CharField()
    item = peewee.CharField()
    amount = peewee.SmallIntegerField()

class BL(BaseModel):
    # blodlines
    name = peewee.CharField()
    item = peewee.CharField()
    amount = peewee.SmallIntegerField()

class CraftedItems(BaseModel):
    # items which are crafted from other items
    name = peewee.CharField()
    item = peewee.CharField()
    amount = peewee.SmallIntegerField()

class BasicItems(BaseModel):
    # items which are found in world missions
    name = peewee.CharField()
    location = peewee.CharField()
    mission = peewee.CharField()
    chance = peewee.CharField()





class DBHandler:
    def __init__(self, signals):
        self.db = db
        self.db.connect()
        self.signals = signals



    def get_dropped_lws(self) -> dict:
        data = {}
        for dropped_LW in LW.select():
            data[dropped_LW.name] = {
                'location': dropped_LW.location,
                'mission': dropped_LW.mission,
                'chance': dropped_LW.chance
            }
        return data



    def get_crafted_lws(self) -> [str]:
        LWs = set()
        for lw in CraftedLW.select():
            LWs.add(lw.name)
        return list(LWs)



    def get_bls(self) -> [str]:
        BLs = set()
        for bl in BL.select():
            BLs.add(bl.name)
        return list(BLs)



    def find_locations(self, item: str) -> [dict]:
        # returns all the locations where you can find a basic item
        return_me = []
        locations = BasicItems.select().where(BasicItems.name==item)
        for entry in locations:
            temp_dict = {}
            temp_dict['location'] = entry.location
            temp_dict['mission'] = entry.mission
            temp_dict['chance'] = entry.chance
            return_me.append(temp_dict)

        return return_me



    def find_recipe(self, item: str, amount: int) -> dict:
        # outputs all the basic items and their amounts and edits gui along the way
        recipe = {}

        # check basic items first
        basic = BasicItems.select().where(BasicItems.name==item)
        if len(basic) > 0:
            recipe[item] = 1

            # determine which mission is the best out of all the options
            best_item = {'location':'', 'mission':'', 'chance':0}
            for i in basic:
                if float(i.chance[:-1]) > best_item['chance']:
                    best_item['location'] = i.location
                    best_item['mission'] = i.mission
                    best_item['chance'] = float(i.chance[:-1])

            self.signals.area_signal.emit(best_item) # edit options window gui

        # recursion
        for table in [CraftedItems, CraftedLW, BL]:
            if recipe:
                break
            for next_item in table.select().where(table.name==item):
                self.signals.recipe_signal.emit(item, next_item.item, next_item.amount)
                recipe = self.merge_dicts(recipe, self.find_recipe(next_item.item, next_item.amount))

        # handles things like level 10 itachi
        if not recipe:
            recipe[item] = 1

        for item in recipe:
            recipe[item] *= amount
        return recipe



    def merge_dicts(self, a: dict, b: dict) -> dict:
        # merges two dicts together and combines values if there are matching keys
        for key in b:
            if key not in a.keys():
                a[key] = b[key]
            elif key in a.keys():
                a[key] += b[key]
        return a



    def close(self):
        self.db.close()