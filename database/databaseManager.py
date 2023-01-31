from mongoengine import *

from database.dto.url import Url

from random import choice
from string import digits, ascii_lowercase, ascii_uppercase

from config import config

connect(
    host=config['mongo_link'],
    alias="default"
)

def create_link(link: str) -> dict:
    try:
        short_link_random = [choice(ascii_lowercase + digits if i != 5 else ascii_uppercase) for i in range(7, 16)]
        link = Url(name=''.join(short_link_random), redirect_to=link)
        link.save()

        short_link = config['domain']+"/link/"+''.join(short_link_random)


        return {"status": 200, "link": short_link}
    except errors.NotUniqueError:
        return {"status": 400}

def redirect_link(link_id: str) -> dict:
    try:
        link = Url.objects.get(name=link_id)
        if link is not None:
            return {"status": 200, "redirect_to": link.redirect_to}
    except errors.DoesNotExist:
        return {"status": 400}
