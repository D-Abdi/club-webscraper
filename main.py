from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

from classes.Annabel import Annabel
from classes.Toffler import Toffler
from classes.Maassilo import Maassilo

app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5173/clubs",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/clubs")
async def read_clubs():
    return [
        Annabel.clubInfo(),
        Toffler.clubInfo(),
        Maassilo.clubInfo()
    ]


@app.get("/clubs/annabel")
async def read_annabel():
    return Annabel.scrape()


@app.get("/clubs/toffler")
async def read_toffler():
    return Toffler.scrape()


@app.get("/clubs/maassilo")
async def read_maassilo():
    return Maassilo.scrape()


Maassilo.scrapeEvent("https://www.maassilo.com/agenda/tiktak-new-years-eve")
