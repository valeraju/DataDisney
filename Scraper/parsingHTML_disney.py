import urllib.request
from bs4 import BeautifulSoup
import re
import Scraper.Schedules as Schedules, Scraper.ThemePark as ThemePark, Scraper.Special as Special
import datetime

#Récupération du code source de la page web Queue Times
link = 'http://www.disneylandparis.fr/calendriers/horaires-parcs/#'


def get_beautifulsoup(link):
    req = urllib.request.Request(link, headers={'User-Agent': "Magic Browser"})
    con = urllib.request.urlopen(req)
    return BeautifulSoup(con.read(), 'html.parser')


soup = get_beautifulsoup(link)
# disneyland_park = ThemePark.ThemePark("Disneyland Park Paris", "10:00 - 21:00")


def convert_str_to_datetime(date_time_str):
    return datetime.datetime.strptime(date_time_str, '%H:%M').time()


def get_themepark():
    global soup
    theme_parks = []
    date_of_day = soup.find('div', {'class': 'hoursDate'}).get_text()
    time_now = datetime.datetime.now().time()
    # state = soup1.findAll(True, {'class': ['panel panel-success', 'panel panel-danger']})[0].find("h1").get_text()
    for tag in soup.find_all('li', {'itemtype': 'http://schema.org/TouristAttraction'}):
        opening_time = (tag.select('span')[0].get_text()).replace("h", ":")
        opening_time_format_datetime = convert_str_to_datetime(opening_time)
        closing_time = (tag.select('span')[1].get_text()).replace("h", ":")
        closing_time_format_datetime = convert_str_to_datetime(closing_time)
        if(opening_time_format_datetime <= time_now and time_now <= closing_time_format_datetime):
            state = "Operating"
        else:
            state = "Closed"
        special_string = tag.find('div', {'class': 'hours extraMagicHours'}).get_text()
        special_opening_time = convert_str_to_datetime(re.search("([0-9]{1,2}h[0-9]{1,2}) à ([0-9]{1,2}h[0-9]{1,2})", special_string).group(1).replace("h", ":"))
        special_closing_time = convert_str_to_datetime(re.search("([0-9]{1,2}h[0-9]{1,2}) à ([0-9]{1,2}h[0-9]{1,2})", special_string).group(2).replace("h", ":"))
        name_park = tag.find('div', {'class': 'pkTitle'}).get_text().strip()
        special = Special.Special(opening_time=special_opening_time, closing_time=special_closing_time, state="Extra Magic Hours")
        time_schedules = Schedules.Schedules(date_of_day, state, opening_time, closing_time, special)
        theme_parks.append(ThemePark.ThemePark(name_park, time_schedules))

    return theme_parks


