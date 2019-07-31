#Found in https://gist.github.com/stp-ip/5759205, few changes were made


# run script within a directory where your json is

import json
from copy import deepcopy

json_data = open('./data.json')
data = json.load(json_data)

default = deepcopy(data)
l = len(default)

for i in range(l):
    name = './json-splits/json_' + str(i+1) + '.json'
    with open(name, 'w') as outfile:
      json.dump(default[i], outfile)
