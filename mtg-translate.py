import requests
import json


def get_correct_name(old_name):
    url = "https://api.scryfall.com/cards/named?fuzzy="
    url_l = url+old_name.replace(" ","+")
    r = requests.get(url_l)
    result = json.loads(r.text)
    if ("name" in result.keys()) :
        return result["name"]
    else:
        return old_name+"-ERROR"


old = "./deck.txt"
new = "./new_deck.txt"
old_f= open(old,"r")
new_f = open(new,"w+")
cards = {}
for line in old_f.readlines():
    line = line[:-1]
    number,name = line.split(" ",1)
    new_name = get_correct_name(name)
    if (new_name not in cards.keys()):
        cards[new_name] = 1
        new_f.write("1 {}\n".format(new_name))
