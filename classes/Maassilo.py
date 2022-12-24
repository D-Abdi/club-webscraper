import requests
from bs4 import BeautifulSoup


class Maassilo:
    def __init__(self, title, location, date):
        self.title = title
        self.location = location
        self.date = date

    def scrape():
        URL = "https://www.maassilo.com/now-and-wow-club"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        siteInfo = soup.find_all("div", class_="events")

        dataList = []

        for info in siteInfo:
            date_element = info.find("p").text
            date_element = date_element.strip()
            title_element = info.find("a").text
            title_element = title_element.strip()
            p_elements = info.find_all(
                "p", string=lambda text: "Locatie:"
            )
            location_element = p_elements[3].text

            eventInfo = Maassilo(title_element, location_element, date_element)
            dataList.append(eventInfo)

        return dataList

    def clubInfo():
        return {
            "name": "Maassilo / Now&Wow",
            "location": "Rotterdam, Netherlands",
            "description": "Maassilo, een 100 jaar oude graanssilo. Maassilo bestaat uit een complex van totaal 3 silo's die in een tijdsbestek van 50 jaar aan de Maashaven Zuidzijde zijn gebouwd. Een unieke eventlocatie aan de zuidzijde van Rotterdam.",
            "address": "Maashaven Zuidzijde 1-2, 3081 AE",
            "events": Maassilo.scrape()
        }
