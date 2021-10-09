import random
from fastapi import FastAPI
from quotes import quote_dict
from typing import Dict, List
from response import JSONResponseObject

app = FastAPI()


@app.get("/", response_class=JSONResponseObject)
def home() -> Dict:
    """API's homepage"""
    return {
        "API": "Videogame quotes API",
        "version": "1.0.0",
        "author": "Batucho",
        "repository-url": "https://github.com/Batucho/Videogame-Quotes-API",
    }


@app.get("/quotes", response_class=JSONResponseObject)
def get_random_quote() -> Dict:
    """Returns a single random quote"""
    quote = random.choice(quote_dict["quotes"])
    return quote


@app.get("/quotes/{number}", response_class=JSONResponseObject)
def get_random_quote(number: int) -> List[Dict]:
    """Returns a number of random quotes"""
    quotes = random.choices(quote_dict["quotes"], k=number)
    return [quote for quote in quotes]


@app.get("/all", response_class=JSONResponseObject)
def get_all_quotes() -> List[Dict]:
    """Returns a list of all stored quotes"""
    return [quote for quote in quote_dict["quotes"]]
