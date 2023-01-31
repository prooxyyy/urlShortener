from database.databaseManager import *

class Url(Document):
    name = StringField(required=True, max_length=16, unique=True)
    redirect_to = StringField(required=True)