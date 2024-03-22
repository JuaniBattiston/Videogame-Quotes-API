import random
from fastapi import FastAPI
from starlette.requests import Request
from quotes import quote_dict
from typing import Dict, List
from response import JSONResponseObject
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/", response_class=JSONResponseObject)
@limiter.limit("5/minute")
def home(request: Request) -> Dict:
    """API's homepage"""
    return {
        "API": "Videogame quotes API",
        "version": "1.0.1",
        "author": "Batucho",
        "repository-url": "https://github.com/Batucho/Videogame-Quotes-API",
    }


@app.get("/quotes", response_class=JSONResponseObject)
@limiter.limit("5/minute")
def get_random_quote(request: Request) -> Dict:
    """Returns a single random quote"""
    quote = random.choice(quote_dict["quotes"])
    return quote


@app.get("/quotes/{number}", response_class=JSONResponseObject)
@limiter.limit("5/minute")
def get_random_quote(number: int,request: Request) -> List[Dict]:
    """Returns a number of random quotes"""
    quotes = random.choices(quote_dict["quotes"], k=number)
    return [quote for quote in quotes]


@app.get("/all", response_class=JSONResponseObject)
@limiter.limit("5/minute")
def get_all_quotes(request: Request) -> List[Dict]:
    """Returns a list of all stored quotes"""
    return [quote for quote in quote_dict["quotes"]]
