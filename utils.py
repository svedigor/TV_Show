from bottle import template
import json

JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871","2993", "305"]

def getVersion():
    return "0.0.1"

def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"


#
#d = []
#x = json.loads(getJsonFromFile("7"))
#d.append(x['_embedded']["episodes"][0]["summary"])
#print(d[0][3:-4])
#print(d)
#if "Al Qaeda" in d[0][3:-4]:
#    print("ok")
#










#print(result['_embedded']['episodes'][1])
#print(x["url"])
#for key, value in x.items():
#    print(key, " : ", value)
#result = []

#data = ["id","rating", "image","name"]
#for i in AVAILABE_SHOWS:
#    x = json.loads(getJsonFromFile(i))
#    for key in x:
#        if key in data:
#            new_data = {
#                "url": x["url"],
#                "rating": x["rating"],
#                "image": x["image"],
#                "name": x["name"]
#            }
#            result.append(new_data)
#print(result)




#print(x)



