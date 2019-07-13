import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template, error)
import utils
import api_data
# Static Routes

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")

@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")

@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")

@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

@route('/browse')
def browse():
    #api = "http://api.tvmaze.com/shows"  #--- these are all available shows that API contains( 240 shows)
    #result = requests.get(api).json()

    result =api_data.result_data   # --- cerated appi_data.py to get data from API with dafault shows

#  --- bottom code to get default data from utils.py
#   result =[]
#   for i in utils.AVAILABE_SHOWS:
#       x = json.loads(utils.getJsonFromFile(i))
#       result.append(x)
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = result)


@route('/ajax/show/<id>')
def show(id):
    result = api_data.get_show(id)
    sectionTemplate = "./templates/show.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=result)

@route('/ajax/show/<showId>/episode/<episodeId>')
def episode (showId, episodeId):
    show_result = api_data.get_show(showId)
    episodes_data = show_result['_embedded']['episodes']
    for i in episodes_data:
        if i["id"] == int(episodeId):
            result  = i
            break
    sectionTemplate = "./templates/episode.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=result)

@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})
run(host='localhost', port=os.environ.get('PORT', 7000))
