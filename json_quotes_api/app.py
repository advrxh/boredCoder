from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from pathlib import Path
import json
import random

from html_templates import HOME_PAGE

app = FastAPI(title="Json Quotes Api")

with Path('quotes.json').open('r+', encoding='utf-8') as f:
    QUOTES = json.load(f)['quotes']

@app.get('/')
async def root():
    QUOTE = random.choice(QUOTES)
    return HTMLResponse(HOME_PAGE.replace('{author}',QUOTE['author'] ).replace('{quote}', QUOTE['quote']))

@app.get('/quote')
@app.get('/quote/random')
async def quote_random():
    return random.choice(QUOTES)

@app.get('/quote/{id}')
async def quote_by_id(id:int):
    try:
        quote = QUOTES[id]
        return quote
    except IndexError:
        return {'msg' : 'Error, invalid quote ID'}

@app.get('/quotes')
async def quotes():
    return QUOTES
