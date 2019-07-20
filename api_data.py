import requests
import json

#api_episodes_address= "http://api.tvmaze.com/shows/:showID/episodes"  ---  API for episodes
#api = "http://api.tvmaze.com/shows"  # --- these are all available shows that API contains( 240 shows)
#result = requests.get(api).json()


# --- bottom code to get default data from utils.py
##result =[]
##for i in utils.AVAILABE_SHOWS:
##    x = json.loads(utils.getJsonFromFile(i))
##    result.append(x)


api_shows_address = "http://api.tvmaze.com/shows/"
my_shows = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871","2993", "305"]

def data_of_shows(api_address,shows):
    result_data = []
    for i in shows:
        episodes_address = requests.get(api_address + i+"/" +"episodes").json()
        show_adress = requests.get(api_address+i).json()
        show_adress["_embedded"] = {"episodes":episodes_address}
        result_data.append(show_adress)
    try:
        return result_data
    except:
        return "{}"
#result_data = data_of_shows(api_shows_address,my_shows)


def get_show(showName):
    try:
        episodes_address = requests.get(api_shows_address + showName + "/" + "episodes").json()
        show_adress = requests.get(api_shows_address + showName).json()
        show_adress["_embedded"] = {"episodes": episodes_address}
        return show_adress
    except:
        return "{}"

