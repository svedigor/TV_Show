import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template, error)
import utils
import json
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
    result =[]
    for i in utils.AVAILABE_SHOWS:
        x = json.loads(utils.getJsonFromFile(i))
        result.append(x)
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = result)


@route('/ajax/show/<id>')
def show(id):
    result = json.loads(utils.getJsonFromFile(id))
    sectionTemplate = "./templates/show.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=result)

@route('/ajax/show/7/episode/189')
def episode ():
    base = json.loads(utils.getJsonFromFile("7"))
    result = base['_embedded']['episodes'][0]
    sectionTemplate = "./templates/episode.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=result)

@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})


#@error(404)
#def error404(error):
#   return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {[})
run(host='localhost', port=os.environ.get('PORT', 7000))
