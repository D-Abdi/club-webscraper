import requests
from bs4 import BeautifulSoup


class Annabel:
    def __init__(self, title, date, img, link):
        self.title = title
        self.date = date
        self.img = img
        self.link = link

    def __str__(self):
        return f"{self.title} {self.date} {self.img} {self.link}"

    def scrape():
        URL = "https://www.annabel.nu/maandagenda/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        siteInfo = soup.find_all("div", class_="column")

        dataList = []

        for info in siteInfo:
            link_element = info.find("a")["href"]
            img_element = info.find("img")
            img_src= str(img_element['src'])
            title_element = info.find("h1").text
            title_element = str(title_element)
            date_element = info.find("p").text
            date_element = str(date_element)
            eventInfo = Annabel(title_element, date_element, img_src, link_element)
            dataList.append(eventInfo)

        return dataList

    def clubInfo():
        return {
            "name": "Annabel",
            "location": "Rotterdam, Netherlands",
            "description": "Welkom in het grootste poppodium van Rotterdam, op een steenworp afstand van Rotterdam Centraal. Je kan hier internationale, toonaangevende acts zien en horen, van hiphop tot pop tot elektronisch. Kom een biertje drinken op het terras of kom gewoon lekker dansen tijdens één van de vele feestjes of festivals.",
            "address": "Schiestraat 20, 3013 AH",
            "events": Annabel.scrape()
        }
