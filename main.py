from fastapi import FastAPI
from classes.Annabel import Annabel
from classes.Toffler import Toffler

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello world"}

@app.get("/annabel")
async def read_annabel():
    annabel = Annabel.scrapeAnnabel()
    return annabel


# for event in toffler:
#     print(event.title, "Title")
#     print(event.artist, "Artist")
#     print(event.date, "Date")
