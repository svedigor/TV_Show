import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template, error)
import utils

import requests
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

# home page
@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

#assignment routes
@route('/browse')
def browse():
    result = utils.data_of_shows(utils.api_shows_address,utils.AVAILABE_SHOWS)
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = result)

@route('/ajax/show/<id>')
def show(id):
    result = utils.get_show(id)
    sectionTemplate = "./templates/show.tpl"
    return template(sectionTemplate, version=utils.getVersion(),
                    result=result)

@route('/ajax/show/<showId>/episode/<episodeId>')
def episode (showId, episodeId):
    result = utils.get_episode(showId,episodeId)
    sectionTemplate = "./templates/episode.tpl"
    return template(sectionTemplate, version=utils.getVersion(),
                    result=result)

@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

@route('/search', method = "POST")
def search_result():
    query = request.forms.get("q")
    results = utils.search_result(query)
    sectionTemplate = "./templates/search_result.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData = {}, query=query, results=results)

@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})
run(host='localhost', port=os.environ.get('PORT', 7000))
