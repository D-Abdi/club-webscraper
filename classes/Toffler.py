import requests
from bs4 import BeautifulSoup

class Toffler:
    def __init__(self, title, artist, date):
        self.title = title
        self.artist = artist
        self.date = date

    def __str__(self) -> str:
        return f"{self.title} {self.artist} {self.date}"

    def scrapeToffler():
        URL = "https://www.toffler.nl/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        siteInfo = soup.find_all("li", class_="event")

        dataList = []

        for info in siteInfo:
            date_element = info.find("span", class_="event_date")
            # print(date_element, "Date")
            day_element = date_element.find("i").text
            day_number_element = date_element.find("em").text
            month_element = date_element.find("b").text
            title_h1_element = info.find("h1", class_="event_title")
            title_h1 = str(title_h1_element)
            title_h1 = title_h1.replace('<h1 class="event_title">', '')
            title_h1 = title_h1.replace('</h1>', '')       

            title_h2_element = info.find("h2", class_="event_title")
            title_h2 = str(title_h2_element)
            title_h2 = title_h2.replace('<h2 class="event_title">', '')
            title_h2 = title_h2.replace('</h2>', '')

            artist_element = info.find("strong", class_="event_excerpt").text

            title_element = "";
            if (title_h1 != "None"): 
                title_element = title_h1
            elif (title_h2 != "None"): 
                title_element = title_h2

            date_string = day_element + " " + day_number_element + " " + month_element
        
            eventInfo = Toffler(title_element, artist_element, date_string)
            dataList.append(eventInfo)
        
        return dataList