from bottle import template
import requests
import json

JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871","2993", "305"]

api_shows_address = "http://api.tvmaze.com/shows/"

def getVersion():
    return "0.0.1"

def getJsonFromFile(showName: object) -> object:
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"

def get_show(showName):
    try:
        episodes_json = requests.get(api_shows_address + showName + "/" + "episodes").json()
        show_json = requests.get(api_shows_address + showName).json()
        show_json["_embedded"] = {"episodes": episodes_json}
        return show_json
    except:
        return "{}"

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

def get_episodes(showId):
    result = get_show(showId)
    return result["_embedded"]["episodes"]

def get_episode(showId,episodeId):
    try:
        episodes_data = get_episodes(showId)
        for i in episodes_data:
            if i["id"] == int(episodeId):
                result  = i
                return result
    except:
        return "{}"

def search_result(query):
    result = []
    shows = data_of_shows(api_shows_address,AVAILABE_SHOWS)
    for show in shows:
        json_show = json.dumps(show["id"])
        episodes = get_episodes(json_show)
        for episode in episodes:
            if (episode['name'] and episode['name'].find(query) != -1) or (episode['summary'] and episode['summary'].find(query) != -1):
                text = show['name'] + ": " + episode['name']
                result.append({"showid":json_show, "episodeid":episode['id'], "text":text})
    return result

