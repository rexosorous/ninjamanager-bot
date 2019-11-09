import peewee



db = peewee.SqliteDatabase('items.db')



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
    def __init__(self):
        self.db = db
        self.db.connect()