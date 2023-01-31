from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from database.databaseManager import *

app = FastAPI()


@app.get("/")
def root():
    return {"status": 200}


@app.get("/link/{short_link}")
def redirect(short_link: str):
    link = redirect_link(link_id=short_link)
    if link['status'] == 200:
        return RedirectResponse(link['redirect_to'])
    else:
        return {'status': link['status']}


@app.get("/short")
def short_link(url: Union[str, None] = None):
    link = create_link(url)

    if link['status'] == 200:
        return {"status": link['status'], "link": link['link']}
    else:
        return {'status': link['status']}
