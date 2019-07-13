import requests
data = {}
api_address = "http://api.tvmaze.com/shows/7/episodes"
api_address1 = "http://api.tvmaze.com/shows/7"

to_add = requests.get(api_address).json()
to_add1 = requests.get(api_address1).json()

#print(to_add)
#data["_embedded"] = {
#        "episodes":to_add
#    }

to_add1["_embedded"] = {
        "episodes":to_add
   }

#print(to_add1)
#for i, key in to_add1.items():
#    print(i,":",key)
x = to_add1['_embedded']['episodes']
for i in x:
    print(i)



