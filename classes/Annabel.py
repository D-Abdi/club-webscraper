import requests
from bs4 import BeautifulSoup

class Annabel:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def __str__(self):
        return f"{self.title} {self.date}"  

    def scrapeAnnabel():
        URL = "https://www.annabel.nu/maandagenda/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        siteInfo = soup.find_all("div", class_="small info")

        dataList = []

        for info in siteInfo:
            title_element = info.find("h1").text
            title_element = str(title_element)
            date_element = info.find("p").text
            date_element = str(date_element)
            eventInfo = Annabel(title_element, date_element)
            dataList.append(eventInfo)

        return dataList