from datetime import date

import peewee

db = peewee.SqliteDatabase(r'..\db\database.sqlite3')


class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Profession(BaseModel):
    profession = peewee.CharField(null=False)
    experience = peewee.IntegerField(default=0)
    wage = peewee.FloatField(null=False)

    class Meta:
        db_table = 'professions'


class Staff(BaseModel):
    firs_name = peewee.CharField(null=False)
    last_name = peewee.CharField(null=False)
    profession_id = peewee.ForeignKeyField(Profession)

    class Meta:
        db_table = 'staff'


class Maker(BaseModel):
    company_name = peewee.CharField(null=False)
    company_description = peewee.TextField()
    company_number = peewee.CharField(default='')

    class Meta:
        db_table = 'makers'


class Medicine(BaseModel):
    name = peewee.CharField(null=False)
    description = peewee.TextField(null=False)
    price = peewee.FloatField(null=False)
    date_of_manufacture = peewee.DateField(null=False, default=date(2020, 1, 1))
    shelf_life = peewee.DateField(null=False, default=date(2021, 1, 1))
    maker_id = peewee.ForeignKeyField(Maker)

    class Meta:
        db_table = 'medicines'

