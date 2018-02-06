from peewee import *


db = SqliteDatabase('Users.db')


class User(Model):
    username = CharField(max_length=20, unique=True)
    name = CharField(max_length=20)
    address = TextField()
    phone_number = CharField(max_length=15)
    email_address = TextField()
    experience_one = TextField()
    edu_degree = TextField()
    edu_completion_date = IntegerField()
    edu_university = TextField()
    edu_location = TextField()

    def get_employment(self):
        return Employment.select().where(Employment.user == self)

    class Meta:
        database = db


class Employment(Model):
    user = ForeignKeyField(rel_model=User)
    job_title = TextField()
    job_duration = CharField(max_length=20)
    job_company = CharField(max_length=30)
    job_location = TextField()
    employment_bullet_1 = TextField()
    employment_bullet_2 = TextField()
    employment_bullet_3 = TextField()


    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([User, Employment], safe=True)
