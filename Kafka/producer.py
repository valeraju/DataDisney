import json
import time
import urllib.request
import Scraper.ThemePark, Scraper.Special, Scraper.Schedules
import Scraper.parsingHTML_disney
import kafka

url_magickingdom = "https://parksapi.herokuapp.com/api/dlp-mk"
url_studios = "https://parksapi.herokuapp.com/api/dlp-wds"

producer = kafka.KafkaProducer(bootstrap_servers="localhost:9092")
json_file = {}
studios_list = {}
magickingdom_list = {}
while True:
    try:
        theme_parks = Scraper.parsingHTML_disney.get_themepark()
        parcs = []
        json_file["name"] = "Disneyland Paris"

        response1 = urllib.request.urlopen(url_magickingdom)
        response2 = urllib.request.urlopen(url_studios)

        attractions1 = json.loads(response1.read().decode())
        attractions2 = json.loads(response2.read().decode())

        magickingdom_list["name"] = "DisneylandParisMagicKingdom"
        magickingdom_list["attractions"] = attractions1
        magickingdom_schedules = theme_parks[0].schedules
        magickingdom_list["schedules_times"] = {"date" : magickingdom_schedules.date, "state" : magickingdom_schedules.state, "opening_time" : str(magickingdom_schedules.opening_time), "closing_time" : str(magickingdom_schedules.closing_time), "special" : {"opening_time" : str(magickingdom_schedules.special.opening_time), "closing_time" : str(magickingdom_schedules.special.closing_time), "state" : magickingdom_schedules.special.state}}

        studios_list["name"] = "DisneylandParisWaltDisneyStudios"
        studios_list["attractions"] = attractions2
        studios_schedules = theme_parks[1].schedules
        studios_list["schedules_times"] = {"date" : studios_schedules.date, "state" : studios_schedules.state, "opening_time" : str(studios_schedules.opening_time), "closing_time" : str(studios_schedules.closing_time), "special" : {"opening_time" : str(studios_schedules.special.opening_time), "closing_time" : str(studios_schedules.special.closing_time), "state" : studios_schedules.special.state}}

        parcs.append(magickingdom_list)
        parcs.append(studios_list)

        json_file["parcs"] = parcs

    except urllib.error.URLError as e:
        print(e.reason)

    producer.send("topic_attractions", json.dumps(json_file).encode())
    print(json_file)
    time.sleep(10)