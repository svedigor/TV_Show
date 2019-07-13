import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template, error)
import utils
import json
result = []

for i in utils.AVAILABE_SHOWS:
    x = json.loads(utils.getJsonFromFile(i))
    print(x['name'])
    result.append(x)

