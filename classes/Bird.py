import requests
from bs4 import BeautifulSoup

class Bird:
    def __init__(self, title, artist, date, img, link):
        self.title = title
        self.artist = artist
        self.date = date
        self.img = img
        self.link = link

    def scrape():
        URL = "https://bird-rotterdam.nl/agenda/#filter=.club"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        siteInfo = soup.find_all("div", class_="club")

        dataList = []

        for info in siteInfo:
            a_element = info.find("a", class_="ticketbtn")
            if (a_element):
                ticket_element = a_element["href"]
            date_element = info.find("h2", class_="date")
            if(date_element):
                date_element = date_element.text
            else:
                date_element = "TBA"
            title_element = info.find("h2", class_="toptitle")
            if(title_element):
                title_element = title_element.text
            else:
                title_element = "Bird Podium"
            highlight_element = info.find("h1", class_="highlight")
            if(highlight_element):
                artist_element = highlight_element.text
            img_src = info.find("div", class_="image")
            if(img_src and img_src["data-src"] != None):
                image_element = img_src["data-src"]
            
            eventInfo = Bird(title_element + " - " + artist_element, artist_element, date_element, image_element, ticket_element)
            dataList.append(eventInfo)

        return dataList

    def clubInfo():
        return {
            "clubName": "birdpodium",
            "name": "Bird Podium",
            "location": "Rotterdam, Netherlands",
            "description": "Diepgeworteld in de jazz, maar met vertakkingen als soul, funk, hiphop en elektronica is podium, club en restaurant BIRD dé plek voor de culturele alleseter.",
            "address": "Raampoortstraat 24, 3032 AH",
            "events": Bird.scrape()
        }




        